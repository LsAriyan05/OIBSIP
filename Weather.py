import requests

print("Simple Weather App")
print("-------------------")

try:
    city = input("Enter your city name: ").strip()

    if not city:
        print("Please enter a valid city name.")
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={"e5d55721b91fe21c76e14e8d5c7e93e9"}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            weather = data['weather'][0]['description']

            print()
            print(f"Weather in {city}: {weather}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
        else:
            print("City not found or API error occurred.")
except requests.exceptions.ConnectionError:
    print("Network problem. Please check your internet connection.")
except Exception as e:
    print("Something went wrong:", e)
