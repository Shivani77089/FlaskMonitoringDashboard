from flask import Flask
from datetime import time
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask-Monitoring-Dashboard tutorial'


@app.route('/endpoint1')
def endpoint1():
    time.sleep(0.20)
    return 'Endpoint1', 400


@app.route('/endpoint2')
def endpoint2():
    time.sleep(5)
    return 'Endpoint2'

app.run(debug=True)
