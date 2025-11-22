import tkinter as tk
import requests
from PIL import Image, ImageTk
from dotenv import load_dotenv
import os

load_dotenv()

# OpenWeatherMap API configuration
baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
city = ""
colour = "#7af5f5"

root = tk.Tk()
root.geometry("800x600")
root.title("Weather App")

searchFrame = tk.Frame(root)
searchVar = tk.StringVar()


def fetch_weather():
    appId = os.getenv("WEATHER_API_KEY")

    if not appId:
        print("API Key not found. Please set the API_KEY environment variable.")
        return
    
    city = searchVar.get()
    completeUrl = baseUrl + "appid=" + appId + "&q=" + city + "&units=metric"

    response = requests.get(completeUrl)
    weather_data = response.json()


    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']
    city = weather_data['name']

    tempLabel.config(text=f"Temperature: {temperature} °C")
    humidityLabel.config(text=f"Humidity: {humidity} %")
    pressureLabel.config(text=f"Pressure: {pressure} hPa")
    minTempLabel.config(text=f"Min Temp: {temp_min} °C")
    maxTempLabel.config(text=f"Max Temp: {temp_max} °C")
    currentWeatherLabel.config(text=city)


#Add Search Box
cityText = tk.Label(searchFrame, text= "City:", bg=colour, font=("Helvetica", 16))
search_entry = tk.Entry(searchFrame, textvariable=searchVar, font=("Helvetica", 16))
search_Button = tk.Button(searchFrame, text="Search", command=fetch_weather,  font=("Helvetica", 16))
searchFrame.configure(bg=colour)

cityText.grid(row=0, column=0)
search_entry.grid(row=0, column=1)
search_Button.grid(row=0, column=2, padx=10)

searchFrame.place(relx=0.5, rely=0.1, anchor="center")


#Add current weather information
currentWeatherLabel = tk.Label(root, text="", font=("Helvetica", 16), bg=colour)
currentWeatherLabel.place(relx=0.5, rely=0.3, anchor="center")

# Resizing our weather icon
weatherIcon = Image.open("img/weather.png")
weatherResized = weatherIcon.resize((100, 100))
weatherImage = ImageTk.PhotoImage(weatherResized)


# Main weather widget
weatherLabel = tk.Label(root, image=weatherImage, bg=colour)
weatherLabel.place(relx=0.5, rely=0.4, anchor="center")

tempLabel = tk.Label(root, text="Temperature: °C", font=("Helvetica", 20), bg=colour)
tempLabel.place(relx=0.5, rely=0.52, anchor="center")

separator = tk.Frame(root, bg="black", height=2, width=300)
separator.place(relx=0.5, rely=0.57, anchor="center")

# Pressure
pressureLabel = tk.Label(root, text="Pressure: hPa", font=("Helvetica", 12), bg=colour)
pressureLabel.place(relx=0.2, rely=0.65, anchor="center")

# Humidity
humidityLabel = tk.Label(root, text="Humidity: %", font=("Helvetica", 12), bg=colour)
humidityLabel.place(relx=0.4, rely=0.65, anchor="center")

# Max Temp
maxTempLabel = tk.Label(root, text="Max Temp: °C", font=("Helvetica", 12), bg=colour)
maxTempLabel.place(relx=0.6, rely=0.65, anchor="center")

# Min Temp
minTempLabel = tk.Label(root, text="Min Temp: °C", font=("Helvetica", 12), bg=colour)
minTempLabel.place(relx=0.8, rely=0.65, anchor="center")
#---------------------------------------------------#



root.configure(bg="#7af5f5")
root.mainloop()








