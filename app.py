import time
import os
import json
import yaml
import atexit
import paho.mqtt.client as mqtt
import threading
import logging
import sys
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format with timestamp
    datefmt="%Y-%m-%d %H:%M:%S"  # Date format
)

# Load configuration from config.yaml
if os.path.exists('/data/options.json'):
    logging.info("Loading options.json")
    with open(r'/data/options.json') as file:
        config = json.load(file)
        logging.info("Config: " + json.dumps(config))
elif os.path.exists('victron\\config.yaml'):
    logging.info("Loading config.yaml")
    with open(r'victron\\config.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)['options']
else:
    sys.exit("No config file found")

# Configuration settings
HA_MQTT_BROKER = config['ha_mqtt_host']
HA_MQTT_PORT = config['ha_mqtt_port']
HA_MQTT_USER = config['ha_mqtt_user']
HA_MQTT_PASSWORD = config['ha_mqtt_password']
HA_MQTT_BASE_TOPIC = 'victron'
HA_MQTT_DISCOVERY_TOPIC = 'homeassistant'


CERBO_MQTT_BROKER = config['cerbo_mqtt_host']
CERBO_MQTT_PORT = config['cerbo_mqtt_port']
CERBO_MQTT_USER = config['cerbo_mqtt_user']
CERBO_MQTT_PASSWORD = config['cerbo_mqtt_password']
CERBO_SERIAL_NO = config['cerbo_serial_no']




def ha_on_connect(client, userdata, flags, rc):
    logging.info("Connected to MQTT broker")
    # Subscribe here to topics in HA that we need to listen to i.e. set SoC topic etc.

def ha_on_disconnect(client, userdata, rc):
    if rc != 0:
        logging.error("Unexpected disconnection.")
    else:
        logging.error("Disconnected successfully.")
    logging.error("Disconnected from HA MQTT broker")


def ha_on_message(client, userdata, msg):
    # Get the topic
    topic = msg.topic

    # Split the topic into parts by '/'
    topic_parts = topic.split('/')
    pass
    # Pass message on to Cerbo if its on a certain topic
    # 

def cerbo_on_connect(client, userdata, flags, rc):
    logging.info("Connected to Cerbo MQTT broker")
    # Subscribe here to Cerbo topics thats we are interested in

def cerbo_on_disconnect(client, userdata, rc):
    if rc != 0:
        logging.error("Unexpected cerbo disconnection.")
    else:
        logging.error("Disconnected cerbo successfully.")
    logging.error("Disconnected from cerbo MQTT broker")


def cerbo_on_message(client, userdata, msg):
    # Get the topic
    topic = msg.topic

    # Split the topic into parts by '/'
    topic_parts = topic.split('/')
    pass
    # Pass message on to HA on correct topic

# Initialize HA MQTT client
ha_mqtt_client = mqtt.Client()
ha_mqtt_client.on_connect = ha_on_connect
ha_mqtt_client.on_disconnect = ha_on_disconnect
ha_mqtt_client.on_message = ha_on_message
ha_mqtt_client.username_pw_set(username=HA_MQTT_USER, password=HA_MQTT_PASSWORD)
ha_mqtt_client.connect(HA_MQTT_BROKER, HA_MQTT_PORT, 60)
ha_mqtt_client.loop_start()

# Initialize HA MQTT client
cerbo_mqtt_client = mqtt.Client()
cerbo_mqtt_client.on_connect = cerbo_on_connect
cerbo_mqtt_client.on_disconnect = cerbo_on_disconnect
cerbo_mqtt_client.on_message = cerbo_on_message
cerbo_mqtt_client.username_pw_set(username=CERBO_MQTT_USER, password=CERBO_MQTT_PASSWORD)
cerbo_mqtt_client.connect(CERBO_MQTT_BROKER, CERBO_MQTT_PORT, 60)
cerbo_mqtt_client.loop_start()


# Clean up on exit
def exit_handler():
    logging.error("Script exiting")
    ha_mqtt_client.publish(f"{HA_MQTT_BASE_TOPIC}_{CERBO_SERIAL_NO}/availability", "offline")
    ha_mqtt_client.loop_stop()

atexit.register(exit_handler)

# HA Discovery Function
def ha_discovery():
    logging.info("Publishing HA Discovery topics...")
    # Define device information
    device = {
        "manufacturer": "Victron",
        "model": "XYZ",
        "identifiers": [f"victron_{CERBO_SERIAL_NO}"],
        "name": f"Victron {CERBO_SERIAL_NO}"
    }

    # Base availability topic
    availability_topic = f"{HA_MQTT_BASE_TOPIC}_{CERBO_SERIAL_NO}/availability"

    # Define all sensor parameters and publish discovery messages
    parameters = {
        "Module Voltage": {"device_class": "voltage", "unit": "V"},
        "Module Current": {"device_class": "current", "unit": "A"},
        "Rated Current": {"device_class": "current", "unit": "A"},
        "Rated Power": {"device_class": "current", "unit": "W"},
        "Current Limit": {"device_class": "current", "unit": "A"},
        "Temperature of DC Board": {"device_class": "temperature", "unit": "°C"},
        "Input Phase Voltage": {"device_class": "voltage", "unit": "V"},
        "PFC0 Voltage": {"device_class": "voltage", "unit": "V"},
        "PFC1 Voltage": {"device_class": "voltage", "unit": "V"},
        "Panel Board Temperature": {"device_class": "temperature", "unit": "°C"},
        "Voltage Phase A": {"device_class": "voltage", "unit": "V"},
        "Voltage Phase B": {"device_class": "voltage", "unit": "V"},
        "Voltage Phase C": {"device_class": "voltage", "unit": "V"},
        "Temperature of PFC Board": {"device_class": "temperature", "unit": "°C"},
        "Input Power": {"device_class": "power", "unit": "W"},
        "Current Altitude": {"device_class": "none", "unit": "m"},
        "Input Working Mode": {"device_class": "none", "unit": None},
        "Alarm Status": {"device_class": "none", "unit": None}
    }

    for param, details in parameters.items():
        discovery_payload = {
            "name": param,
            "unique_id": f"victron_{CERBO_SERIAL_NO}_{param.replace(' ', '_').lower()}",
            "state_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/{param.replace(' ', '_').lower()}",
            "availability_topic": availability_topic,
            "device": device,
            "device_class": details.get("device_class"),
            "unit_of_measurement": details.get("unit"),
        }
        discovery_topic = f"{HA_MQTT_DISCOVERY_TOPIC}/sensor/victron_{CERBO_SERIAL_NO}/{param.replace(' ', '_').lower()}/config"
        ha_mqtt_client.publish(discovery_topic, json.dumps(discovery_payload), retain=True)

    # Define settable parameters as MQTT number entities
    settable_parameters = {
        "Current Limit": {"min": 0, "max": 1, "step": 0.1, "unit": "A", "command_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/set/current_limit"},
        "Output Voltage": {"min": 735, "max": 810, "step": 0.1, "unit": "V", "command_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/set/output_voltage"},
        "Output Current": {"min": 0, "max": 1, "step": 0.1, "unit": "A", "command_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/set/current"},
        "Altitude": {"min": 0, "max": 5000, "step": 100, "unit": "m", "command_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/set/altitude"},
    }

    # Publish discovery messages for settable parameters
    for param, details in settable_parameters.items():
        discovery_payload = {
            "name": param,
            "unique_id": f"victron_{CERBO_SERIAL_NO}_{param.replace(' ', '_').lower()}",
            "command_topic": details["command_topic"],
            "min": details["min"],
            "max": details["max"],
            "step": details["step"],
            "unit_of_measurement": details["unit"],
            "availability_topic": availability_topic,
            "device": device
        }
        discovery_topic = f"{HA_MQTT_DISCOVERY_TOPIC}/number/victron_{CERBO_SERIAL_NO}/{param.replace(' ', '_').lower()}/config"
        ha_mqtt_client.publish(discovery_topic, json.dumps(discovery_payload), retain=True)


    ha_mqtt_client.publish(availability_topic, "online")



# Main loop to continuously read parameters
try:
    ha_discovery()
    while True:
        time.sleep(0.5)
        pass
except Exception as e:
    logging.error(f"An error occurred: {e}")
    logging.error("Traceback: %s", traceback.format_exc())
    exit_handler()
except KeyboardInterrupt:
    logging.error("Stopping script...")
    exit_handler()