import socket, pickle, time, os, hashlib, random, json
from datetime import datetime
from Blockchain import Blockchain

CONFIG_FILE = "config.yml"
BC_FILE = "bc.json"

def main():
    data = get_server_config()
    run(data)

############# MAIN EFFORT HERE ############

def run(data):
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            connection, address = init_server(s, data)
            with connection:
                # print("Connected to " + str(address))
                still_data = True
                while still_data:
                    try:
                        log = pickle.loads(connection.recv(data["pickle"]))
                        good = check_incoming_json(log)
                        print("\n\t\033[1mALERT:\033[0m LOG RECIEVED")
                        if good:
                            response = good_json_handler(log)
                        else:
                            response = bad_json_handler()
                        connection.sendall(pickle.dumps(response))
                    except EOFError as e:
                        still_data = False
                    except pickle.UnpicklingError as e:
                        print("Pickling Error")


########################## HELPERS #################################

def good_json_handler(log):
    response = None
    print("\t\t\033[1mTime:\033[0m\t" + str(log['time']))
    print("\t\t\033[1mData:\033[0m\t" + str(log['data'])[:28] + "...")
    b1 = load_from_file() # Load the blockchain from file
    if log["verify"] == True:  # Check if it is a verification
        print("\t\t\033[1mStatus:\033[0m\tVerify: " + log["data"][:20] + "... --> " + str(b1.verify(log["data"])))
        good = b1.verify(log["data"])
        response = make_response(True, good, log["data"])
    else:
        b1 = recieved_log(b1, log)  # <<<< If add log, add to block
        added = write_to_file(b1) # Then we write back to file.
        response = make_response(False, added, log["data"])
    return response

def bad_json_handler():
    correct_format = "JSON should have the following keys: verify:(bool), time(datetime): data(any string), hash(hash of the string)"
    print("\t\t\033[1mERROR:\033[0m\tBad JSON Format")
    print("\t\t\033[1mFIX:\033[0m\t" + correct_format)
    response = {"verify": False, "data": correct_format}
    return response

def check_incoming_json(incoming):
    output = False
    if incoming != None:
        check_add = ["verify", "time", "data", "hash"]
        check_verify = ["verify", "time", "data"]
        incoming_keys = list(incoming.keys())
        output = check_add == incoming_keys or check_verify == incoming_keys
    return output

def make_response(verify, result, data):
    response = {"verify": verify, "data": data, "result": result}
    return response

def write_to_file(b1):
    print("\t\t\033[1mStatus:\033[0m\tWriting to file!")
    output = False
    os.chdir("/tmp")
    try:
        b1_dict = b1.get_as_dict()
        with open(BC_FILE, 'w') as file:
            json.dump(b1_dict, file, indent=4)
        output = True
    except BaseException as e:
        ouput = False
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
    else:
        print("Overwriting!")
        f = open(BC_FILE, "w")
        f.close()
    return b1

def recieved_log(b1, log):
    if b1 == None:
        b1 = Blockchain(log['time'], log['data'])
    else:
        b1.add_node(log['time'], log['data'])
    return b1

def print_client_data(data):
    print("\n########### TRANSACTION REPORT ############\n")
    for key in data.keys():
        print("\tKey: " + str(key) + " --> Value: " + str(data[key]))
    print("\n############### END REPORT ################\n")
    # time.sleep(2)

def init_server(s, data):
    good = False
    connection = None
    address = None
    while not good:
        # print("Binding...")
        try:
            s.bind((data['server_ip'], data["server_port"]))
            s.listen()
            connection, address = s.accept()
            good = True
        except OSError as e:
            pass
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
            elif "pickle" in line:
                config["pickle"] = int(line.split()[1].replace("\"", ""))
    return config

# def write_data(data):
#     output = "\n########### TRANSACTION REPORT ############\n"
#     for key in data.keys():
#         output += "\tKey: " + str(key) + " --> Value: " + str(data[key])
#     output += "\n############### END REPORT ################\n"
#     print(os.getcwd())
#     with open("/tmp/chain.txt", "a") as f:
#         print("writing")
#         f.write(output)


if __name__ == '__main__':
    main()
