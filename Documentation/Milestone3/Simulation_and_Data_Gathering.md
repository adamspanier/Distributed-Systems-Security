# Simulation and Data Gathering

## Unencrypted Environment
```python
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
INFLUXDB_TOKEN = "TOEKN_OMITTED"  # InfluxDB token
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
# This is a partial copy of the script. The full script can be found at <script location>.
```
## Encrypted Environment
```python
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
INFLUXDB_TOKEN = "TOKEN_OMITTED"  # InfluxDB token
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
# This is a partial copy of the script. The full script can be found at <script location>.
```

## Blockchain/Fingerprinting Environment
```python
import socket
import pickle
from datetime import datetime
import time
import random
import string
import pprint

BLOCKCHAIN_HOST = "blockchain-dsc"
BLOCKCHAIN_PORT = 1065

FINGERPRINT_HOST = "fingerprinting-dsc"
FINGERPRINT_PORT = 1066

def send_json_to_server(host, port, json_data):
    with socket.create_connection((host, port), timeout=5) as sock:
        sock.sendall(pickle.dumps(json_data))
        response = sock.recv(4096)
        return pickle.loads(response)

# --- Blockchain ---
def random_string(length=50):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def test_blockchain_add():
    print("Sending blockchain add test data...")
    results = []
    for _ in range(5):
        data = random_string()
        timestamp = datetime.now().isoformat()
        test_json = {'verify': False, 'time': timestamp, 'data': data}
        response = send_json_to_server(BLOCKCHAIN_HOST, BLOCKCHAIN_PORT, test_json)
        results.append((test_json, response))
        time.sleep(0.5)
    return results

def test_blockchain_verify(added_entries):
    print("Verifying blockchain entries...")
    results = []
    for entry, _ in added_entries:
        entry['verify'] = True
        entry['time'] = datetime.now().isoformat()
        response = send_json_to_server(BLOCKCHAIN_HOST, BLOCKCHAIN_PORT, entry)
        results.append((entry, response))
        time.sleep(0.5)
    return results

# --- Fingerprinting ---
def build_pressure_json(pressure_value, verify=False):
    return {
        'verify': verify,
        'time': datetime.now().isoformat(),
        'data': f'pressue:{pressure_value}'
    }

def test_fingerprinting_valid_pattern():
    print("Testing valid fingerprinting pattern...")
    pattern_sequence = [0.25, 0.5, 0.75, 1.0, 0.75, 0.5, 0.25, 0.0, 0.25, 0.5]
    results = []

    for i, val in enumerate(pattern_sequence):
        verify = (i % 2 != 0)
        payload = build_pressure_json(val, verify=verify)
        response = send_json_to_server(FINGERPRINT_HOST, FINGERPRINT_PORT, payload)
        results.append((payload, response))
        time.sleep(0.5)

    return results
```
