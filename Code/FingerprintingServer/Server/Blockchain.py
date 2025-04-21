from Node import Node
import hashlib

class Blockchain:
    __head = None

    def __init__(self, time=None, data=None):
        self.set_head(time, data)

    # helpers
    def get_head_data():
        output = "None"
        if self.get_head() != None and isinstance(self.get_head(), Node):
            output = self.__head.get_data()
        return output

    def add_node(self, time=None, data=None):
        cur = self.get_head()
        while cur.get_next() != None:
            cur = cur.get_next()
        if time == None and data == None:
            cur.set_next(Node(cur.get_hash()))
        else:
            cur.set_next(Node(time, data, cur.get_hash()))

    def verify(self, data):
        found = False
        next = self.get_head()
        prev_hash = next.get_hash()
        while not found and next.get_next() != None:
            if next.get_is_head():
                h = hashlib.sha256(data.encode()).hexdigest()
                if next.get_hash() == h:
                    found = True
                else:
                    next = next.get_next()
            else:
                prev_hash = next.get_hash()
                next = next.get_next()
                new_hash = hashlib.sha256((prev_hash + data).encode()).hexdigest()
                if next.get_hash() == new_hash:
                    found = True
        return found

    def get_as_dict(self):
        blockchain = {}
        id = 1
        cur = self.get_head()
        while cur != None:
            blockchain[str(id)] = {
                "time": cur.get_time(),
                "data": cur.get_data(),
                "hash": cur.get_hash(),
                "head": cur.get_is_head(),
                "next": cur.get_next_data()
            }
            id += 1
            cur = cur.get_next()
        return blockchain

    def get_last(self):
        cur = self.get_head()
        while cur.get_next() != None:
            cur = cur.get_next()
        return cur

    def get_second_last(self):
        cur = self.get_head()
        while cur.get_next().get_next() != None:
            cur = cur.get_next()
        return cur

    def get_length(self):
        count = 0
        cur = self.get_head()
        while cur.get_next() != None:
            count += 1
            cur = cur.get_next()
        return count


    # getters
    def get_head(self):
        return self.__head

    # setters
    def set_head(self, time, data):
        if time == None and data == None:
            self.__head = Node()
            self.__head.set_is_head()
        else:
            self.__head = Node(time, data)
            self.__head.set_is_head()

    # to string
    def __str__(self):
        num = 1
        next = self.get_head()
        output = " \033[1mHead Node:\033[0m " + next.get_data() \
            + " : " + str(next.get_time()) + "\n"
        while next.get_next() != None:

            next = next.get_next()
            output += "\n\t--> \033[1mNode " + str(num) + ":\033[0m " + next.get_data() \
                + " : " + str(next.get_time()) + "\n\t    Hash: " + str(next.get_hash()) + "\n"
            num += 1
        return output[:-7]
