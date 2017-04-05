#!/usr/bin/env python
__author__ = "Santiago Pestarini"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "santiagonob@gmail.com"

import os
from gnsstime import gnsstime as gt

font_family = 'Source Sans Pro'


def plot_plotly(ep, weeks, e, n, output_dir):
    import plotly.offline as py
    import plotly.graph_objs as go
    # Create and style traces
    trace_e = go.Scatter(
        x=weeks,
        y=e,
        mode='lines+markers',
        name='este',
        line=dict(color='green'),
    )
    trace_n = go.Scatter(
        x=weeks,
        y=n,
        mode='lines+markers',
        name='norte',
        line=dict(color='blue'),
    )
    trace_0 = go.Scatter(
        x=weeks,
        y=[0, ]*len(weeks),
        mode='lines',
        name='',
        showlegend=False,
        line=dict(color='black'),
    )
    data = [trace_0, trace_e, trace_n]
    # Edit the layout
    ft = "%s: diferencias entre coordenadas oficiales y \"corregidas\""
    layout = dict(title=ft % ep.upper(),
                  # xaxis=dict(title='gps weeks'),
                  yaxis=dict(title='metros'),
                  font=dict(family=font_family)
                  )
    fig = dict(data=data, layout=layout)
    _dir = '%s/%s' % (output_dir, ep)
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    fname = '%s/index.html' % _dir
    py.plot(fig, filename=fname, auto_open=False, show_link=False)


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
    p.circle(weeks, e, legend="este", fill_color=ec, line_color=ec)
    p.line(weeks, n, line_color=nc)
    p.circle(weeks, n, legend="norte", fill_color=nc, line_color=nc)
    # show the results
    save(p)


def plot_deviations(ep_list, output_dir='evolution'):
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


def plot_ellipses(ep_list, output_dir='ellipses'):
    print("Saving ellipses graphics...")
    for ep in ep_list:
        print(ep)
        # prepare some data
        e = []
        n = []
        for wk in ep_list[ep]:
            e.append(round(ep_list[ep][wk]['d_lon'], 3))
            n.append(round(ep_list[ep][wk]['d_lat'], 3))
        # call plot function
        plot_ellipse_3sigma(ep, e, n, output_dir)
    print("DONE\n")


def plot_ellipse_3sigma(ep, e, n, output_dir):
    import numpy as np
    import plotly.offline as py
    import plotly.graph_objs as go
    # Prepare some data
    a = 3*np.sqrt(np.sum(np.square(e))/(len(e)-1))
    b = 3*np.sqrt(np.sum(np.square(n))/(len(n)-1))
    # Create and style traces
    trace = go.Scatter(
        x=e,
        y=n,
        mode='markers',
        name='desvíos',
    )
    trace_a = go.Scatter(
        x=[-a, a],
        y=[0, 0],
        mode='lines',
        name='a=%.3f [m]' % a,
        line=dict(color='black'),
    )
    trace_b = go.Scatter(
        x=[0, 0],
        y=[-b, b],
        mode='lines',
        name='b=%.3f [m]' % b,
        line=dict(color='black'),
    )
    data = [trace, trace_a, trace_b]
    # Edit the layout
    ft = "%s: desvíos y elipse de confianza del 99%%"
    factor = 1 / max(0.015, min(a, b)) * 1000
    factor = 1 / ((a + b) / 2) * 1000
    print(ep, factor)
    layout = dict(
        title=ft % ep.upper(),
        xaxis=dict(title='diferencia en longitud [m]'),
        yaxis=dict(title='diferencia en latitud [m]'),
        font=dict(family=font_family),
        hovermode='closest',
        height=b*factor,
        width=a*factor,
        shapes=[
            {
                'type': 'circle',
                'xref': 'x',
                'yref': 'y',
                'x0': -a,
                'y0': -b,
                'x1': a,
                'y1': b,
                'opacity': 0.1,
                'fillcolor': 'red',
                'line': {
                    'color': 'red',
                },
            }
        ]
    )
    fig = dict(data=data, layout=layout)
    _dir = '%s/%s' % (output_dir, ep)
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    fname = '%s/index.html' % _dir
    py.plot(fig, filename=fname, auto_open=False, show_link=False)
