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
    city = weather_data['name']

    tempLabel.config(text=f"Temperature: {temperature} °C")
    humidityLabel.config(text=f"Humidity: {humidity} %")
    pressureLabel.config(text=f"Pressure: {pressure} hPa")
    currentWeatherLabel.config(text=f"Current Weather: {city}")
#---------------------------------------------------#
#Add Search Box
cityText = tk.Label(searchFrame, text= "City:", bg=colour, font=("Helvetica", 16))
search_entry = tk.Entry(searchFrame, textvariable=searchVar, font=("Helvetica", 16))
search_Button = tk.Button(searchFrame, text="Search", command=fetch_weather,  font=("Helvetica", 16))
searchFrame.configure(bg=colour)

cityText.grid(row=0, column=0)
search_entry.grid(row=0, column=1)
search_Button.grid(row=0, column=2, padx=10)

searchFrame.grid(row=0, column=1, padx=20, pady=20)
#---------------------------------------------------#
#Add current weather information
currentWeatherLabel = tk.Label(root, text="Current Weather: ", font=("Helvetica", 16), bg=colour)
currentWeatherLabel.grid(row=0, column=2, padx=80, pady=20)

### Add Weather Details
weatherIcon = Image.open("img/weather.png")
weatherResized = weatherIcon.resize((100, 100))
weatherImage = ImageTk.PhotoImage(weatherResized)


weatherLabel = tk.Label(root, image=weatherImage, bg=colour)
weatherLabel.place(relx=0.5, rely=0.4, anchor="center")

tempLabel = tk.Label(root, text="Temperature: °C", font=("Helvetica", 20), bg=colour)
tempLabel.place(relx=0.5, rely=0.52, anchor="center")
#---------------------------------------------------#
# Add Humidity Details
humidityIcon = Image.open("img/humidity.png")
humidityResized = humidityIcon.resize((50, 50))
humidityImage = ImageTk.PhotoImage(humidityResized)
humidityLabelIcon = tk.Label(root, image=humidityImage, bg=colour)
humidityLabelIcon.place(relx=0.25, rely=0.6, anchor="center")

humidityLabel = tk.Label(root, text="Humidity: %", font=("Helvetica", 20), bg=colour)
humidityLabel.place(relx=0.25, rely=0.7, anchor="center")
#---------------------------------------------------#
#Add pressure Details
pressureIcon = Image.open("img/pressure.png")
pressureResized = pressureIcon.resize((50, 50))
pressureImage = ImageTk.PhotoImage(pressureResized)
pressureLabelIcon = tk.Label(root, image=pressureImage, bg=colour)
pressureLabelIcon.place(relx=0.75, rely=0.6, anchor="center")
pressureLabel = tk.Label(root, text="Pressure: hPa", font=("Helvetica", 20), bg=colour)
pressureLabel.place(relx=0.75, rely=0.7, anchor="center")
#---------------------------------------------------#



root.configure(bg="#7af5f5")
root.mainloop()








