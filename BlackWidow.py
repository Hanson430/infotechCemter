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


print(gasLevelGauge())
print(gasStaions())