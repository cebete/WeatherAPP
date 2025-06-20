import os
import requests
import json
import urllib3


# Set up file and folder paths
folderPath = os.path.join(os.getenv('LOCALAPPDATA'), "WeatherAPP")
filePath = os.path.join(folderPath, 'apikey.json')

# Create the folder if it doesn't exist
os.makedirs(folderPath, exist_ok=True)

def LoadData():
    if os.path.exists(filePath):
        with open(filePath, "r") as file:
            return json.load(file)
    return {"key": "", "unit": "metric"}

def SaveData(data):
    with open(filePath, "w") as file:
        json.dump(data, file, indent=4)

def PrintMenu():
    print("Welcome to WeatherAPP!")
    print("1) Check Weather")
    print("2) Set API key")
    print("3) Change Units")
    print("4) Exit")

def GetUnitDesignator(data):
    return "C" if data.get("unit") == "metric" else "F"

def CheckInternetConnection(target):
    http = urllib3.PoolManager(timeout=3.0)
    request = http.request('GET', target, preload_content=False)
    code = request.status
    request.release_conn()
    if code == 200:
        return True
    else:
        return False
    
def ChangeUnit(data):
    while True:
        print("1) Metric")
        print("2) Imperial")
        choice = input("> ")

        if choice == "1":
            data["unit"] = "metric"
            break
        elif choice == "2":
            data["unit"] = "imperial"
            break
        else:
            print("❌ Invalid choice. Try again.")

    SaveData(data)

def GetWeather(data):
    if not CheckInternetConnection("https://www.google.com"):
        print("No internet connection!")
        return

    city = input("Enter city name: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={data['key']}&units={data['unit']}"

    try:
        response = requests.get(url)
        json_data = response.json()
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return

    if str(json_data.get("cod")) != "200":
        message = json_data.get("message", "").lower()
        if "city not found" in message or "nothing to geocode" in message:
            print("❌ Invalid city name!")
        elif "invalid api key" in message:
            print("❌ Invalid API key!")
        elif not CheckInternetConnection(url):
            print("❌ API seems to be down.")
        else:
            print("❌ Unknown error occurred.")
        return

    # Display weather
    print(f"📍 Weather in {json_data['name']}")
    print(f"🌡️ Temperature: {round(json_data['main']['temp'])}°{GetUnitDesignator(data)}")
    print(f"🌥️  Description: {json_data['weather'][0]['description']}")
    print(f"💧 Humidity: {json_data['main']['humidity']}%")
    print(f"💨 Wind Speed: {json_data['wind']['speed']} m/s")

def SetAPIKey(data):
    apiKey = input("(openweathermap.org) API Key: ")
    data["key"] = apiKey
    SaveData(data)


def main():
    data = LoadData()

    while True:
        PrintMenu()
        choice = input("> ")

        if choice == "1":
            GetWeather(data)
        elif choice == "2":
            SetAPIKey(data)
        elif choice == "3":
            ChangeUnit(data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main() 