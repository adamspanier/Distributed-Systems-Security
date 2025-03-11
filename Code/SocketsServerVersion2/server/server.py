import socket, pickle, time

CONFIG_FILE = "config.yml"
LOG_FILE = "logs.csv"

def main():
    data = get_server_config()
    run(data)

############# MAIN EFFORT HERE ############

def run(data):
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            connection, address = init_server(s, data)
            with connection:
                print("Connected to " + str(address))
                still_data = True
                while still_data:
                    try:
                        con_data = pickle.loads(connection.recv(256))
                        print_client_data(con_data)
                        connection.sendall(pickle.dumps(con_data))
                    except EOFError as e:
                        still_data = False

############################################

def print_client_data(data):
    print("\n########### TRANSACTION REPORT ############\n")
    for key in data.keys():
        print("\tKey: " + str(key) + " --> Value: " + str(data[key]))
    print("\n############### END REPORT ################\n")


def init_server(s, data):
    s.bind((data['server_ip'], data["server_port"]))
    s.listen()
    connection, address = s.accept()
    return connection, address


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


if __name__ == '__main__':
    main()
