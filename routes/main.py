from __main__ import app
from globals import *
from twingate_queries import *

#index route
@app.route('/')
def index():
    connectors_data = connectors()
    devices_data = devices()
    resources_data = resources()
    return render_template('index.html', connectors_data=connectors_data, devices_data=devices_data, resources_data=resources_data)

@app.route('/index2')
def index2():
    return render_template('index2.html')

#connectors route
@app.route('/connectors')
def api_conenctors():
    connectors_data = connectors()
    return json.dumps(connectors_data)

#devices route
@app.route('/devices')
def api_devices():
    devices_data = devices()
    return json.dumps(devices_data)

#resources route
@app.route('/resources')
def api_resources():
    resources_data = resources()
    return json.dumps(resources_data)

