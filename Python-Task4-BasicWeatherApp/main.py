import os

import requests


API_URL = "https://api.openweathermap.org/data/2.5/weather"


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def get_weather(city, api_key):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        if response.status_code == 401:
            print("Error: Invalid API key.")
            return None
        if response.status_code == 404:
            print("Error: City not found.")
            return None

        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("Error: The weather request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the weather service.")
    except requests.exceptions.RequestException as error:
        print(f"Error: Unable to fetch weather data ({error}).")

    return None


def display_weather(data):
    temperature_c = data["main"]["temp"]
    temperature_f = celsius_to_fahrenheit(temperature_c)
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
    city_name = data["name"]
    country = data["sys"]["country"]

    print("\n" + "=" * 35)
    print(f"Weather for {city_name}, {country}")
    print("=" * 35)
    print(f"Temperature: {temperature_c:.1f} °C")
    print(f"Temperature: {temperature_f:.1f} °F")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description.title()}")
    print(f"Wind speed: {wind_speed} m/s")


def main():
    print("=" * 35)
    print("       BASIC WEATHER APP")
    print("=" * 35)

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Error: OPENWEATHER_API_KEY is not set.")
        return

    while True:
        city = input("\nEnter a city name (or type 'exit'): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break
        if not city:
            print("Error: City name cannot be empty.")
            continue

        weather_data = get_weather(city, api_key)
        if weather_data is not None:
            display_weather(weather_data)


if __name__ == "__main__":
    main()
