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
from victron_map import READ_PARAMETER_MAP

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
INVERTER_MODEL = config['inverter_model']
HA_MQTT_BROKER = config['ha_mqtt_host']
HA_MQTT_PORT = config['ha_mqtt_port']
HA_MQTT_USER = config['ha_mqtt_user']
HA_MQTT_PASSWORD = config['ha_mqtt_password']
HA_MQTT_BASE_TOPIC = 'victron'
HA_MQTT_DISCOVERY_TOPIC = 'homeassistant'


CERBO_MQTT_BROKER = config['cerbo_mqtt_host']
CERBO_MQTT_PORT = config['cerbo_mqtt_port']
# CERBO_MQTT_USER = config['cerbo_mqtt_user']
# CERBO_MQTT_PASSWORD = config['cerbo_mqtt_password']
CERBO_SERIAL_NO = config['cerbo_serial_no']
SOLARCHARGERS = config['solarchargers']
GRID_METERS = config['grid_meters']

ha_mqtt_connected = False


def ha_on_connect(client, userdata, flags, rc):
    global ha_mqtt_connected
    ha_mqtt_connected = True
    logging.info("Connected to MQTT broker")
    # Subscribe here to topics in HA that we need to listen to i.e. set SoC topic etc.

def ha_on_disconnect(client, userdata, rc):
    global ha_mqtt_connected
    ha_mqtt_connected = False
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
    
# Initialize HA MQTT client
ha_mqtt_client = mqtt.Client()
ha_mqtt_client.on_connect = ha_on_connect
ha_mqtt_client.on_disconnect = ha_on_disconnect
ha_mqtt_client.on_message = ha_on_message
ha_mqtt_client.username_pw_set(username=HA_MQTT_USER, password=HA_MQTT_PASSWORD)
ha_mqtt_client.connect(HA_MQTT_BROKER, HA_MQTT_PORT, 60)
ha_mqtt_client.loop_start()

def cerbo_on_connect(client, userdata, flags, rc):
    logging.info("Connected to Cerbo MQTT broker")
    cerbo_mqtt_client.subscribe(f'N/{CERBO_SERIAL_NO}/#')
    cerbo_mqtt_client.subscribe(f'W/{CERBO_SERIAL_NO}/#')
    # Subscribe here to Cerbo topics thats we are interested in

def cerbo_on_disconnect(client, userdata, rc):
    if rc != 0:
        logging.error("Unexpected cerbo disconnection.")
    else:
        logging.error("Disconnected cerbo successfully.")
    logging.error("Disconnected from cerbo MQTT broker")


def cerbo_on_message(client, userdata, msg):
    global ha_mqtt_connected
    global ha_mqtt_client
    if ha_mqtt_connected == True:
        # Get the topic and payload
        topic = msg.topic
        payload = msg.payload.decode("utf-8")

        # Split the topic into parts by '/'
        topic_parts = topic.split("/")
        module_type = topic_parts[2]
        module_id = topic_parts[3]
        topic_suffix = "/".join(topic_parts[4:])  # Get the part after the ID

        # Find the matching parameter in READ_PARAMETER_MAP
        for param, details in READ_PARAMETER_MAP.items():
            if details["topic"] == topic_suffix:
                # Found a match, construct Home Assistant topic and payload
                ha_topic = f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/{module_type}/{module_id}/{param.replace(' ', '_').lower()}"
                payload_json = json.loads(payload)
                ha_payload = round(payload_json["value"], 2)
                # Publish to the Home Assistant topic
                ha_mqtt_client.publish(ha_topic, ha_payload, retain=False)
                ha_mqtt_client.publish(f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/availability", "online")
                print(f"Published to {ha_topic}: {ha_payload}")
                break
        else:
            pass
            # print(f"Topic {topic_suffix} not found in READ_PARAMETER_MAP")
    else:
        print("MQTT not connected ... ")

# Initialize HA MQTT client
cerbo_mqtt_client = mqtt.Client()
cerbo_mqtt_client.on_connect = cerbo_on_connect
cerbo_mqtt_client.on_disconnect = cerbo_on_disconnect
cerbo_mqtt_client.on_message = cerbo_on_message
# cerbo_mqtt_client.username_pw_set(username=CERBO_MQTT_USER, password=CERBO_MQTT_PASSWORD)
cerbo_mqtt_client.connect(CERBO_MQTT_BROKER, CERBO_MQTT_PORT, 60)
cerbo_mqtt_client.loop_start()


# Clean up on exit
def exit_handler():
    logging.error("Script exiting")
    ha_mqtt_client.publish(f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/availability", "offline")
    ha_mqtt_client.loop_stop()

atexit.register(exit_handler)

# HA Discovery Function
def ha_discovery_solarchargers():
    # Base availability topic
    availability_topic = f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/availability"
    logging.info("Publishing HA Solarcharger Discovery topics...")
    
    for solarcharger in SOLARCHARGERS:
    
        # Define device information
        device = {
            "manufacturer": "Victron",
            "model": solarcharger['model'],
            "identifiers": [f"victron_{CERBO_SERIAL_NO}_solarcharger_{solarcharger['id']}"],
            "name": f"Victron {solarcharger['name']}"
        }
    
    # Filter items with the specified module type


        for param, details in READ_PARAMETER_MAP.items():
            if details['module_type'] == 'solarcharger':
                discovery_payload = {
                    "name": param,
                    "unique_id": f"victron_{CERBO_SERIAL_NO}_{param.replace(' ', '_').lower()}",
                    "state_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/solarcharger/{solarcharger['id']}/{param.replace(' ', '_').lower()}",
                    "availability_topic": availability_topic,
                    "device": device,
                    "device_class": details.get("device_class"),
                    "unit_of_measurement": details.get("unit"),
                }
                discovery_topic = f"{HA_MQTT_DISCOVERY_TOPIC}/sensor/victron_{CERBO_SERIAL_NO}/solarcharger/{solarcharger['id']}/{param.replace(' ', '_').lower()}/config"
                ha_mqtt_client.publish(discovery_topic, json.dumps(discovery_payload), retain=True)

    ha_mqtt_client.publish(availability_topic, "online")



# Main loop to continuously read parameters
try:
    if len(SOLARCHARGERS) > 0:
        ha_discovery_solarchargers()
    while True:
        time.sleep(5)
        if cerbo_mqtt_client.is_connected():
            cerbo_mqtt_client.publish(f"R/{CERBO_SERIAL_NO}/keepalive")
        pass
except Exception as e:
    logging.error(f"An error occurred: {e}")
    logging.error("Traceback: %s", traceback.format_exc())
    exit_handler()
except KeyboardInterrupt:
    logging.error("Stopping script...")
    exit_handler()