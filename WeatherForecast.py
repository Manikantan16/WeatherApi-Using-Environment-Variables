#import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
import time
import os
from dotenv import load_dotenv



 
root =Tk()
root.geometry("400x600") #size of the window by default
root.resizable(0,0) #to make the window size fixed
#title of our window
root.title("Weather App - AskPython.com")
root.configure(background = "light blue")




def getWeather():
    #define the APIKeys in the environment variable or env file section
    api_key = os.getenv('api_key')  
     
    # Get city name from user from the input field 
    city=TxtCity.get()
      
    if not city:
        messagebox.showerror("Input Error", "Oops!! City Name cannot be blank.")
        return
    # API url
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        json_data = requests.get(weather_url).json()
        if json_data['cod'] == 200:
            condition = json_data['weather'][0]['main']
            temp = int(json_data['main']['temp'] - 273.15)
            feels_like_temp = int(json_data['main']['feels_like'] - 273.15)
            min_temp = int(json_data['main']['temp_min'] - 273.15)
            max_temp = int(json_data['main']['temp_max'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']
            sunrise_time = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
            sunset_time = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
            cloudy = json_data['clouds']['all']
            description = json_data['weather'][0]['description']
            weather = f"\nWeather of: {city}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
        else:
            weather = f"\n\tWeather for '{city}' not found!\n\tPlease Enter a valid City Name !!"
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")
    
    tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output
 
 
 
 
 
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold',background='light blue').pack(pady=20) #to generate label heading
 
TxtCity = Entry(root, justify='left', width=20, font='Arial 14 bold')
TxtCity.focus()
TxtCity.pack(pady=20)

 
Button(root, command = getWeather, text = "Check Weather", font="Arial 10 bold", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold',background='light blue').pack(pady=10)
 
tfield = Text(root, width=46, height=10,font = 'arial 10 bold')
tfield.pack()

load_dotenv()

root.mainloop()