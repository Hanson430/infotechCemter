<<<<<<< HEAD
print("\n*************************************\n")
=======
import random  # Used for generating random weather conditions
>>>>>>> 931fc04 (ChatGPT - Efficient Code - Stable)

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

# Main execution
print("\n*************************************\n")
print("Weather Branch - Developer: Corbin Hanson")

weather_alert = weather()  # Generate a random weather condition
vehicle_response_system(weather_alert)  # Pass the weather condition to the function

<<<<<<< HEAD
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
=======
>>>>>>> 931fc04 (ChatGPT - Efficient Code - Stable)
