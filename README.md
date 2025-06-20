# 🌦️ WeatherAPP – Python CLI Weather App

**WeatherAPP** is a simple, lightweight Python command-line application that fetches real-time weather data for any city using the [OpenWeatherMap API](https://openweathermap.org/api). It supports both metric and imperial units, stores your API key and preferences locally, and handles errors gracefully.

---

## 🚀 Features

- 📡 Real-time weather for any city  
- 🌡️ Metric (°C) and Imperial (°F) unit switching  
- 🔐 API key and preferences saved locally  
- ❌ Handles common errors (invalid city, no internet, invalid API key)  
- 🖥️ Easy to use CLI interface  

---

## 📸 Sample Output

```
📍 Weather in London  
🌡️ Temperature: 22°C  
🌥️  Description: scattered clouds  
💧 Humidity: 60%  
💨 Wind Speed: 5.2 m/s  
```

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/WeatherAPP.git
cd WeatherAPP
```

### 2. Install dependencies
```bash
pip install requests urllib3
```

---

## 🔧 Setup & Usage

### Run the app
```bash
python weatherapp.py
```

### Menu Options
- `1) Check Weather` – Enter a city to get current weather data  
- `2) Set API key` – Input your OpenWeatherMap API key  
- `3) Change Units` – Switch between °C and °F  
- `4) Exit` – Close the app  

### Data Storage
Your API key and preferred units are stored in:
```
%LOCALAPPDATA%\WeatherAPP\apikey.json
```

---

## 🧠 How It Works

1. Prompts the user for a city name  
2. Sends a request to OpenWeatherMap's API using your API key and preferred unit  
3. Parses and displays weather info in a clean format  
4. Saves your API key and settings locally for future use  

---

## 🛡 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
Feel free to fork this repo and submit improvements or fixes.

---

## 📫 Contact

Questions? Feedback? [Open an issue](https://github.com/cebete/WeatherAPP/issues).
