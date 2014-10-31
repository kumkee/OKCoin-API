from okcoin.time2tid import time2tid
from okcoin.utiltime import utc2local
from okcoin.utiltime import datetime2unixtime
from okcoin.utiltime import unixtime2localtime
from datetime import datetime, timedelta

my_dt = datetime(2014, 10, 31, 12, 30)

my_dt = my_dt - timedelta(hours=8) 

lst_trades = time2tid( datetime2unixtime(my_dt) )

timeformat = "%Y/%b/%d %I:%M:%S %p"

print
print "Target time:", utc2local(my_dt).strftime(timeformat)
print "Closing prices:"

for trade in lst_trades:
   print unixtime2localtime(trade['date']).strftime(timeformat), trade['type'], float(trade['price'])

print

print "Raw data:" 
print lst_trades
