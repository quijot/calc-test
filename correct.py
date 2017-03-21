#!/usr/bin/env python
from sys import argv
from convert import xyz2lla
from toPOSGAR07 import toPOSGAR07, desvioEP


try:
    ep = argv[1]
    x = argv[2]
    y = argv[3]
    z = argv[4]
    epoch = argv[5]

    lat, lon, alt = xyz2lla(x, y, z)
    latC, lonC = toPOSGAR07(lat, lon, epoch)
    latD, lonD = desvioEP(latC, lonC, ep)
    print("%s\t%.3f\t%.3f\t%s" % (ep, round(latD, 3), round(lonD, 3), epoch))
except:
    pass
