import datetime
from okcoin import utiltime

dt = datetime.datetime(2014,2,19,6,0,0)

ut = utiltime.datetime2unixtime(dt)

dt_local = utiltime.utc2local(dt)

utl = utiltime.datetime2unixtime(dt_local)

print "The reference time in UTC is:"
print dt

print "Its unix timestamp is (utc):"
print ut

print "The reference local time is:"
print dt_local

print "Its unix timestamp is (local timezone):"
print ut
