from time2tid import time2tid
from utiltime import datetime2unixtime
from multiprocessing.pool import ThreadPool
from datetime import datetime, timedelta

from functools import partial

MAX_THREADS = 50

def get_tid(dt, k=3, start_s=0, term_s=-1 ):

   return time2tid( datetime2unixtime(dt), k = k, start_s=start_s, term_s=term_s )


def __periodic_closing(dt0, dt1, delta, func=get_tid):

   numThreads = long((dt1 - dt0).total_seconds() / delta.total_seconds() + 1)

   ls_dt = [ dt0 + i*delta for i in xrange(numThreads) ]

   pool = ThreadPool(processes = (numThreads if numThreads <= MAX_THREADS else MAX_THREADS))

   return pool.map(func, ls_dt)


def periodic_closing(dt0, dt1, delta):

   mydel_seconds = long((dt1 - dt0).total_seconds() / delta.total_seconds()) * delta.total_seconds()
   mydel = timedelta(seconds = mydel_seconds)

   [tradegroup0, tradegroup1] = __periodic_closing(dt0, dt1, mydel)

   s0 = tradegroup0[0]['tid']
   s1 = tradegroup1[0]['tid']

   mapfunc = partial(get_tid, start_s=s0, term_s=s1)

   tradegroups = __periodic_closing(dt0+delta, dt1-delta, delta, mapfunc)
 
   tradegroups.insert(0, tradegroup0)
   tradegroups.append(tradegroup1)

   return tradegroups
