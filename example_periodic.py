import okcoin.periodic_closing as pc
from datetime import datetime, timedelta
from okcoin.utiltime import unixtime2localtime, unixtime2datetime

def store_trades(raw):
    
   s = ""
   timeformat = "%Y/%b/%d %I:%M:%S %p"
   for trade in raw:
      s += unixtime2datetime(trade['date']).strftime(timeformat)
      s += ' tid:' + str(trade['tid'])
      s += ' ' + trade['type']
      s += ' ' + trade['price']
      s += ';\t'

   print s


def main():
 
   dt_start = datetime(2014, 3, 2, 12)
   dt_final = datetime(2014, 3, 4, 12)

   td = timedelta(hours=1)

   t = datetime.today()

   trade_groups = pc.periodic_closing(dt_start, dt_final, td)

   for g in trade_groups:
      store_trades(g)

   print
   print "Time consumed:", datetime.today() - t

   return 0



if __name__ == '__main__':
   main()
