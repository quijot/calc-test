#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import glob
import csv
import datetime

for file in glob.glob('desvios/????.tsv'):
  print('Procesando', file)
  dates = []
  n = []
  e = []
  # read from each EP file
  csvfile = open(file,'r')
  plots = csv.reader(csvfile, delimiter='\t')
  for row in plots:
    ep = row[0]
    n.append(float(row[1]))
    e.append(float(row[2]))
    d = row[3].split('-')
    d = [int(f) for f in d]
    dates.append(datetime.date(d[0],d[1],d[2]))
  csvfile.close()
  # start processing
  print('Registros:', len(dates))
  # font family
  plt.rcParams['font.family'] = 'Abel'
  # figure 1 - NORTE
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title('%s: Componente NORTE [m]' % ep)
  #ax.set_aspect('equal')
  ax.set_frame_on(False)
  ax.plot([min(dates), max(dates)], [0, 0], 'k-')
  ax.plot_date(dates, n, color='b', marker='o')
  ax.grid()
  fig.autofmt_xdate()
  #plt.xlabel('diferencia en longitud [m]')
  #plt.ylabel('diferencia en latitud [m]')
  plt.savefig('flow/%s-N.svg' % ep, format='svg')
  plt.close()
  # figure 2 - ESTE
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title('%s: Componente ESTE [m]' % ep)
  #ax.set_aspect('equal')
  ax.set_frame_on(False)
  ax.plot([min(dates), max(dates)], [0, 0], 'k-')
  ax.plot_date(dates, e, color='g', marker='o')
  ax.grid()
  fig.autofmt_xdate()
  #plt.xlabel('diferencia en longitud [m]')
  #plt.ylabel('diferencia en latitud [m]')
  plt.savefig('flow/%s-E.svg' % ep, format='svg')
  plt.close()
