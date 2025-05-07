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

def test_fingerprinting_invalid_pattern():
    print("Testing invalid fingerprinting pattern...")
    bad_pattern_sequence = [0.25, 0.5, 0.9, 1.0, 1.2, 0.75, 0.6]
    results = []

    for val in bad_pattern_sequence:
        payload = build_pressure_json(val, verify=True)
        response = send_json_to_server(FINGERPRINT_HOST, FINGERPRINT_PORT, payload)
        results.append((payload, response))
        time.sleep(0.5)

    return results

if __name__ == "__main__":
    print("Running ICS test suite...")

    blockchain_add = test_blockchain_add()
    blockchain_verify = test_blockchain_verify(blockchain_add)

    fingerprinting_valid = test_fingerprinting_valid_pattern()
    fingerprinting_invalid = test_fingerprinting_invalid_pattern()

    print("\nRESULTS:\n")
    pprint.pprint({
        "blockchain_add": blockchain_add,
        "blockchain_verify": blockchain_verify,
        "fingerprinting_valid": fingerprinting_valid,
        "fingerprinting_invalid": fingerprinting_invalid
    })

# Save to timestamped log file
log_filename = f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
with open(log_filename, "w") as f:
    f.write("\nRESULTS (Logged):\n")
    pprint.pprint({
        "blockchain_add": blockchain_add,
        "blockchain_verify": blockchain_verify,
        "fingerprinting_valid": fingerprinting_valid,
        "fingerprinting_invalid": fingerprinting_invalid
    }, stream=f)
print(f"Results also saved to {log_filename}")
