print("\n*************************************\n")

print("Weather Branch - Developer: Corbin Hanson\n")

#Import Libraries Here!
import  random
from time import sleep

#Weather Function to determine the weather
def weather ():
    weatherForecastList = ["snowing", "blizzard", "icy", "raining", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

weatherAlert = weather()

def vehicleReponseSystem():
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because "
            "it is", weatherAlert, "outside.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because "
            "it is a", weatherAlert, "outside!")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated your alarm by 90 minutes because "
            "it is ", weatherAlert, "outside!")
    elif weatherAlert == "raining":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because "
            "it is ", weatherAlert, "outside.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated your alarm by 0 minutes because "
            "it is ", weatherAlert, "outside.")
    else:
        print("\nThe National Weather Service is calling for", weatherAlert, "skies outside, drive safe!")

vehicleReponseSystem()