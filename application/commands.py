from .libraries.news import News
from .libraries.time import Time
from .libraries.weather import Weather


commands = {
    'what are the headlines today': News.headlines,
    'what is the current weather': Weather.current,
    'what is the weather today': Weather.today,
    'what is the weather tomorrow': Weather.tomorrow,
    'what time is it': Time.current
}
