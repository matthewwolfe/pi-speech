import os
import pyowm


owm = pyowm.OWM(os.getenv('OWM_API_KEY'))

class Weather:

    @staticmethod
    def today():
        observation = owm.weather_at_place(os.getenv('OWM_LOCATION'))
        weather = observation.get_weather()

        status = weather.get_status()
        temperatures = weather.get_temperature(unit='fahrenheit')
        currentTemperature = int(round(temperatures['temp']))

        return 'Current weather is %s, Temperature is %s degrees Fahrenheit' % (status, currentTemperature)

    @staticmethod
    def tomorrow():
        pass
