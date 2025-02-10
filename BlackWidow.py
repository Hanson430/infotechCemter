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
    
vehicleReponseSystem()