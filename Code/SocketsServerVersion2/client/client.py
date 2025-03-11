import socket, hashlib, pickle, random
from datetime import datetime

CONFIG_FILE = "config.yml"
LOG_FILE = "logs.csv"

def main():
    data = get_server_config()
    run(data)

############# MAIN EFFORT HERE ############

def run(data):
    for i in range(10):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                connect(s, data)
                test = get_auto_data()
                s.sendall(pickle.dumps(test))
                try:
                    con_data = pickle.loads(s.recv(256))
                    print("Data: " + str(con_data["data"]))
                except EOFError as e:
                    print("Client EOF")
            except ConnectionResetError as e:
                print("Reset Connection in Client")
            except BrokenPipeError as e:
                print("Borken Pipe Error")

############################################

def connect(s, data):
    try:
        s.connect((data["server_name"], data["server_port"]))
    except ConnectionResetError as e:
        print("Reset Connection")

def get_server_config():
    config = {}
    with open(CONFIG_FILE, "r") as f:
        for line in f:
            if "server-ip" in line:
                config["server_ip"] = line.split()[1].replace("\"", "")
            elif "server-port" in line:
                config["server_port"] = int(line.split()[1].replace("\"", ""))
            elif "max-bytes" in line:
                config["max-bytes"] = int(line.split()[1].replace("\"", ""))
            elif "server-name" in line:
                config["server_name"] = line.split()[1].replace("\"", "")
            elif "client-name" in line:
                config["client_name"] = line.split()[1].replace("\"", "")
    return config

def get_auto_data():
    data = {}
    data["time"] = str(datetime.now())
    data["ages"] = str(random.randint(2, 90))
    data["data"] = get_random_data()
    data["hash"] = hashlib.sha256(data["data"].encode()).hexdigest()
    return data


def get_random_data():
    length = random.randint(10, 20)
    output = ""
    for i in range(length):
        chooser = random.randint(0, 2)
        if chooser == 0:
            output += chr(random.randint(97, 122))
        elif chooser == 1:
            output += chr(random.randint(65, 90))
        elif chooser == 2:
            output += chr(random.randint(35, 38))
    return output

if __name__ == '__main__':
    main()
