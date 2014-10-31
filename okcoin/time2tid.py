import okcoin
from time import sleep
import sys

imax = 30

def htime(h,i):
    return h[i]['date']

def htid(h,i):
    return h[i]['tid']

def hprice(h,i):
    return float(h[i]['price'])

def check_hzt(h,z,t):
    if htime(h, z+1) < t:
        return 1
    elif htime(h, z) >= t:
        return -1
    else:
        return 0
    #return ( htime(h, z) < t and htime(h, z+1) >= t )

def checkh(h,k,t):
    return ( t > htime(h,k-1) and t <= htime(h,-1) )


def regfalsi_h(s0, s1, k, t, M):
    #M = okcoin.MarketData()
    h1 = M.get_history(since = s1)
    h0 = M.get_history(since = s0)
    h = h1

    side = 0
    a = htid(h0, -1)
    b = htid(h1, k-1)
    fa = htime(h0, -1) - t
    fb = htime(h1, k-1) - t
    i = 0
    if checkh(h0,k,t):
        return h0
    while not checkh(h,k,t):
        i += 1
        s = ( a * fb - b * fa ) / ( fb - fa ) - 2*k
        h = M.get_history(since = s)
        #print " i = %d"%i; i += 1 ####debug
        #print " s = %d"%s####debug
        #print " t0 = %d"% htime(h, 0)####debug
        #print " tn = %d"% htime(h, -1)####debug
        fs0 = htime(h, k-1) - t
        fs1 = htime(h, -1) - t
        if i > imax:
            sys.exit(2)
        if fs1 * fb > 0:
            if side == -1:
                fa /= 2
            side = -1
            fb = fs1
            b = htid(h, k-1)
        elif fs0 * fa > 0:
            if side == 1:
                fb /= 2
            side = 1
            fa = fs0
            a = htid(h, -1)
        else:
            break
    return h
    

def regfalsi(h,t):
    x = 0
    y = len(h) - 1
    side = 0
    fx = htime(h, x) - t
    fy = htime(h, y) - t
    z = x 
    i = 0
    while check_hzt(h, z, t) <> 0:
        i += 1
        if i > imax:
            sys.exit(3)
        #print "z = %d"%z###debug
        #print "tz = %d"%htime(h,z)###debug
        z = ( x * fy - y * fx ) / ( fy - fx )# - 1
        fz = htime(h, z) - t
        if fz * fy > 0:
            if side == -1:
                fx /= 2
            side = -1
            y = z
            fy = htime(h, y) - t
        elif fz * fx > 0:
            if side == 1:
                fy /= 2
            side = 1
            x = z
            fx = htime(h, x) - t
        else:
            if z + 1 == len(h):
                z -= 1
            try:
                inc = check_hzt(h,z,t)
            except IndexError:
                print " z = %d, len = %d, t = %d"% (z, len(h), t)
                print "h[0] =", h[0]
                print "h[n] =", h[-1]
            while inc <> 0: 
                z += inc
                inc = check_hzt(h,z,t)
            break
    return z


def secant(h,k,t):
    f0 = htime(h, 0) - t 
    f1 = htime(h, -1) - t
    return (htid(h,0) * f1 - htid(h,-1) * f0) / (f1 - f0) - 2# - 2*k -1


def time2tid(t, k = 3, start_s = 1, term_s = -1, market=okcoin.MarketData()):
    t = int(t)

    #label = 'timedelta'
    #print 't = {0:d}'.format(t)####debug

    h = regfalsi_h(start_s, term_s, k, t, market)

    z = regfalsi(h,t)

    #print h[z-2]###debug
    #print h[z-1]###debug
    #print h[z]  ###debug
    #print h[z+1]###debug
    #res = list( [ htime(h,z - k+1 +i) - t, hprice(h, z - k+1 +i) ] for i in range(k) )
    
    res = list( h[ z - (k-1-i) ] for i in range(k) )

    return res
