print("\n*************************************\n")

print("Weather Branch - Developer: Corbin Hanson")

#Import Libraries Here!
import  random # Used for generating random weather conditions
from time import sleep # Imported butnot used in the code

#Weather Function to determine the weather
def weather ():
    weatherForecastList = ["snowing", "blizzard", "icy", "raining", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition
#Generate a random weather condtition
weatherAlert = weather()
#repsonse based on weather condition
def vehicleReponseSystem():
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because "
            "it is", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 55MPH.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because "
            "it is a", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 45MPH.")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated your alarm by 90 minutes because "
            "it is ", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 35MPH.")
    elif weatherAlert == "raining":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because "
            "it is ", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 65MPH.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated your alarm by 0 minutes because "
            "it is ", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 70MPH.")
    else:
        print("\nThe National Weather Service is calling for", weatherAlert, "skies outside.")
        sleep(1)
        print("VRS has been disengaged, drive safe!")
#execute the code based on the condition
vehicleReponseSystem()