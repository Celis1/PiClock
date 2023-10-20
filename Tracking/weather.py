import os
from typing import Any
import geocoder
import requests
import configparser

# TODO : need to know if this will fail without internet
class WeatherTracker:
    BASE_URL = "http://api.weatherstack.com/current?access_key="
    
    def __init__(self, config_file) -> None:
        self.api_key = self._get_key(config_file)
        self.location = geocoder.ip('me')
        self.city_name = self.location.city
        self.state = self.location.state
        print(self.city_name, self.state)
        self.url = self.BASE_URL + self.api_key + "&query=" + self.city_name + "," + self.state
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
        if response.status_code == 200:
            data = response.json()
            # TODO : remove for debugging
            print(data)
            
            if 'current' in data:
                current_weather = data['current']
                # convert to fahrenheit
                if fahrenheit:
                    temperature = current_weather['temperature'] * 9/5 + 32
                else:
                    temperature = current_weather['temperature']

                description = current_weather['weather_descriptions'][0]
                humidity = current_weather['humidity']
                
                self.weather['temperature'] = temperature
                self.weather['description'] = description
                self.weather['humidity'] = humidity


                # TODO : remove for debugging
                # print(f'Current weather in {self.city_name}:')
                # print(f'Temperature: {temperature}°F')
                # print(f'Description: {description}')
                # print(f'Humidity: {humidity}%')
                return True
            else:
                print('No current weather data available for this location.')
                return False
        else:
            print(f'Failed to retrieve weather data. Status code: {response.status_code}')
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
    weather = WeatherTracker('./config.ini')
    weather.update_weather()
    print(weather())
