import socket, json
from datetime import datetime


CONFIG_FILE = "config.yml"
LOG_FILE = "logs.csv"


def main():
    server()


def server():
    sock = init_server()
    run(sock)


def run(sock):
    while True:
        text, data, address = get_data_and_address(sock)
        print_client_data(address, text)
        log_data(address, text)
        reply(sock, data, address)


def log_data(address, text):
    data = json.loads(text)
    record = str(datetime.now()) + ","
    for key in data.keys():
        record += str(data[key]) + ","
    record = record[:-1] + "\n"
    with open(LOG_FILE, "a") as f:
        f.write(record)


def reply(sock, data, address):
    text = 'Your data was {} bytes long'.format(len(data))
    data = text.encode('ascii')
    sock.sendto(data, address)


def print_client_data(address, text):
    print("\n########### TRANSACTION REPORT ############\n")
    ip, port = parse_address(address)
    print("The client at " + str(ip) + ":" + str(port) + " sent:\n")
    data_dict = json.loads(text)
    for key in data_dict.keys():
        print("\tKey: " + str(key) + " --> Value: " + str(data_dict[key]))
    print("\n############### END REPORT ################\n")


def parse_address(address):
    ip = None
    port = None
    try:
        ip = address[0]
        port = address[1]
    except IndexError as e:
        print("Index error in address parser")
    return ip, port


def get_data_and_address(sock):
    text = None
    address = None
    try:
        data, address = sock.recvfrom(get_server_config()["max-bytes"])
        text = data.decode('ascii')
    except OSError as e:
        print("Server Recieve Error")
    return text, data, address


def init_server():
    sock = None
    config = get_server_config()
    try:
        print("\n########### SERVER BOOT ############\n")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((config["server_ip"], config["server_port"]))
        print('Listening at {}'.format(sock.getsockname()))
    except OSError as e:
        print("Server Socket Creation Error")
    return sock


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
    return config

if __name__ == '__main__':
    main()
