import json
import random
import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

END = "\x1b[0m"
CLEAR = "[033[H"

RED = "\033[91m"
WHITE = "\033[97m"
BLACK = "\033[90m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

def WeatherReport():
    city_name = "Saint Petersburg"
    api_key = '641ea5cd5814ed50841ef8ff8446b7b7'
    url_weather = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

    response = requests.get(url_weather)
    result = json.loads(response.text)
    
    if response.status_code == 200:
        
        country = result['sys']['country']
        weather = result['weather'][0]['description']
        humidity = result['main']['humidity']
        pressure = result['main']['pressure']
        
        print(f'{BLUE}Report weather in {city_name}, {country}{END}')
        print(f' - Description: {weather}')
        print(f' - Humidity: {humidity} %')
        print(f' - Pressure: {pressure} hPa')

    else:
        print("Unable to receive data")

def GetFromAPI():
    num = random.randint(1, 800)
    url = f'https://rickandmortyapi.com/api/character/{num}'
    response = requests.get(url)
    result = response.json()
    
    id = result['id']
    name = result['name']
    status = result['status']
    species = result['species']
    type_species = result['type']
    gender = result['gender']
    origin = result['origin']['name']

    print(f'{BLUE}Information about character: (From Rick and Morty API){END}')
    print(f' - ID: {id}')
    print(f' - Name: {name}')
    print(f' - Status: {status}')
    print(f' - Species: {species}')
    print(f' - Type of species: {type_species}')
    print(f' - Gender: {gender}')
    print(f' - Origin: {origin}')

def GetFox():
    url = f'https://randomfox.ca/floof/'
    response = requests.get(url)
    image_url = response.json()['image']

    image_response = requests.get(image_url)
    image_data = Image.open(BytesIO(image_response.content))
        
    # Convert image
    image_data = image_data.resize((600, 400), Image.LANCZOS)
    image_tk = ImageTk.PhotoImage(image_data)
        
    # Update image
    label.config(image=image_tk)
    label.image = image_tk



if __name__ ==  "__main__":
    WeatherReport()
    GetFromAPI()

    root = tk.Tk()
    root.title("Fox is ya best!!")

    label = tk.Label(root)
    label.pack()

    button = tk.Button(root, text = "Nex Foxxxxx!", command = GetFox)
    button.pack()
    GetFox()

    root.mainloop()