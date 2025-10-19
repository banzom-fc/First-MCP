import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="weather-mcp",
)

@mcp.tool(name="get_weather", description="Get the current weather for a given city")
async def get_weather(city: str) -> str:
    """
    Get the current weather for a given city.
    Args:
        city (str): The name of the city to get the weather for.
    Returns:
        str: A string containing the current weather data for the city.
    Example:
        get_weather("New York")
    Example response:
        Weather in New York from wttr.in: New York: 🌦️  +22°C
    """
    return fetch_weather_wttr(city)

def fetch_weather_metaweather(city: str) -> str:
    """
    Fetch the current weather for a given city using MetaWeather API (no API key required).
    Args:
        city (str): The name of the city to get the weather for.
    Returns:
        str: Weather description or error message.
    """
    try:
        # Step 1: Get WOEID for the city
        search_url = f"https://www.metaweather.com/api/location/search/?query={city}"
        search_resp = requests.get(search_url, timeout=5)
        search_resp.raise_for_status()
        locations = search_resp.json()
        if not locations:
            return f"City '{city}' not found in MetaWeather."
        woeid = locations[0]['woeid']
        # Step 2: Get weather by WOEID
        weather_url = f"https://www.metaweather.com/api/location/{woeid}/"
        weather_resp = requests.get(weather_url, timeout=5)
        weather_resp.raise_for_status()
        weather_data = weather_resp.json()
        today = weather_data['consolidated_weather'][0]
        weather = today['weather_state_name']
        temp = round(today['the_temp'], 1)
        return f"Weather in {city}: {weather}, {temp}°C (MetaWeather)"
    except Exception as e:
        return f"Error fetching weather from MetaWeather: {e}"
    
def fetch_weather_wttr(city: str) -> str:
    """
    Fetch the current weather for a given city using wttr.in (no API key required).
    Args:
        city (str): The name of the city to get the weather for.
    Returns:
        str: Weather description or error message.
    """
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5, verify=False)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"Error fetching weather from wttr.in: {e}"

@mcp.tool(name="get_weather_wttr", description="Get the current weather for a given city using wttr.in (no API key required)")
async def get_weather_wttr(city: str) -> str:
    return fetch_weather_wttr(city)

def test_get_weather():
    """
    Test the get_weather function with a sample city.
    """
    city = "New York"
    result = fetch_weather_metaweather(city)
    print(f"Weather in {city}: {result}")

def test_get_weather_wttr():
    """
    Test the get_weather_wttr function with a sample city.
    """
    city = "New York"
    result = fetch_weather_wttr(city)
    print(f"Weather in {city} from wttr.in: {result}")

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

# Uncomment the following lines to run tests
# test_get_weather()
# test_get_weather_wttr()