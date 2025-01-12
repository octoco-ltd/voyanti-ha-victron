import yaml

# Load the configuration YAML
with open("mqtt_sensors.yaml", "r") as file:
    mqtt_config = yaml.safe_load(file)

# Initialize the parameters dictionary
parameters = {}

# Process sensors
for sensor in mqtt_config.get("sensor", []):
    name = sensor.get("name", "Unknown Parameter")
    device_class = sensor.get("device_class", "none")
    unit = sensor.get("unit_of_measurement", None)
    state_topic = sensor.get("state_topic", "")

    # Extract the topic after the ID (e.g., c0847d9b49b3)
    topic_parts = state_topic.split("/")
    topic_after_id = "/".join(topic_parts[2:]) if len(topic_parts) > 2 else ""

    # Add the parameter to the dictionary
    parameters[name] = {
        "device_class": device_class,
        "unit": unit,
        "topic": topic_after_id
    }

# Output the resulting parameters dictionary
print(parameters)