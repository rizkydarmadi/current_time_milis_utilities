import pytz
from datetime import datetime
import datetime as dt

class Datetime():

    def convert_from_utc_milis_to_local_timezone(utc_milis,timezone):

        utc_datetime = dt.datetime.utcfromtimestamp(utc_milis/1000.)
        return utc_datetime.replace(tzinfo=pytz.timezone('UTC')).astimezone(timezone).strftime('%d.%m.%Y %H:%M:%S')
       

    def convert_local_timezone_to_utc_milis(localtime):

        date = datetime.strptime(localtime,'%d.%m.%Y %H:%M:%S')
        date_= date.astimezone(pytz.UTC)

        return round(date_.timestamp() * 1000)

