from jinja2 import Environment, FileSystemLoader
from webob import Request
import os

assets =[
    'app.js',
    'react.js',
    'leaflet.js',
    'D3.js',
    'moment.js',
    'math.js',
    'main.css',
    'bootstrap.css',
    'normalize.css',
    ]

STYLE = []
SCRIPT = []

def app(environ, start_response):
    response_code = '200 OK'
    response_type = ('Content-Type', 'text/HTML')
    start_response(response_code, [response_type])

    for item in assets:
        (shortname, extension) = os.path.splitext(item)
        if extension == '.css':
            STYLE.append(item)
        elif extension == '.js':
            SCRIPT.append(item)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('index.html')
    print(template.render(css=STYLE, js=SCRIPT))

req2 = Request.blank('index.html')
print(req2.get_response(app))
