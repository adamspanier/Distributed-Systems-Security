import socket, hashlib, pickle, random, time, os, json
from datetime import datetime
from Blockchain import Blockchain
import traceback

CONFIG_FILE = "config.yml"
BC_FILE = "bc.json"

def main():
    data = get_server_config()
    run(data)

############# MAIN EFFORT HERE ############

def run(data):
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                connect(s, data)
                test = get_auto_data()
                s.sendall(pickle.dumps(test))
                try:
                    con_data = pickle.loads(s.recv(data["pickle"]))
                    print("\n\033[1mALERT:\033[0m RESPONSE RECIEVED")
                    print("\t\033[1mData Recieved:\033[0m " + str(con_data["data"]))
                    print("\t\033[1mVerify:\033[0m " + str(con_data["verify"]))
                    print("\t\033[1mResponse:\033[0m " + str(con_data["result"]))
                    print("\t\033[1mPattern:\033[0m " + str(con_data["pattern"]))
                except EOFError as e:
                    print("Client EOF")
            except ConnectionResetError as e:
                print("Reset Connection in Client")
            except BrokenPipeError as e:
                print("Borken Pipe Error")
            except BaseException as e:
                print(e)
                print("Traceback Info:")
                traceback.print_exc()
                print()
            time.sleep(0.05)

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
            elif "pickle" in line:
                config["pickle"] = int(line.split()[1].replace("\"", ""))
    return config

def get_auto_data():
    num = random.randint(0, 1)
    output = None
    output = get_add_data()
    if num == 1:
        output["verify"] = True
    return output

def load_from_file():
    b1 = None
    os.chdir("/tmp")
    if BC_FILE in os.listdir():
        with open(BC_FILE, 'r') as file:
            try:
                data = json.load(file)
                for key in data.keys():
                    node = data[key]
                    if bool(node['head']):
                        h = hashlib.sha256(node['data'].encode()).hexdigest()
                        if h == node['hash']:
                            b1 = Blockchain(node['time'], node['data'])
                    else:
                        last = b1.get_last()
                        last_hash = last.get_hash()
                        comb = last_hash + node['data']
                        new_hash = hashlib.sha256(comb.encode()).hexdigest()
                        if new_hash == node['hash'] and next_data == node['data']:
                            b1.add_node(node['time'], node['data'])
                        else:
                            print("tampered data")
                    next_data = node['next']
            except BaseException as e:
                    print("Empty json")
                    print(e)
    return b1

def gen_next_data():
    b1 = load_from_file()
    output = "Error"

    if b1 is None:
        output = "pressure:0.0"
    elif b1.get_length() == 1:
        val1 = float(b1.get_last().get_data().split(":")[1])
        val1 += 0.25
        output = "pressure:" + str(val1)
    elif b1.get_length() > 1:
        val1 = float(b1.get_last().get_data().split(":")[1])
        val2 = float(b1.get_second_last().get_data().split(":")[1])
        if val1 - val2 >= 0.0 and val1 < 1.0:
            val1 += 0.25
            output = "pressue:" + str(val1)
        elif val1 == 1.0:
            val1 -= 0.25
            output = "pressue:" + str(val1)
        elif val2 - val1 >= 0.0 and val1 > 0.0:
            val1 -= 0.25
            output = "pressue:" + str(val1)
        elif val1 == 0.0:
            val1 += 0.25
            output = "pressue:" + str(val1)
    return output

def get_time():
    return str(datetime.now())

def get_add_data():
    data = {}
    data["verify"] = False
    data["time"] = str(datetime.now())
    data["data"] = gen_next_data()
    data["hash"] = hashlib.sha256(data["data"].encode()).hexdigest()
    return data

if __name__ == '__main__':
    main()
