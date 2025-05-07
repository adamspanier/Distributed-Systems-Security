import paho.mqtt.client as mqtt
import random
import time
import json
import requests
import socket
from influxdb_client import InfluxDBClient, Point, WritePrecision

# MQTT Broker Details
MQTT_BROKER = "mqtt-broker"  # Updated for encrypted environment
MQTT_PORT = 8883
MQTT_TOPIC = "dcs/plc/data"

# InfluxDB
INFLUXDB_URL = "https://influxdb-secure:8097"
INFLUXDB_TOKEN = "4amA3Ofsh12fWB2R4ZKtlhFC9tOe9xgV4M8zhAw2zj4zp1sP143QYcaqRfyJ65YfpD-vBiRfY62RbLc1pfyvKQ=="  # InfluxDB token
INFLUXDB_ORG = "my-org"  # The InfluxDB organization name
INFLUXDB_BUCKET = "plc_data"  # The target bucket

# Create InfluxDB client using the token-based authentication
influx_client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)

write_api = influx_client.write_api()

# Retry logic for MQTT connection
def connect_mqtt(client):
    while True:
        try:
            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            print("Connected to MQTT Broker")
            return
        except socket.error as e:
            print(f"[MQTT] Connection failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)

def generate_plc_data(plc_id):
    return {
        "plc_id": plc_id,
        "temperature": round(random.uniform(20, 100), 2),
        "pressure": round(random.uniform(1, 10), 2),
        "flow_rate": round(random.uniform(5, 50), 2),
        "timestamp": int(time.time())
    }

# Publish data to MQTT and InfluxDB
def publish_data(mqtt_client):
    plc_ids = [1, 2, 3]
    while True:
        for plc_id in plc_ids:
            data = generate_plc_data(plc_id)
            payload = json.dumps(data)

            # Publish to MQTT
            mqtt_client.publish(MQTT_TOPIC, payload)
            print(f"[MQTT] Published: {payload}")

            # Write to InfluxDB
            try:
                point = (
                    Point("plc_data")
                    .tag("plc_id", str(data["plc_id"]))
                    .field("temperature", data["temperature"])
                    .field("pressure", data["pressure"])
                    .field("flow_rate", data["flow_rate"])
                    .time(data["timestamp"], WritePrecision.S)
                )
                write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)
                print("[InfluxDB] Data pushed successfully")
            except Exception as e:
                print(f"[InfluxDB] Failed to push: {e}")

            time.sleep(5)  # simulate interval between messages

if __name__ == "__main__":
    mqtt_client = mqtt.Client()
    connect_mqtt(mqtt_client)
    mqtt_client.loop_start()

    try:
        publish_data(mqtt_client)
    except KeyboardInterrupt:
        print("Stopped by user")
        mqtt_client.loop_stop()