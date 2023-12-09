#import libraries
import tkinter as tk
from tkinter import *
import requests 


window = Tk()

#functions 
#1 http request
def get_weather():
   api = "7a9f598d91af5090ea403c2743c308bd"
   cityname = search_txt.get()
   url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api}"
   response = requests.get(url)
   weather = response.json()


   temp_lbl.config(text=f"Temperature: {int(weather['main']['temp'] - 273)} c")
   hum_lbl.config(text=f"Humidity: {weather['main']['humidity']}%")
   wind_lbl.config(text=f"Wind Speed: {int(weather['wind']['speed'] /3.6)} km/h")
   press_lbl.config(text=f"Pressure: {weather['main']['pressure']} hPa")
   precip_lbl.config(text=f"Precipitation: {weather.get('rain', {}).get('1h', 0)} %") 



#create widgets
frame_win = tk.Frame(window, relief=tk.RAISED)
search_lbl = tk.Label(frame_win, text="location: ",font=("ARIAL",20), fg='blue')
search_btn = tk.Button(frame_win,text="search",bd=6,fg="black",height=1, width=8,command=get_weather)
search_txt = tk.Entry(frame_win,width =20,font=("ARIAL",12))


temp_lbl = tk.Label(frame_win, text="Temperature: ",font=("ARIAL",20), fg='red') 
hum_lbl = tk.Label(frame_win, text="Humidity: ",font=("ARIAL",20), fg='red')
wind_lbl = tk.Label(frame_win, text="Wind Speed: ",font=("ARIAL",20), fg='red')
press_lbl = tk.Label(frame_win, text="pressure: ",font=("ARIAL",20), fg='red')
precip_lbl = tk.Label(frame_win, text="precipitaion: ",font=("ARIAL",20), fg='red')
#precip doesnt work

#make widgets position
frame_win.grid(column=0, row=0, padx=3,pady=20,sticky="nw")
search_lbl.grid(column=0, row=0, padx=90,pady=5,sticky="nw")
search_btn.grid(column=0, row=0, padx=400,pady=5,sticky="nw")
search_txt.grid(column=0, row=0, padx=200,pady=15,sticky="nw")

temp_lbl.grid(column=0, row=0, padx=50,pady=80,sticky="nw")
hum_lbl.grid(column=0, row=0, padx=50,pady=150,sticky="nw")
wind_lbl.grid(column=0, row=0, padx=50,pady=220,sticky="nw")
press_lbl.grid(column=0, row=0, padx=50,pady=290,sticky="nw")
precip_lbl.grid(column=0, row=0, padx=50,pady=360,sticky="nw")

#bind serch button with enter button in keyboard
window.bind('<Return>', lambda event=None: get_weather())



#create main window
window.title("weather forecast")
window.geometry("500x500+10+10")
mainloop()
