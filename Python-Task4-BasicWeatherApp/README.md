# Task 4 — Basic Weather App

## Overview

A beginner-friendly command-line weather application that uses the OpenWeatherMap Current Weather API to retrieve live weather information for a city.

## Internship Requirements Covered

- Ask the user for a city name
- Call OpenWeatherMap and parse JSON
- Display temperature in Celsius and Fahrenheit
- Display humidity
- Display weather condition
- Display wind speed
- Handle city-not-found, timeout/network, and invalid-key errors
- Reject empty city input

## Technologies

- Python
- `requests`
- JSON responses
- OpenWeatherMap API

## Run

```bash
python -m pip install -r requirements.txt
python main.py
```

## API Key Setup

Set the `OPENWEATHER_API_KEY` environment variable before running the app. Do not commit your real API key to GitHub.

Windows PowerShell:

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY"
```

Windows Command Prompt:

```cmd
set OPENWEATHER_API_KEY=YOUR_API_KEY
```

macOS/Linux:

```bash
export OPENWEATHER_API_KEY="YOUR_API_KEY"
```

## Screenshots

Add screenshots showing a successful weather lookup, city-not-found handling, and empty-input validation.
