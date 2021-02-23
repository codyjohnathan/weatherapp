from tkinter import *
from configparser import ConfigParser
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

icons = 'http://openweathermap.org/img/wn/{}@2x.png'

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()

    else:
        return None


def get_icon():
    pass


def search():
    pass


get_weather("London")


app = Tk()

app.title("Weather App")
app.geometry('600x250')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Weather by City",
                    width=12, command=search)
search_btn.pack()

loc_label = Label(app, text="", font=("bold", 20))
loc_label.pack()


image = Label(app, bitmap='')
image.pack()

temp_label = Label(app, text='')
temp_label.pack()

app.mainloop()
