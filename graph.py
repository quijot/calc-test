import os

from py.plot import plot_deviations, plot_ellipses
from py.posgar import transform_to_posgar07
from py.sirgas import get_sirgas_weekly_solutions
from py.xyz2lla import xyz2lla_from_file


def save_tsv(dic, output_dir='tsv'):
    # save dic to TSV (tab separated value)
    import os
    import csv
    from gnsstime import gnsstime as gt
    from datetime import timedelta as td

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for ep, sol in dic.items():
        fname = '%s/%s.tsv' % (output_dir, ep)
        with open(fname, 'w') as f:
            w = csv.writer(f, delimiter='\t')
            w.writerow(['station', 'd_lat', 'd_lon', 'gpsweek', 'date'])
            for week, coord in sol.items():
                gpsdt = gt.from_gpsw(week) + td(days=3.5)
                dlat = '%.3f' % round(coord['d_lat'], 3)
                dlon = '%.3f' % round(coord['d_lon'], 3)
                w.writerow([ep, dlat, dlon, week, gpsdt.date()])


def save(struct, fname):
    # save struct to fname
    from pprint import pprint
    with open(fname, 'w') as f:
        pprint(struct, f)


output = 'results'
if not os.path.exists(output):
    os.makedirs(output)

pg = xyz2lla_from_file('coord.xyz')
sws = get_sirgas_weekly_solutions(pg, download=False)
corrected = transform_to_posgar07(sws, pg)
plot_deviations(corrected, output_dir='%s/evolution' % output)
plot_ellipses(corrected, output_dir='%s/ellipses' % output)
save(dict(corrected), '%s/corrected.py' % output)
save_tsv(corrected, output_dir='%s/desvios' % output)
