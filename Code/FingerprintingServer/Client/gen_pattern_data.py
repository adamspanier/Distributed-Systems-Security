import random as rand
import math


SEED_VAL = 42
DATA = []

def main():
    for i in range(30):
        gen_next_data()
    for i in range((len(DATA))):
        print(DATA[i])


def gen_next_data():
    if len(DATA) == 0:
        DATA.append("pressure:0.0")
    elif len(DATA) == 1:
        val1 = float(DATA[len(DATA)-1].split(":")[1])
        val1 += 0.25
        DATA.append("pressure:" + str(val1))
    else:
        val1 = float(DATA[len(DATA)-1].split(":")[1])
        val2 = float(DATA[len(DATA)-2].split(":")[1])
        if val1 - val2 >= 0.0 and val1 < 1.0:
            val1 += 0.25
            DATA.append("pressue:" + str(val1))
        elif val1 == 1.0:
            val1 -= 0.25
            DATA.append("pressue:" + str(val1))
        elif val2 - val1 >= 0.0 and val1 > 0.0:
            val1 -= 0.25
            DATA.append("pressue:" + str(val1))
        elif val1 == 0.0:
            val1 += 0.25
            DATA.append("pressue:" + str(val1))

if __name__ == '__main__':
    main()
