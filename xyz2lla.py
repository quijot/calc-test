#!/usr/bin/env python
import pyproj
from sys import argv
from convert import xyz2lla


try:
  ep = argv[1]
  x = argv[2]
  y = argv[3]
  z = argv[4]
  try: epoch = argv[5]
  except: epoch = 2006.632

  lat, lon, alt = xyz2lla(x, y, z)
  #print(ep, lat, lon, alt, epoch)
  print("'%s': { 'lat': %s, 'lon': %s, 'alt': %s }," % (ep, lat, lon, alt))
except:
  pass

