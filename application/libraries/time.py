import datetime


class Time:

    @staticmethod
    def current():
        return 'It is %s' % datetime.datetime.now().strftime('%I:%M%p')
