#!/usr/bin/env python
__author__ = "Santiago Pestarini"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "santiagonob@gmail.com"


from gnsstime import gnsstime as gt


def get_sirgas_weekly_solutions(ep_list,
                                from_week=1640,
                                to_week=gt.now().gpsw,
                                step=1,
                                crddir='sws/',
                                download=True):
    """Descarga los archivos de soluciones semanales IBG para SIRGAS,
    las convierte a geodésicas y devuelve un dict con los resultados.
    input:
        ep_list: ['EP01', 'EP02', ...] (list, tuple o cualquier tipo iterable)
        from_week: int (semana gps de la primera solución requerida)
        to_week: int (semana gps de la última solución requerida (NO incluida))
        step: int (intervalo de semanas, si es 2, se descargan cada 2 semanas)
        crddir: string (directorio de descarga)
        download: bool (si es True intenta descargar los archivos, si no
                  busca y procesa archivos en crddir)
    output:
        dict:
            {'EP01':
                {1640: {'lat': -33.6789, 'lon': -60.1234},
                 1642: {'lat': -33.6789, 'lon': -60.1234}},
             'EP02':
                {1640: {'lat': -33.6789, 'lon': -60.1234},
                 1642: {'lat': -33.6789, 'lon': -60.1234}}
            }
    usage:
        >>> from sirgas import get_sirgas_weekly_solutions as sws
        >>> solutions = sws(ep_list)  # use default parameteres
        >>> soluciones['UNRO'][1900]
        >>> {'lat': -32.959351923311004, 'lon': -60.62842570569655}
    """
    from os.path import isfile
    from shutil import copyfileobj
    from urllib.request import urlopen
    from collections import defaultdict
    from datetime import timedelta as td
    from py.xyz2lla import xyz2lla
    import os

    solution_set = 'ibg'
    sirgas = defaultdict(dict)
    if not os.path.exists(crddir):
        os.makedirs(crddir)

    print("Downloading SIRGAS weekly solutions",
          "and converting it from (x, y, z) to (lat, lon, alt)...")
    for wk in range(from_week, to_week, step):
        gpsdt = gt.from_gpsw(wk) + td(days=3.5)
        year = str(gpsdt.year)[2:]  # 2 digits year
        crdfile = "%s%sP%s.crd" % (solution_set, year, wk)
        url = "ftp://ftp.sirgas.org/pub/gps/SIRGAS/%s/%s" % (wk, crdfile)
        print(url)
        crd = '%s%s' % (crddir, crdfile)
        if isfile(crd):
            print("File %s already exists" % crdfile)
            with open(crd) as f:
                data = f.read().split('\n')
        elif download:
            try:
                with urlopen(url) as response, open(crd, 'wb') as out_file:
                    copyfileobj(response, out_file)
                    data = response.read().decode('utf-8').split('\n')
            except:
                print("ERROR downloading %s file" % crdfile)
                data = ''
        else:
            print("File %s don't exists. Not downloading it." % crdfile)
            data = ''
        for line in data:
            if line.strip()[:1].isdigit():
                try:
                    num, ep, name, x, y, z, flag = line.split()
                    if ep in ep_list:
                        lat, lon, alt = xyz2lla(x, y, z)
                        sirgas[ep][wk] = {'lat': lat, 'lon': lon}
                except:
                    pass
    return sirgas
