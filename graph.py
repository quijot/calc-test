from py.xyz2lla import xyz2lla_from_file
from py.sirgas import get_sirgas_weekly_solutions
from py.posgar import transform_to_posgar07
from py.plot import plot_deviations

pg = xyz2lla_from_file('coord.xyz')
sws = get_sirgas_weekly_solutions(pg, download=False)
corrected = transform_to_posgar07(sws, pg)
plot_deviations(corrected, output_dir='plot')
