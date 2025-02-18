import random
from time import sleep


def gas_level_gauge():
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])


def gas_stations():
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ee's"])


def gas_level_alert():
    gas_level = gas_level_gauge()
    gas_station = gas_stations()

    # Define the messages based on gas level
    messages = {
        "Empty": "****WARNING - YOU ARE OUT OF GAS****\nCalling AAA...",
        "Low": f"Your gas tank is extremely low, checking GPS for the closest gas station...\n"
               f"The closest gas station is {gas_station}, which is {round(random.uniform(1, 25), 1)} miles away.",
        "Quarter Tank": f"Your gas tank is at a Quarter Tank, checking GPS for the closest gas station...\n"
                        f"The closest gas station is {gas_station}, which is {round(random.uniform(25.1, 50), 1)} miles away.",
        "Half Tank": "Your gas tank is at Half Tank, which is enough to get to your destination!",
        "Three Quarter Tank": "Your gas tank is Three Quarter full!",
        "Full Tank": "Your gas tank is full, have a nice drive!"
    }

    # Print the corresponding message
    print("\n**************************\n")
    print("Gasoline Branch - Developer: Corbin Hanson\n")
    sleep(1.25)
    print(messages[gas_level])


# Run the function
gas_level_alert()

