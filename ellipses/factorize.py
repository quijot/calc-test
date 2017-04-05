from glob import glob

with open('../plotly.js') as js, open('script-line.html') as html:
    js = '<script type="text/javascript">%s</script>' % js.read()[:-1]
    html = html.read()
    for fname in glob('*/index.html', recursive=True):
        with open(fname) as f:
            code = f.read()
        code = code.replace(js, html)
        with open(fname, 'w') as f:
            f.write(code)
