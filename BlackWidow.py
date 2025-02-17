print("\n**************************\n")
print("Gasoline Branch - Developer: Corbin Hanson\n")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStaions():
    gasStaionsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ee's"]
    return random.choice(gasStaionsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25), 1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50), 1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("****WARNING - YOU ARE OUT OF GAS****\n")
        sleep(1.25)
        print("Calling AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremly low, checking GPS for the closest gas station\n")
        sleep(1.25)
        print("The closest gas station is", gasStaions(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a Quarter Tank, checking GPS for the closest gas station.")
        sleep(1.25)
        print("The closest gas station is", gasStaions(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is on a Half of a Tank which is enough to get to your destination!")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is Three Quarter of a Tank full!")
    else:
        print("Your gas tank is full, have a nice drive!")

gasLevelAlert()
