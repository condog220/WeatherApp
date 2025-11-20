import tkinter as tk
import requests
from PIL import Image, ImageTk

# OpenWeatherMap API configuration
appId = "3729e98fa6f69aeccb7b10332b62f0e8"
baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
city = ""
completeUrl = baseUrl + "appid=" + appId + "&q=" + city + "&units=metric"

root = tk.Tk()
root.geometry("800x600")
root.title("Weather App")

searchFrame = tk.Frame(root)
searchVar = tk.StringVar()


def fetch_weather(city):
    completeUrl = baseUrl + "appid=" + appId + "&q=" + city + "&units=metric"
    response = requests.get(completeUrl)
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    tempLabel.config(text=f"Temperature: {temperature} °C")


def Find():
    city = searchVar.get()
    fetch_weather(city)


cityText = tk.Label(searchFrame, text= "City:")
search_entry = tk.Entry(searchFrame, textvariable=searchVar, font=("Helvetica", 16))
search_Button = tk.Button(searchFrame, text="Search", command=Find,  font=("Helvetica", 16))

cityText.grid(row=0, column=0)
search_entry.grid(row=0, column=1)
search_Button.grid(row=0, column=2, padx=10)

searchFrame.grid(row=0, column=1, padx=20, pady=20)

### Add Weather Details
weatherIcon = Image.open("img/weather.png")
weatherResized = weatherIcon.resize((100, 100))
weatherImage = ImageTk.PhotoImage(weatherResized)


weatherLabel = tk.Label(root, image=weatherImage)
weatherLabel.grid(row=1, column=1, padx=20, pady=20)

tempLabel = tk.Label(root, text="Temperature: °C", font=("Helvetica", 20))
tempLabel.grid(row=2, column=1, padx=20, pady=10)


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=1)

root.mainloop()








