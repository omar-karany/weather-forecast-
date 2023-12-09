import tkinter as tk
import requests

def get_weather():
    api_key = "7a9f598d91af5090ea403c2743c308bd"
    city_name = search_txt.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        display_weather_info(weather_data)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        # You can add error handling here, such as displaying an error message to the user

def display_weather_info(weather_data):
    temp_lbl.config(text=f"Temperature: {int(weather_data['main']['temp'] - 273)}°C")
    hum_lbl.config(text=f"Humidity: {weather_data['main']['humidity']}%")
    wind_lbl.config(text=f"Wind Speed: {int(weather_data['wind']['speed'] / 3.6)} km/h")
    press_lbl.config(text=f"Pressure: {weather_data['main']['pressure']} hPa")
    precip_lbl.config(text=f"Precipitation: {get_precipitation(weather_data)} mm")

def get_precipitation(weather_data):
    rain_info = weather_data.get('rain', {}).get('1h', 0)
    return f"{rain_info} mm"

# Create widgets
window = tk.Tk()

frame_win = tk.Frame(window, relief=tk.RAISED)
search_lbl = tk.Label(frame_win, text="Location:", font=("ARIAL", 20), fg='blue')
search_btn = tk.Button(frame_win, text="Search", bd=6, fg="black", height=1, width=8, command=get_weather)
search_txt = tk.Entry(frame_win, width=20, font=("ARIAL", 12))

temp_lbl = tk.Label(frame_win, text="Temperature:", font=("ARIAL", 20), fg='red')
hum_lbl = tk.Label(frame_win, text="Humidity:", font=("ARIAL", 20), fg='red')
wind_lbl = tk.Label(frame_win, text="Wind Speed:", font=("ARIAL", 20), fg='red')
press_lbl = tk.Label(frame_win, text="Pressure:", font=("ARIAL", 20), fg='red')
precip_lbl = tk.Label(frame_win, text="Precipitation:", font=("ARIAL", 20), fg='red')

# Make widgets position
frame_win.grid(column=0, row=0, padx=3, pady=20, sticky="nw")
search_lbl.grid(column=0, row=0, padx=90, pady=5, sticky="nw")
search_btn.grid(column=0, row=0, padx=400, pady=5, sticky="nw")
search_txt.grid(column=0, row=0, padx=200, pady=15, sticky="nw")

temp_lbl.grid(column=0, row=0, padx=50, pady=80, sticky="nw")
hum_lbl.grid(column=0, row=0, padx=50, pady=150, sticky="nw")
wind_lbl.grid(column=0, row=0, padx=50, pady=220, sticky="nw")
press_lbl.grid(column=0, row=0, padx=50, pady=290, sticky="nw")
precip_lbl.grid(column=0, row=0, padx=50, pady=360, sticky="nw")

# Bind search button with Enter key in the keyboard
window.bind('<Return>', lambda event=None: get_weather())

# Create main window
window.title("Weather Forecast")
window.geometry("500x500+10+10")
window.mainloop()
