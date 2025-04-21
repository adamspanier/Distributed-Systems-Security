from Node import Node
from Blockchain import Blockchain
import random, time, json, os, hashlib
from datetime import datetime


LOG_SIMULATION_NUMBER = 500
BC_FILE = "bc.json"


def main():
    b1 = simulate()
    print(b1)

def simulate():
    b1 = None
    print("\n\033[1m ********* RUNNING SIMULATION **********\033[0m")
    for i in range(LOG_SIMULATION_NUMBER):
        print("\n\t\033[1mALERT:\033[0m LOG RECIEVED")
        log = generate_log()
        print("\t\t\033[1mTime:\033[0m\t" + str(log['time']))
        print("\t\t\033[1mData:\033[0m\t" + str(log['data'])[:28] + "...")

        #################################################
        # This is the bit we put in the server.
        # Need to copy: load_from_file, make_response, recieved_log
        #               write_to_file

        b1 = load_from_file() # Load the blockchain from file
        if log["verify"] == True:  # Check if it is a verification
            print("\t\t\033[1mStatus:\033[0m\tVerify: " + log["data"][:20] + "... --> " + str(b1.verify(log["data"])))
            good = b1.verify(log["data"])
            response = make_response(True, good, log["data"])
        else:
            b1 = recieved_log(b1, log)  # <<<< If add log, add to block
            added = write_to_file(b1) # Then we write back to file.
            response = make_response(False, added, log["data"])

        #################################################

        sleep_time = random.random()*3
        print("\t\t\033[1mSleep:\033[0m\t" + str(round(sleep_time, 3)) + " seconds")
        time.sleep(sleep_time)
    print("\n ********* ENDING SIMULATION **********\n")
    return b1

def make_response(verify, result, data):
    response = {"verify": verify, "data": data, "result": result}
    return response

def write_to_file(b1):
    print("\t\t\033[1mStatus:\033[0m\tWriting to file!")
    output = False
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
    if BC_FILE in os.listdir() and os.path.getsize(BC_FILE) != 0:
        with open(BC_FILE, 'r') as file:
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
    else:
        f = open(BC_FILE, "w")
        f.close()
    return b1


def generate_log():
    num = random.randint(0, 1)
    data = None
    b1 = load_from_file()
    if num == 1 and b1 != None:
        where_stop = random.randint(0, b1.get_length())
        count = 0
        cur = b1.get_head()
        if b1.get_length() > 1:
            while cur.get_next() != None:
                if count == where_stop-1:
                    d = cur.get_data()
                elif where_stop == 0:
                    d = cur.get_data()
                cur = cur.get_next()
                count += 1
        else:
            d = cur.get_data()
        data = {"verify": True, "time":get_time(), "data":d}
    else:
        d = get_random_data()
        data = {"verify": False, "time":get_time(), "data":d}
    return data

def recieved_log(b1, log):
    if b1 == None:
        b1 = Blockchain(log['time'], log['data'])
    else:
        b1.add_node(log['time'], log['data'])
    return b1

def make_random_blockchain(num_blocks, t, d):
    b1 = Blockchain(get_time(), get_random_data())
    for i in range(100):
        if i == 47:
            b1.add_node(t, d)
        else:
            b1.add_node(get_time(), get_random_data())
    return b1

def get_random_data():
    length = random.randint(150, 170)
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

def get_time():
    return str(datetime.now())

if __name__ == '__main__':
    main()
