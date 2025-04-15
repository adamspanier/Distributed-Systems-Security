import socket, hashlib, pickle, random, time, os, json
from datetime import datetime
from Blockchain import Blockchain

CONFIG_FILE = "config.yml"
BC_FILE = "bc.json"

def main():
    data = get_server_config()
    run(data)

############# MAIN EFFORT HERE ############

def run(data):
    # for i in range(10):
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
                except EOFError as e:
                    print("Client EOF")
            except ConnectionResetError as e:
                print("Reset Connection in Client")
            except BrokenPipeError as e:
                print("Borken Pipe Error")
            except BaseException as e:
                pass
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

# just get it to run without verify, then add verification
def get_auto_data():
    num = random.randint(0, 1)
    output = None
    if num == 0:
        output = get_add_data()
    else:
        output = get_verify_data()
    return output

# Not working
def get_verify_data():
    b1 = load_from_file()
    data = None
    d = None
    try:
        if b1 != None:
            where_stop = random.randint(0, b1.get_length())
            count = 0
            cur = b1.get_head()
            if b1.get_length() > 1:
                while cur.get_next() != None:
                    if count == where_stop-1:
                        d = cur.get_data()
                        break
                    elif where_stop == 0:
                        d = cur.get_data()
                    cur = cur.get_next()
                    count += 1
            else:
                d = cur.get_data()
            data = {"verify": True, "time":get_time(), "data":d}
    except BaseException as e:
        print(e)
    return data

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

def get_time():
    return str(datetime.now())

def get_add_data():
    output = None
    data = {}
    data["verify"] = False
    data["time"] = str(datetime.now())
    data["data"] = get_random_data()
    data["hash"] = hashlib.sha256(data["data"].encode()).hexdigest()
    bad_data = {"response": False}
    num = random.randint(0, 100)
    if num % 2 == 0:
        output = bad_data
    else:
        output = data
    return output

def get_random_data():
    length = random.randint(50, 60)
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
