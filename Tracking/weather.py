
import os
from typing import Any
import geocoder
import requests
import configparser

# TODO : need to know if this will fail without internet
class WeatherTracker:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    
    def __init__(self, config_file) -> None:
        self.api_key = self._get_key(config_file)
        self.location = geocoder.ip('me')
        self.city_name = self.location.city
        self.url = self.BASE_URL + "appid=" + self.api_key + "&q=" + self.city_name
        self.weather = {
            'temperature': None,
            'pressure': None,
            'humidity': None,
            'description': None
        }

    def __call__(self):
        return self.weather

    def update_weather(self, fahrenheit = True):
        response = requests.get(self.url)
        x = response.json()
        if x["cod"] != "404":        
            y = x["main"]
            
            if fahrenheit:
                # convert temp to fahrenheit
                temperature = y["temp"] * 9/5 - 459.67
            else:
                # TODO : verify that this is correct
                # use celcius
                temperature = y["temp"] - 273.15

            self.weather['temperature'] = temperature
            self.weather['pressure'] = y["pressure"]
            self.weather['humidity'] = y["humidity"]
        
            z = x["weather"]
            self.weather['description'] = z[0]["description"]
            return True
        
        else:
            print(" City Not Found ")
            return False

    def _get_key(self, config_file):
        '''
        Function for getting the api key from the config file
        '''
        # make sure the config file exists
        if not os.path.exists(config_file):
            return None
        else:
            config = configparser.ConfigParser()
            config.read(config_file)

            return config.get('Keys', 'weather_api')


if __name__ == "__main__":
    weather = WeatherTracker()
    weather.update_weather()
    print(weather())