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

# Map numbers to logging levels
LOG_LEVEL_MAP = {
    0: logging.CRITICAL,
    1: logging.ERROR,
    2: logging.WARNING,
    3: logging.INFO,
    4: logging.DEBUG
}

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


log_level = LOG_LEVEL_MAP.get(config.get('debug', 2), logging.INFO)  # Default to INFO if out of range
# Configure logging
logging.basicConfig(
    level=log_level,  # Set logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format with timestamp
    datefmt="%Y-%m-%d %H:%M:%S"  # Date format
)

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
CERBO_MODEL = config['cerbo_model']
SOLARCHARGERS = config['solarchargers']
GRID_METERS = config['grid_meters']

ha_mqtt_connected = False

# Initialize HA MQTT client
ha_mqtt_client = mqtt.Client()
cerbo_mqtt_client = mqtt.Client()


def ha_on_connect(client, userdata, flags, rc):
    global ha_mqtt_connected
    ha_mqtt_connected = True
    ha_mqtt_client.subscribe(f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/settings/set/#")
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
    if topic == f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/settings/set/min_soc_limit":
        print(f"W/{CERBO_SERIAL_NO}/settings/0/Settings/CGwacs/BatteryLife/MinimumSocLimit")
        payload = msg.payload.decode("utf-8")
        ha_paylod = json.dumps({ "value": payload })
        cerbo_mqtt_client.publish(f"W/{CERBO_SERIAL_NO}/settings/0/Settings/CGwacs/BatteryLife/MinimumSocLimit", ha_paylod)
        

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

    if ha_mqtt_connected:
        # Get the topic and payload
        topic = msg.topic
        payload = msg.payload.decode("utf-8")

        # Split the topic into parts by '/'
        topic_parts = topic.split("/")
        if len(topic_parts) < 4:
            return

        module_type = topic_parts[2]
        module_id = topic_parts[3]
        topic_suffix = "/".join(topic_parts[4:])  # Get the part after the ID

        # Correctly match topic_suffix with READ_PARAMETER_MAP
        for param, details in READ_PARAMETER_MAP.items():
            expected_suffix = details["topic"]
            if topic_suffix == expected_suffix:  # Exact match with full topic from victron_map.py
                ha_topic = f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/{module_type}/{module_id}/{param.replace(' ', '_').lower()}"
                payload_json = json.loads(payload)
                if "map" in details:
                    ha_payload = details["map"].get(payload_json["value"])
                else:
                    ha_payload = round(payload_json["value"], 2)
                # Publish to the Home Assistant topic
                ha_mqtt_client.publish(ha_topic, ha_payload, retain=False)
                ha_mqtt_client.publish(f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/availability", "online")
                logging.debug(f"Published to {ha_topic}: {ha_payload}")
                return  # Exit once a match is found
            
        if topic == f"N/{CERBO_SERIAL_NO}/settings/0/Settings/CGwacs/BatteryLife/MinimumSocLimit":
            payload_json = json.loads(payload)
            ha_payload = round(payload_json["value"], 2)
            ha_mqtt_client.publish(f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/settings/get/min_soc_limit", ha_payload, retain=False)
        else:
            logging.warning(f"No match found for topic_suffix: {topic_suffix}")
    else:
        logging.info("MQTT not connected ...")

# Initialize HA MQTT client
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

# HA Discovery Function for Solarchargers
def ha_discovery_solarchargers():
    availability_topic = f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/availability"
    logging.info("Publishing HA Solarcharger Discovery topics...")
    
    for solarcharger in SOLARCHARGERS:
        device = {
            "manufacturer": "Victron",
            "model": solarcharger['model'],
            "identifiers": [f"victron_{CERBO_SERIAL_NO}_solarcharger_{solarcharger['id']}"],
            "name": f"{solarcharger['name']}"
        }

        for param, details in READ_PARAMETER_MAP.items():
            if details['module_type'] == 'solarcharger':
                # Use only the parameter (e.g., "Current") for the entity name
                display_name = param.replace('MPPT', '').strip()  # e.g., "Current" or "Voltage"

                # Log the generated name for debugging
                logging.debug(f"Generated display_name: {display_name}")

                discovery_payload = {
                    "name": display_name,  # Entity name is concise
                    "unique_id": f"solarcharger_{solarcharger['id']}_{param.replace(' ', '_').lower()}",
                    "state_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/solarcharger/{solarcharger['id']}/{param.replace(' ', '_').lower()}",
                    "availability_topic": availability_topic,
                    "device": device,
                    "device_class": details.get("device_class"),
                    "unit_of_measurement": details.get("unit"),
                }

                discovery_topic = f"{HA_MQTT_DISCOVERY_TOPIC}/sensor/solarcharger_{solarcharger['id']}_{param.replace(' ', '_').lower()}/config"
                ha_mqtt_client.publish(discovery_topic, json.dumps(discovery_payload), retain=True)

    ha_mqtt_client.publish(availability_topic, "online")

# HA Discovery Function for Grid Meters
def ha_discovery_grid():
    availability_topic = f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/availability"
    logging.info("Publishing HA Grid Meter Discovery topics...")
    
    for grid in GRID_METERS:
        device = {
            "manufacturer": "Victron",
            "model": grid['model'],
            "identifiers": [f"victron_{CERBO_SERIAL_NO}_grid_{grid['id']}"],
            "name": f"{grid['name']}"  # Keep "Grid Meter" as defined in GUI config
        }

        for param, details in READ_PARAMETER_MAP.items():
            if details['module_type'] == 'grid':
                # Remove "Grid" from the parameter name
                display_name = param.replace('Grid', '').strip()  # e.g., "L3 Current"

                # Log the generated name for debugging
                logging.debug(f"Generated display_name: {display_name}")

                discovery_payload = {
                    "name": display_name,  # Use concise entity name
                    "unique_id": f"grid_{grid['id']}_{param.replace(' ', '_').lower()}",
                    "state_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/grid/{grid['id']}/{param.replace(' ', '_').lower()}",
                    "availability_topic": availability_topic,
                    "device": device,
                    "device_class": details.get("device_class"),
                    "unit_of_measurement": details.get("unit"),
                }

                discovery_topic = f"{HA_MQTT_DISCOVERY_TOPIC}/sensor/grid_{grid['id']}_{param.replace(' ', '_').lower()}/config"
                ha_mqtt_client.publish(discovery_topic, json.dumps(discovery_payload), retain=True)

    ha_mqtt_client.publish(availability_topic, "online")

# HA Discovery Function for Cerbo        
def ha_discovery_cerbo():
    # Base availability topic
    availability_topic = f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/availability"
    logging.info("Publishing HA Cerbo Discovery topics...")

    # Define device information
    device = {
        "manufacturer": "Victron",
        "model": CERBO_MODEL,
        "identifiers": [f"victron_{CERBO_SERIAL_NO}_cerbo"],
        "name": f"{CERBO_MODEL}"
    }

    # Publish discovery messages for existing parameters
    for param, details in READ_PARAMETER_MAP.items():
        if details['module_type'] == 'system' or details['module_type'] == 'settings':
            discovery_payload = {
                "name": f"{param}",
                "unique_id": f"victron_{CERBO_SERIAL_NO}_cerbo_{param.replace(' ', '_').lower()}",
                "state_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/{details['module_type']}/0/{param.replace(' ', '_').lower()}",
                "availability_topic": availability_topic,
                "device": device,
                "device_class": details.get("device_class"),
                "unit_of_measurement": details.get("unit"),
            }
            discovery_topic = f"{HA_MQTT_DISCOVERY_TOPIC}/sensor/victron_{CERBO_SERIAL_NO}/cerbo_{param.replace(' ', '_').lower()}/config"
            ha_mqtt_client.publish(discovery_topic, json.dumps(discovery_payload), retain=True)

    # Add `min_soc_limit` as a number entity
    min_soc_limit_payload = {
        "name": "Minimum SOC Limit",
        "unique_id": f"victron_{CERBO_SERIAL_NO}_cerbo_min_soc_limit",
        "command_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/settings/set/min_soc_limit",
        "state_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/settings/get/min_soc_limit",
        "min": 20,
        "max": 100,
        "step": 5,
        "mode": "slider",
        "device_class": "battery",
        "icon": "mdi:battery-heart-outline",
        "unit_of_measurement": "%",
        "device": device
    }
    min_soc_limit_discovery_topic = f"{HA_MQTT_DISCOVERY_TOPIC}/number/{CERBO_SERIAL_NO}_min_soc_limit/config"
    ha_mqtt_client.publish(min_soc_limit_discovery_topic, json.dumps(min_soc_limit_payload), retain=True)

    # Publish online availability
    ha_mqtt_client.publish(availability_topic, "online")
    
# HA Discovery Function for inverters    
def ha_discovery_inverter():
    # Base availability topic with CERBO_SERIAL_NO included
    availability_topic = f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/availability"
    logging.info("Publishing HA Inverter Discovery topics...")
    
    # Define device information
    device = {
        "manufacturer": "Victron",
        "model": INVERTER_MODEL,
        "identifiers": [f"victron_{CERBO_SERIAL_NO}_inverter"],  # Included CERBO_SERIAL_NO
        "name": f"{INVERTER_MODEL}"
    }

    for param, details in READ_PARAMETER_MAP.items():
        if details['module_type'] == 'vebus':
            discovery_payload = {
                "name": f"{param}",
                "unique_id": f"inverter_{param.replace(' ', '_').lower()}",  # Unique ID without CERBO_SERIAL_NO
                # Include CERBO_SERIAL_NO in state_topic
                "state_topic": f"{HA_MQTT_BASE_TOPIC}/{CERBO_SERIAL_NO}/{details['module_type']}/276/{param.replace(' ', '_').lower()}",
                "availability_topic": availability_topic,  # Includes CERBO_SERIAL_NO
                "device": device,
                "device_class": details.get("device_class"),
                "unit_of_measurement": details.get("unit"),
            }
            # Discovery topic does not need CERBO_SERIAL_NO
            discovery_topic = f"{HA_MQTT_DISCOVERY_TOPIC}/sensor/inverter_{param.replace(' ', '_').lower()}/config"
            ha_mqtt_client.publish(discovery_topic, json.dumps(discovery_payload), retain=True)

    # Publish online availability for inverter
    ha_mqtt_client.publish(availability_topic, "online")

# Main loop to continuously read parameters
try:
    if len(SOLARCHARGERS) > 0:
        ha_discovery_solarchargers()
    if len(GRID_METERS) > 0:
        ha_discovery_grid()
    ha_discovery_inverter()
    ha_discovery_cerbo()
    while True:
        time.sleep(30)
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