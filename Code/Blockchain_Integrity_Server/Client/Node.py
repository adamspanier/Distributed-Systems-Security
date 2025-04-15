import hashlib, random, time
from datetime import datetime

class Node:
    __time = None
    __data = None
    __hash = None
    __next = None
    __is_head = None

    def __init__(self, time=None, data=None, hash=None):
        self.set_time(time)
        self.set_data(data)
        self.set_hash(hash)
        self.set_next(None)
        self.set_head_false()

    # helpers
    def get_random_data(self):
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

    def get_next_data(self):
        output = "None"
        if self.get_next() != None and isinstance(self.get_next(), Node):
            output = self.__next.get_data()
        return output

    def set_head_false(self):
        self.__is_head = False

    # getters
    def get_time(self):
        return self.__time

    def get_data(self):
        return self.__data

    def get_hash(self):
        return self.__hash

    def get_next(self):
        return self.__next

    def get_is_head(self):
        return self.__is_head

    # setters
    def set_time(self, time):
        if time == None:
            self.__time = str(datetime.now())
        else:
            self.__time = time

    def set_data(self, data):
        if data == None:
            self.__data = self.get_random_data()
        else:
            self.__data = data

    def set_hash(self, hash):
        if hash == None:
            #if head, just hash of data
            self.__hash = hashlib.sha256(self.get_data().encode()).hexdigest()
        else:
            #if not head, has of prev hash + data
            comb = hash + self.get_data()
            self.__hash = hashlib.sha256(comb.encode()).hexdigest()

    def set_next(self, next):
        if isinstance(next, Node):
            self.__next = next

    def set_is_head(self):
        self.__is_head = True

    # to string
    def __str__(self):
        output = "Node:\v\tTime: " +str(self.get_time()) + "\n\tData: " \
            + str(self.get_data()) + "\n\tHash: " + str(self.get_hash()) \
            + "\n\tNext: " + str(self.get_next_data()) + "\n"
        return output
