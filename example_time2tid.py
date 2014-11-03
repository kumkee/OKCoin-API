from okcoin.time2tid import time2tid
from okcoin.utiltime import utc2local
from okcoin.utiltime import datetime2unixtime
from okcoin.utiltime import unixtime2localtime
from datetime import datetime, timedelta
#import logging

def main():
   #logging.basicConfig(filename='time2tid_test.log', level=logging.DEBUG)

   my_dt = datetime(2014, 10, 31, 15, 30)

   my_dt = my_dt - timedelta(hours=8) 

   timeformat = "%Y/%b/%d %I:%M:%S %p"

   print
   print "Target time:", utc2local(my_dt).strftime(timeformat)

   #logging.info('Entering time2tid')
   lst_trades = time2tid( datetime2unixtime(my_dt) )
   #logging.info('Done time2tid')

   print "Closing prices:"

   for trade in lst_trades:
      print unixtime2localtime(trade['date']).strftime(timeformat), trade['type'], float(trade['price'])

   print

   print "Raw data:" 
   print lst_trades


if __name__ == '__main__':
   main()
