# Importing necessary libraries
import sys  # provides access to system-specific parameters and functions
import time  # Allows for time-related functions like delays 
import random  # Used for generating random weather conditions

# ANSI escape sequences for color
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color back to default

# Adding color to the initial welcome messages
print(f"\n{CYAN}Welcome Branch - Developer: Corbin Hanson{RESET}")

print(f"\n{GREEN}Welcome to InfoTech Center V1.0{RESET}\n")

x = 0
ellipsis = 0

# Loop to simulate a system booting animation
while x != 20:
    x += 1  # increment counter

    # Creates loading message with increasing dots
    message = f"{YELLOW}Infotech Center System Booting{RESET}" + "." * ellipsis  

    ellipsis += 1  # Increase ellipsis count

    # Overwrites the current line in the terminal
    sys.stdout.write("\r" + message)

    time.sleep(.5)  # pause for half a second to have an effect

    # Reset ellipsis after reaching 3 dots to loop back
    if ellipsis == 4:
        ellipsis = 0

# When the loop completes, it has a final message
if x == 20:
    print(f"\n\n{RED}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")


# Main execution
print("\n*************************************\n")
print("Weather Branch - Developer: Corbin Hanson")

# Weather function to determine the weather
def weather():
    weather_forecast_list = ["snowing", "blizzard", "icy", "raining", "windy", "sunny"]
    return random.choice(weather_forecast_list)


# Vehicle response function
def vehicle_response_system(weather_alert):
    # Weather condition to alarm time and speed mapping
    weather_info = {
        "snowing": (30, 55),
        "blizzard": (60, 45),
        "icy": (90, 35),
        "raining": (60, 65),
        "windy": (0, 70),
        "sunny": (0, 0)
    }

    # Get the minutes and speed from the dictionary, default to 0 minutes and 0 speed if not found
    minutes, speed = weather_info.get(weather_alert, (0, 0))

    if minutes > 0:
        print(f"\nThe National Weather Service has updated your alarm by {minutes} minutes because it is {weather_alert} outside.")
        print(f"VRS has been engaged only allowing us to drive {speed}MPH.")
    else:
        print(f"\nThe National Weather Service is calling for {weather_alert} skies outside.")
        print("VRS has been disengaged, drive safe!")



weather_alert = weather()  # Generate a random weather condition
vehicle_response_system(weather_alert)  # Pass the weather condition to the function

