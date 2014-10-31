from datetime import datetime
from datetime import timedelta
from calendar import timegm
import calendar
import pytz

def datetime2unixtime(mDateTime):
   return timegm( mDateTime.utctimetuple() )


def unixtime2datetime(utime):
   return datetime.fromtimestamp(utime)

def unixtime2localtime(utime):
   return utc2local( datetime.fromtimestamp(utime) )

#----------The following two functions are from---------------
#http://stackoverflow.com/questions/4563272/how-to-convert-a-python-utc-datetime-to-a-local-datetime-using-only-python-stand/13287083#13287083
def utc_to_local(utc_dt):
    # get integer timestamp to avoid precision lost
    timestamp = datetime2unixtime(utc_dt)#timestamp = calendar.timegm(utc_dt.timetuple())
    local_dt = datetime.fromtimestamp(timestamp)
    assert utc_dt.resolution >= timedelta(microseconds=1)
    return local_dt.replace(microsecond=utc_dt.microsecond)

def utc2local(utc_dt, local_tz=pytz.timezone("Asia/Shanghai")):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)

#-------------------------------------------------------------
