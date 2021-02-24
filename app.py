from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
from PIL import Image
from io import BytesIO
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        # making a tuple items in my UI
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celcius = temp_kelvin - 273.15
        temp_fahr = (temp_kelvin - 273.15) * 9/5 + 32
        icon = json['weather'][0]['icon']
        weathr = json['weather'][0]['main']
        descp = json['weather'][0]['description']
        # return tuple when function called
        final = (city, country, temp_celcius, icon, weathr, descp, temp_fahr)
        return final


def get_icon():
    pass


def search():
    city = city_text.get()
    icons_url = 'http://openweathermap.org/img/wn/{}@2x.png'
    result = get_weather(city)
    if result:
        loc_label['text'] = "{},{}".format(result[0], result[1])
        temp_label['text'] = "{:.2f}°C / {:.2f}°F".format(result[2], result[6])
        # image['bitmap'] = icons_url.format(result[3])
        descp_label['text'] = "{}".format(result[5])
    else:
        messagebox.showerror("Error \n Cannot find {}".format(city))


app = Tk()

# app.title("Weather App")
app.geometry("600x250")

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Weather by City",
                    width=12, command=search)
search_btn.pack()

loc_label = Label(app, text="", font=("bold", 20))
loc_label.pack()


# image = Label(app, bitmap="")
# image.pack()

temp_label = Label(app, text="")
temp_label.pack()

descp_label = Label(app, text="")
descp_label.pack()

app.mainloop()
