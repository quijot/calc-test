#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import glob
import csv

eps = []
slat = []
slon = []

for file in glob.glob('csv/????.csv'):
  print('Procesando', file)
  x = []
  y = []
  # read from each EP file
  csvfile = open(file,'r')
  plots = csv.reader(csvfile, delimiter='\t')
  for row in plots:
    ep = row[0]
    x.append(float(row[1]))
    y.append(float(row[2]))
  csvfile.close()
  # start processing
  print('Registros:', len(x))
  # font family
  plt.rcParams['font.family'] = 'Abel'
  # figure
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title('Desvíos %s' % ep)
  # ellipse
  a = 3*np.sqrt(np.sum(np.square(x))/(len(x)-1))
  b = 3*np.sqrt(np.sum(np.square(y))/(len(y)-1))
  ax.plot([a, -a], [0, 0], 'k-')
  ax.plot([0, 0], [-b, b], 'k-')
  ellip = patches.Ellipse([0,0], 2*a, 2*b, alpha=0.1, color='r')
  ax.add_patch(ellip)
  ax.set_aspect('equal')
  ax.set_frame_on(False)
  ax.scatter(x, y, s=50, color='b', marker='o')
#  ax.legend(['eje mayor', 'eje menor', 'conf. 99%', 'desvíos'])
  ax.annotate('a=%.3f' % a, xy=(a*.70,a*0.03))
  ax.annotate('b=%.3f' % b, xy=(b*0.03,b*.85), rotation=90)
  ax.grid()
  plt.xlabel('diferencia en longitud [m]')
  plt.ylabel('diferencia en latitud [m]')
  plt.savefig('charts/%s.svg' % ep, format='svg')
  plt.close()
  # prepare lists for late charts
  eps.append(ep)
  slon.append(a)
  slat.append(b)

# EPs con 3*sigma < 5 cm
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('EPs cuya confianza 99% < 0.05 m')
ax.grid()
ax.set_aspect('equal')
ax.set_frame_on(False)
for i in range(1, len(eps)):
  if max(slon[i], slat[i]) < 0.05:
    ax.plot(slon[i], slat[i], 'o')
    ax.annotate(eps[i], xy=(slon[i], slat[i]+0.002), rotation=60)
plt.xlabel('diferencia en longitud [m]')
plt.ylabel('diferencia en latitud [m]')
plt.savefig('charts/min.svg', format='svg')
plt.close()

# EPs con 3*sigma > 5 cm
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('EPs cuya confianza 99% > 0.05 m')
ax.grid()
ax.set_aspect('equal')
ax.set_frame_on(False)
for i in range(1, len(eps)):
  if max(slon[i], slat[i]) > 0.05:
    ax.plot(slon[i], slat[i], 'o')
    ax.annotate(eps[i], xy=(slon[i], slat[i]+0.002), rotation=60)
plt.xlabel('diferencia en longitud [m]')
plt.ylabel('diferencia en latitud [m]')
plt.savefig('charts/max.svg', format='svg')
plt.close()

