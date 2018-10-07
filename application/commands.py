from .libraries.time import Time
from .libraries.weather import Weather


commands = {
    'what is the weather today': Weather.today,
    'what is the weather tomorrow': Weather.tomorrow,
    'what time is it': Time.current
}
