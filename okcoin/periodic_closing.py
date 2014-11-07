from time2tid import time2tid
from utiltime import datetime2unixtime
from multiprocessing.pool import ThreadPool
from datetime import datetime, timedelta

MAX_THREADS = 50

def get_tid(dt, k=3):

   return time2tid( datetime2unixtime(dt), k = k )


def periodic_closing(dt0, dt1, delta):

   numThreads = long((dt1 - dt0).total_seconds() / delta.total_seconds() + 1)

   ls_dt = [ dt0 + i*delta for i in xrange(numThreads) ]

   pool = ThreadPool(processes = (numThreads if numThreads <= MAX_THREADS else MAX_THREADS))

   return pool.map(get_tid, ls_dt)
