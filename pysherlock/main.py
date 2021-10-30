import requests
import time
import wikipedia
from bs4 import BeautifulSoup
import qrcode
from spotify2py import Spotify
import webbrowser as web

def web_ss(website:str):
    BASE = 'https://render-tron.appspot.com/screenshot/'
    url = website
    path = 'screenshot.jpg'
    time.sleep(5)
    response = requests.get(BASE + url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
    
    print("Image saved as screenshot.jpg!")

def wiki(topic:str):
    print(wikipedia.summary(topic))

def weather(city:str):
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
     
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
     
    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
     
    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
     
    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]
     
    # printing all data
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    print(other_data)
    weather = {
        "Temp": temp,
        "Time": time,
        "Sky": sky,
        "Other":other_data
        }
    print(weather)
weather("Bangalore")
def qrgen(data):
    img = qrcode.make(data)
    type(img)  # qrcode.image.pil.PilImage
    img.save("qrcode.png")
        
 def playonSpotify(topic:str, play_track: bool ):
    access_token = requests.get("https://open.spotify.com/get_access_token").json()["accessToken"]
    track_url = Spotify(access_token).get_track(topic)["track_url"]
    if play_track: 
        web.open(track_url)
    else: 
        return track_url
