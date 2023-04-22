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