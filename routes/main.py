from __main__ import app
from globals import *
from twingate_queries import *

# these are the html dashboard routes

# main dashboard, this is an older less dynamic version, you have to manually refresh it to see new data, all the data is pulled in as part of the render
@app.route('/')
def index():
    print(request.url + " requested")
    connectors_data = connectors()
    devices_data = devices()
    resources_data = resources()
    return render_template('index.html', connectors_data=connectors_data, devices_data=devices_data, resources_data=resources_data)

# this is a newer better version of the dashboard, really should be the only one, it uses js to dynamically build the cards using the api routes below
@app.route('/index2')
def index2():
    print(request.url + " requested")
    return render_template('index2.html')

# these are the api routes below, they just return json data not html

# connectors route
@app.route('/connectors')
def api_conenctors():
    print(request.url + " requested")
    connectors_data = connectors()
    return json.dumps(connectors_data)

# devices route
@app.route('/devices')
def api_devices():
    print(request.url + " requested")
    devices_data = devices()
    return json.dumps(devices_data)

# resources route
@app.route('/resources')
def api_resources():
    print(request.url + " requested")
    resources_data = resources()
    return json.dumps(resources_data)

# users route
@app.route('/users')
def api_users():
    print(request.url + " requested")
    users_data = users()
    return json.dumps(users_data)

# service accounts route
@app.route('/service_accounts')
def api_service_accounts():
    print(request.url + " requested")
    service_accounts_data = service_accounts()
    return json.dumps(service_accounts_data)