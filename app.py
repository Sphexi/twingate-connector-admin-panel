# app launcher, sets a basic error handler and runs waitress

# import from the globals file
from globals import *


# start flask
app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())

# setup error handling, http errors return a json body with details all others a generic 500
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return make_response({"message":str(e)}, e.code)
    print(traceback.format_exc())
    return make_response({"error":"a server side error occurred, please go check the logs"},500)

import routes.main


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000, threads=10)