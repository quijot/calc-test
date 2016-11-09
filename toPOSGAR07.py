#!/usr/bin/env python
import vms2015, sumBL
import datetime
from pyproj import Geod, Proj, transform
from coordp07 import posgar07


def sign(number):
    """Will return 1 for positive
    or zero, and -1 for negative"""
    try:return number/abs(number)
    except ZeroDivisionError:return 1


def toPOSGAR07(lat, lon, epoch):
    # obsDate
    fmt = '%Y-%m-%d'
    obsDate = datetime.datetime.strptime(epoch, fmt)
    obsDate = obsDate.timetuple()
    obsDay = obsDate.tm_yday + 0.5 # es al mediodia
    yearDays = datetime.datetime.strptime('%d-12-31' % obsDate.tm_year, fmt).timetuple()
    obsEpoch = yearDays.tm_year + obsDay / yearDays.tm_yday
    # refDate 2011.322
    startEpoch = 2011.322
    years = obsEpoch - startEpoch
    # round lat, lon
    latd = round(lat)
    lond = round(lon)
    # arcos
    g = Geod(ellps="GRS80")
    am = am1seg(latd, lond)
    ap = ap1seg(latd, lond)
    # correc
    # variable, hasta 2011.322
    cLat1 = vms2015.vel[lond][latd]['n'] / am * years / 3600
    cLon1 = vms2015.vel[lond][latd]['e'] / ap * years / 3600
    # fija, desde 2011.322 hasta 2006.632
    cLat2 = sumBL.disp[lond][latd]['n'] / am / 3600
    cLon2 = sumBL.disp[lond][latd]['e'] / ap / 3600
    # resultados
    latC = lat - cLat1 + cLat2
    lonC = lon - cLon1 + cLon2
    return latC, lonC


# Arco de Meridiano de 1 segundo para Latitudi=lat
def am1seg(lat, lon):
    g = Geod(ellps="GRS80")
    return g.inv(lon,lat,lon,lat+1/3600)[2]


# Arco de Paralelo de 1 segundo para Latitudi=lat
def ap1seg(lat, lon):
    g = Geod(ellps="GRS80")
    return g.inv(lon,lat,lon+1/3600,lat)[2]


# Desvíos entre lat1-lat2 y lon1-lon2
def desvios(lat1, lon1, lat2, lon2):
    g = Geod(ellps="GRS80")
    azi1, azi2, dLat = g.inv(lon1, lat1, lon1, lat2)
    dLat = sign(azi1) * dLat
    azi1, azi2, dLon = g.inv(lon1, lat1, lon2, lat1)
    dLon = sign(azi1) * dLon
    return dLat, dLon


# Desvíos entre coordenadas dadas y coordenadas de un EP dada
# latEP-lat y lonEP-lon
def desvioEP(lat, lon, EP):
    latEP = posgar07[EP]['lat']
    lonEP = posgar07[EP]['lon']
    return desvios(latEP, lonEP, lat, lon)
