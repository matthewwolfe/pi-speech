import os
import pyowm


owm = pyowm.OWM(os.getenv('OWM_API_KEY'))

class Weather:

    @staticmethod
    def current():
        observation = owm.weather_at_place(os.getenv('OWM_LOCATION'))
        weather = observation.get_weather()

        status = weather.get_detailed_status()
        temperatures = weather.get_temperature(unit='fahrenheit')
        currentTemperature = int(round(temperatures['temp']))

        return 'Current weather is %s, Temperature is %s degrees Fahrenheit' % (status, currentTemperature)

    @staticmethod
    def today():
        forecast = owm.daily_forecast(os.getenv('OWM_LOCATION'), limit=1).get_forecast().get_weathers()
        weather = next(iter(forecast), None)

        temperatures = weather.get_temperature(unit='fahrenheit')
        rain = weather.get_rain()
        wind = weather.get_wind(unit='miles_hour')

        if 'all' in rain:
            rain = int(round(rain['all'] * 100))
        else:
            rain = 0;

        return '''
            The forecast for today is %s with a high of %s degrees Fahrenheit. The chance of rain is %s percent.
            Average wind around %s MPH.
        ''' % (
            weather.get_detailed_status(),
            int(round(temperatures['max'])),
            rain,
            int(round(wind['speed']))
        )

    @staticmethod
    def tomorrow():
        pass
