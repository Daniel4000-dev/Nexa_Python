import sys;
import requests;
from dotenv import load_dotenv;
import os;

load_dotenv()

# OpenWeather API key
API_KEY = os.getenv('API_KEY')

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        condition = data['weather'][0]['description']
        humidity = data['main']['humidity']
        print(f"Weather in {city}: Temperature: {temperature}°C Condition: {condition.capitalize()} Humidity: {humidity}%")
    else:
        error_message = response.json().get("message", "Unknown error")
        print(f"Error fetching data for {city}: {error_message}")
        
def main():
    # Allow users to enter multiple city names with their command line
    cities = sys.argv[1:]
    if not cities:
        city = input("Enter a city: ")
        cities = [city]
        
    for city in cities:
        fetch_weather(city)
        
if __name__ == "__main__":
    main()