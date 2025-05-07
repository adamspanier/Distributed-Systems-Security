import paho.mqtt.client as mqtt
import random
import time
import json
import requests
import socket
from influxdb_client import InfluxDBClient, Point, WritePrecision

# MQTT Broker Details
MQTT_BROKER = "mqtt-broker-no-crypto"  # Use hostname instead of IP
MQTT_PORT = 1883
MQTT_TOPIC = "dcs/plc/data"

# InfluxDB
INFLUXDB_URL = "http://influxdb-no-crypto:8086"
INFLUXDB_TOKEN = "83_4N_dKB8V9dhzFlnAUBFvjXi0HquTpag0CH84x4AWAhITLiF1V5lBnlpmiPFpj39rsROpuyzg2bSOwTo-VNg=="  # InfluxDB token
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
# Pivoting, which is why the bottom is commented out 4/10/2025 MP
# def push_to_influxdb(data):
#     payload = f"plc_data,plc_id={data['plc_id']} temperature={data['temperature']},pressure={data['pressure']},flow_rate={data['flow_rate']} {data['timestamp']}"
#     try:
#         response = requests.post(INFLUXDB_URL, data=payload)
#         if response.status_code != 204:
#             print(f"[InfluxDB] Failed to push: {response.status_code} {response.text}")
#     except Exception as e:
#         print(f"[InfluxDB] Error: {e}")
#
# def main():
#     client = mqtt.Client()
#     connect_mqtt(client)
#     client.loop_start()
#
#     while True:
#         for plc_id in range(1, 4):
#             data = generate_plc_data(plc_id)
#             client.publish(MQTT_TOPIC, json.dumps(data))
#             push_to_influxdb(data)
#             print(f"Published: {data}")
#             time.sleep(5)
#
# if __name__ == "__main__":
#     main()
