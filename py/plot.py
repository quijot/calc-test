#!/usr/bin/env python
__author__ = "Santiago Pestarini"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "santiagonob@gmail.com"

import os
from gnsstime import gnsstime as gt


def plot_plotly(ep, weeks, e, n, output_dir):
    import plotly.offline as py
    import plotly.graph_objs as go
    # Create and style traces
    trace_e = go.Scatter(
        x=weeks,
        y=e,
        mode='lines+markers',
        name='east',
        line=dict(color='green')
    )
    trace_n = go.Scatter(
        x=weeks,
        y=n,
        mode='lines+markers',
        name='north',
        line=dict(color='blue')
    )
    trace_0 = go.Scatter(
        x=weeks,
        y=[0, ]*len(weeks),
        mode='lines',
        name='',
        showlegend=False,
        line=dict(color='black')
    )
    data = [trace_0, trace_e, trace_n]
    # Edit the layout
    ft = "%s difference between official and corrected coordinates"
    layout = dict(title=ft % ep.upper(),
                  # xaxis=dict(title='gps weeks'),
                  yaxis=dict(title='meters'),)
    fig = dict(data=data, layout=layout)
    _dir = '%s/%s' % (output_dir, ep)
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    fname = '%s/index.html' % _dir
    py.plot(fig, filename=fname, auto_open=False)


def plot_bokeh(ep, weeks, e, n, output_dir):
    from bokeh.plotting import figure, output_file, save
    # output to static HTML file
    _dir = '%s/%s' % (output_dir, ep)
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    output_file('%s/index.html' % _dir)
    # create a new plot with a title and axis labels
    ft = "%s difference between official and corrected coordinates"
    p = figure(title=ft % ep.upper(),
               x_axis_label='gps weeks',
               y_axis_label='meters')
    # add a line renderer with legend and line thickness
    ec = 'green'
    nc = 'blue'
    zc = 'black'
    p.line(weeks, [0, ]*len(weeks), line_width=2, line_color=zc)
    p.line(weeks, e, line_color=ec)
    p.circle(weeks, e, legend="east", fill_color=ec, line_color=ec)
    p.line(weeks, n, line_color=nc)
    p.circle(weeks, n, legend="north", fill_color=nc, line_color=nc)
    # show the results
    save(p)


def plot_deviations(ep_list, output_dir='plot'):
    print("Saving deviations graphics...")
    for ep in ep_list:
        print(ep)
        # prepare some data
        e = []
        n = []
        weeks = []
        for wk in ep_list[ep]:
            e.append(round(ep_list[ep][wk]['d_lon'], 3))
            n.append(round(ep_list[ep][wk]['d_lat'], 3))
            weeks.append(gt.from_gpsw(wk))
        # call plot function
        plot_plotly(ep, weeks, e, n, output_dir)
    print("DONE\n")
