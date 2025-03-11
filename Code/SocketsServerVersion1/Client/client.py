import socket, json, random, hashlib, time
from datetime import datetime



# MAX_BYTES = 65535
# SERVER_IP = "127.0.0.1"
# SERVER_PORT = 1065


def main():
    client()


def client():
    sock = init_client()
    # data = get_data()
    for i in range(50):
        data = get_auto_data()
        clear_data = encode_json(data)
        send(clear_data, sock)
        receive_reply(sock)
        time.sleep(1)


def send(clear_data, sock):
    config = get_server_config()
    print("\n########### SENDING DATA ############\n")
    print("DATA: " + json.loads(clear_data)["data"])
    sock.sendto(clear_data, (config["server_ip"], config["server_port"]))
    print('The OS assigned me the address {}'.format(sock.getsockname()))


def get_server_config():
    config = {}
    with open("config.yml", "r") as f:
        for line in f:
            if "server-ip" in line:
                config["server_ip"] = line.split()[1].replace("\"", "")
            elif "server-port" in line:
                config["server_port"] = int(line.split()[1].replace("\"", ""))
            elif "max-bytes" in line:
                config["max-bytes"] = int(line.split()[1].replace("\"", ""))
    return config


def receive_reply(sock):
    print("\n########### RECIEVING REPLY ############\n")
    try:
        data, address = sock.recvfrom(get_server_config()["max-bytes"]) # Danger!
        text = data.decode('ascii')
        print('The server {} replied {!r}'.format(address, text))
    except OSError as exc:
        print("Socket Recieve Error")
    print("\n########### END TRANSMISSION ############\n")


def encode_json(in_dict):
    dump = None
    try:
        dump = json.dumps(in_dict).encode('utf-8')
    except TypeError as exc:
        print("JSON Dumps Error")
    return dump


def init_client():
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except BaseException as e:
        print("Socket Initialization Error")
    return sock


def get_data():
    data = {}
    data['firstName'] = input("Enter first name: ");
    data['lastName'] = input("Enter last name: ")
    data['id'] = int(input("Enter ID: "))
    return data


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
