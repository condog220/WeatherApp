import tkinter as tk
import requests
from PIL import Image, ImageTk
import os
from dotenv import load_dotenv

load_dotenv()

# OpenWeatherMap API configuration
baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
city = ""
completeUrl = baseUrl + "appid=" + appId + "&q=" + city + "&units=metric"

root = tk.Tk()
root.geometry("800x600")
root.title("Weather App")

searchFrame = tk.Frame(root)
searchVar = tk.StringVar()


def fetch_weather():
    appId = os.environ.get("WEATHER_API_KEY")

    if not appId:
        print("Error: WEATHER_API_KEY environment variable not set.")
        return
    

    city = searchVar.get()
    completeUrl = baseUrl + "appid=" + appId + "&q=" + city + "&units=metric"

    response = requests.get(completeUrl)
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']


    tempLabel.config(text=f"Temperature: {temperature} °C")
    humidityLabel.config(text=f"Humidity: {humidity} %")
    pressureLabel.config(text=f"Pressure: {pressure} hPa")
#---------------------------------------------------#
#Add Search Box
cityText = tk.Label(searchFrame, text= "City:")
search_entry = tk.Entry(searchFrame, textvariable=searchVar, font=("Helvetica", 16))
search_Button = tk.Button(searchFrame, text="Search", command=fetch_weather,  font=("Helvetica", 16))

cityText.grid(row=0, column=0)
search_entry.grid(row=0, column=1)
search_Button.grid(row=0, column=2, padx=10)

searchFrame.grid(row=0, column=1, padx=20, pady=20)
#---------------------------------------------------#
### Add Weather Details
weatherIcon = Image.open("img/weather.png")
weatherResized = weatherIcon.resize((100, 100))
weatherImage = ImageTk.PhotoImage(weatherResized)


weatherLabel = tk.Label(root, image=weatherImage)
weatherLabel.grid(row=1, column=1, padx=20, pady=20)

tempLabel = tk.Label(root, text="Temperature: °C", font=("Helvetica", 20))
tempLabel.grid(row=2, column=1, padx=20, pady=10)
#---------------------------------------------------#
# Add Humidity Details
humidityIcon = Image.open("img/humidity.png")
humidityResized = humidityIcon.resize((50, 50))
humidityImage = ImageTk.PhotoImage(humidityResized)
humidityLabelIcon = tk.Label(root, image=humidityImage)
humidityLabelIcon.place(relx=0.25, rely=0.6, anchor="center")

humidityLabel = tk.Label(root, text="Humidity: %", font=("Helvetica", 20))
humidityLabel.place(relx=0.25, rely=0.7, anchor="center")
#---------------------------------------------------#
#Add pressure Details
pressureIcon = Image.open("img/pressure.png")
pressureResized = pressureIcon.resize((100, 100))
pressureImage = ImageTk.PhotoImage(pressureResized)
pressureLabelIcon = tk.Label(root, image=pressureImage)
pressureLabelIcon.place(relx=0.75, rely=0.6, anchor="center")
pressureLabel = tk.Label(root, text="Pressure: hPa", font=("Helvetica", 20))
pressureLabel.place(relx=0.75, rely=0.7, anchor="center")
#---------------------------------------------------#


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=1)

root.mainloop()








