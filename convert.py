#!/usr/bin/env python
from pyproj import Proj, transform


# Conversor de Cartesianas geocéntricas a Geodésicas
def xyz2lla(x, y, z):
  ecef = Proj(proj='geocent', ellps='GRS80')
  lla = Proj(proj='latlong', ellps='GRS80')
  lon, lat, alt = transform(ecef, lla, x, y, z)
  return lat, lon, alt

