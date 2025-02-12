import random  # Used for generating random weather conditions

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

