#!/usr/bin/env python3
"""
Weather API Script for CoPaw Weather Skill

This script queries OpenWeatherMap API for current weather information.

Usage:
    python weather_api.py --city "Beijing"
    python weather_api.py --city "New York"

Environment Variables:
    WEATHER_API_KEY: Your OpenWeatherMap API key (required)

API Documentation:
    https://openweathermap.org/current
"""
import argparse
import json
import os
import sys

try:
    import requests
except ImportError:
    print("Error: requests library not installed")
    print("Install with: pip install requests")
    sys.exit(1)


def get_weather(city: str, api_key: str) -> dict:
    """
    Query OpenWeatherMap API for weather data.

    Args:
        city: City name (e.g., "Beijing", "New York")
        api_key: OpenWeatherMap API key

    Returns:
        Weather data dictionary

    Raises:
        requests.HTTPError: If API request fails
    """
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Celsius
        "lang": "zh_cn"     # Chinese descriptions
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def format_weather_output(data: dict) -> str:
    """
    Format weather data for display.

    Args:
        data: Weather data from API

    Returns:
        Formatted weather string
    """
    city = data["name"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    output = f"""City: {city}
Temperature: {temp}°C (feels like {feels_like}°C)
Weather: {description}
Humidity: {humidity}%
Wind Speed: {wind_speed} m/s"""

    return output


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Query weather information for a city"
    )
    parser.add_argument(
        "--city",
        required=True,
        help="City name (e.g., 'Beijing', 'New York')"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output in JSON format"
    )
    args = parser.parse_args()

    # Get API key from environment
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        print("Error: WEATHER_API_KEY environment variable not set")
        print("\nTo fix this:")
        print("1. Get a free API key from https://openweathermap.org/api")
        print("2. Set the environment variable:")
        print("   export WEATHER_API_KEY='your-api-key-here'")
        return 1

    try:
        # Query weather data
        data = get_weather(args.city, api_key)

        # Output results
        if args.json:
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(format_weather_output(data))

        return 0

    except requests.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Error: City '{args.city}' not found")
            print("Please check the city name and try again")
        elif e.response.status_code == 401:
            print("Error: Invalid API key")
            print("Please check your WEATHER_API_KEY")
        else:
            print(f"Error: API request failed: {e}")
        return 1

    except requests.Timeout:
        print("Error: Request timed out")
        print("Please check your network connection")
        return 1

    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
