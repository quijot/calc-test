#!/usr/bin/env python
__author__ = "Santiago Pestarini"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "santiagonob@gmail.com"


def sign(number):
    """Will return 1 for positive
    or zero, and -1 for negative"""
    try:
        return number/abs(number)
    except ZeroDivisionError:
        return 1


def to_posgar07(lat, lon, epoch):
    """
    Correcciones para transformar coordenadas geodésicas de ITRF08, época X
    a POSGAR07 (ITRF05, época 2006.632)
    """
    from datetime import datetime as dt
    import py.sumBL as sumBL
    import py.vms2015 as vms2015

    # obs_date
    fmt = '%Y-%m-%d'
    obs_date = dt.strptime(epoch, fmt)
    obs_date = obs_date.timetuple()
    obs_day = obs_date.tm_yday + 0.5  # es al mediodia
    year_days = dt.strptime('%d-12-31' % obs_date.tm_year, fmt).timetuple()
    obs_epoch = year_days.tm_year + obs_day / year_days.tm_yday
    # ref_date 2011.322
    start_epoch = 2011.322
    years = obs_epoch - start_epoch
    # round lat, lon
    latd = round(lat)
    lond = round(lon)
    # arcos
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


def am1seg(lat, lon):
    """Arco de Meridiano de 1 segundo para Latitudi=lat"""
    from pyproj import Geod
    g = Geod(ellps="GRS80")
    return g.inv(lon, lat, lon, lat+1/3600)[2]


def ap1seg(lat, lon):
    """Arco de Paralelo de 1 segundo para Latitudi=lat"""
    from pyproj import Geod
    g = Geod(ellps="GRS80")
    return g.inv(lon, lat, lon+1/3600, lat)[2]


def deviations(lat1, lon1, lat2, lon2):
    """Desvíos entre lat1-lat2 y lon1-lon2 en metros."""
    from pyproj import Geod
    g = Geod(ellps="GRS80")
    azi1, azi2, dLat = g.inv(lon1, lat1, lon1, lat2)
    dLat = sign(azi1) * dLat
    azi1, azi2, dLon = g.inv(lon1, lat1, lon2, lat1)
    dLon = sign(azi1) * dLon
    return dLat, dLon


def transform_to_posgar07(sirgas, p07):
    """
    Transformar masivamente coordenadas de ITRF08 a POSGAR07
    input:
        sirgas = {ep: {week1: {'lat': lat, 'lon': lon}, week2: { ... }}}
        p07 = list, tuple, dict con lista de EP en sirgas a corregir
    output:
        misma estructura con coordenadas 'corregidas'
    """
    from collections import defaultdict
    from datetime import timedelta as td
    from gnsstime import gnsstime as gt

    corrected = defaultdict(dict)
    for ep in p07:
        for wk in sirgas[ep]:
            gpsdt = gt.from_gpsw(wk) + td(days=3.5)
            latc, lonc = to_posgar07(sirgas[ep][wk]['lat'],
                                     sirgas[ep][wk]['lon'],
                                     str(gpsdt.date()))
            latd, lond = deviations(p07[ep]['lat'],
                                    p07[ep]['lon'],
                                    latc,
                                    lonc)
            corrected[ep][wk] = {'lat': latc,
                                 'lon': lonc,
                                 'd_lat': latd,
                                 'd_lon': lond}
    return corrected
