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

print(weather())