import requests
import time

def moveBlinds():
    print( "The code to move blind here")

previousState = 0
#Add your own app id (after the appid=) , you need to make an account on api.openweathermap.org (It is free to do so)
api_address = 'http://api.openweathermap.org/data/2.5/weather?q=San%20Diego&appid='
data = requests.get(api_address)
weather_dict = data.json()

# Change the sunset and sunrise to the ones commented to make it work irl
sunrise = time.time()
sunset = sunrise + 60
#sunset = weather_dict['sys']['sunset']
#sunrise = weather_dict['sys']['sunrise']
currentTime = time.time()

if ( currentTime > sunrise and currentTime < sunset ):
    previousState = 1

currentState = previousState
hasStateChanged = 0
flag = 0
while( True ):
    currentTime = time.time()
    print( currentState, previousState )
    if( flag ):
        break
    if( currentTime > sunrise and currentTime < sunset ):
        currentState = 1
    else:
        currentState = 0
    if ( currentState != previousState ):
        moveBlinds()
        previousState = currentState
        flag = 1
        data = requests.get(api_address)
        weather_dict = data.json()
        #sunset = weather_dict['sys']['sunset']
        #sunrise = weather_dict['sys']['sunrise']
