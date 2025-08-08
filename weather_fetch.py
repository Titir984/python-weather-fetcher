import requests

def get_weather(city):
    API_KEY = "https://wttr.in/"  # Using wttr.in free API (no signup needed)
    try:
        url = f"{API_KEY}{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            print("Weather Info:", response.text)
        else:
            print("Error: Could not fetch weather data.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
