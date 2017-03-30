#!/usr/bin/env python
__author__ = "Santiago Pestarini"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "santiagonob@gmail.com"


def xyz2lla(x, y, z):
    """Conversor de coordenadas Cartesianas geocéntricas a Geodésicas:
        input:
            x, y, z (expresadas en metros)
        output:
            lat, lon (grados sexagesimales), alt (metros)
    """
    from pyproj import Proj, transform

    ecef = Proj(proj='geocent', ellps='GRS80')
    lla = Proj(proj='latlong', ellps='GRS80')
    lon, lat, alt = transform(ecef, lla, x, y, z)
    return lat, lon, alt


def xyz2lla_from_file(xyz_file):
    """
    Convertir coordenadas de un archivo dado de (x,y,z) a (lat,lon,alt)
    input:
        archivo con una línea por EP, con el siguiente formato:
        ep x y z
    output:
        dict, con el siguiente formato:
        {ep: {'lat': lat, 'lon': lon, 'alt': alt}, ...}
    """
    output = {}
    with open(xyz_file) as f:
        for line in f:
            if not line.startswith('#'):
                ep, x, y, z = line.split()
                lat, lon, alt = xyz2lla(x, y, z)
                output[ep] = {'lat': lat, 'lon': lon, 'alt': alt}
    return output
