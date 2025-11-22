# Weather App

A sleek and user-friendly desktop application that provides real-time weather updates for cities worldwide. Built with Python and Tkinter, this app utilizes the OpenWeatherMap API to deliver accurate temperature, humidity, and pressure data in a clean interface.

## Features

*   **Real-Time Weather Data**: Fetches current weather conditions including temperature, humidity, pressure, min/max temps.
*   **City Search**: Easily search for weather data by city name.
*   **Visual Feedback**: Dynamic weather icons and a clean, color-coded UI.
*   **Detailed Metrics**: View precise metrics like atmospheric pressure (hPa) and humidity percentages.

## Prerequisites

Before you begin, ensure you have the following installed:
*   Python 3.x
*   An active API key from [OpenWeatherMap](https://openweathermap.org/api)

## Installation

1.  **Clone the repository**
    ```bash
    git clone <repository-url>
    cd WeatherApp
    ```

2.  **Install dependencies**
    This project requires `requests`, `pillow`, and `python-dotenv`.
    ```bash
    pip install requests pillow python-dotenv
    ```

## Configuration

1.  Create a file named `.env` in the root directory of the project.
2.  Add your OpenWeatherMap API key to the `.env` file:
    ```env
    WEATHER_API_KEY=your_api_key_here
    ```

## Usage

Run the application using Python:

```bash
python app.py
```

1.  Enter a city name in the search bar (e.g., "London", "Tokyo").
2.  Click **Search** to view the current weather details.

## Technologies Used

*   **[Python](https://www.python.org/)**: Core programming language.
*   **[Tkinter](https://docs.python.org/3/library/tkinter.html)**: Standard GUI library for Python.
*   **[OpenWeatherMap API](https://openweathermap.org/)**: Source for real-time weather data.
*   **[Pillow (PIL)](https://python-pillow.org/)**: Python Imaging Library for handling images.
