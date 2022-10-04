from urllib import response
from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/status")
def healthCheck():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info("status request successful")
    return response

@app.route("/metrics")
def metrics():
  response = app.response_class(
          response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
          status=200,
          mimetype='application/json'
  )
  app.logger.info("metrics request successful")
  return response

@app.route("/")
def hello():
    # Logging a CUSTOM message
    app.logger.info('Main request successfull')
    return "Hello World!"
    
if __name__ == "__main__":
    # Stream logs to a file, and set the default log level to DEBUG
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    # logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S', filename='app.log')
    # logging.basicConfig(
    #     format='%(asctime)s %(levelname)-8s %(message)s',
    #     level=logging.INFO,
    #     datefmt='%Y-%m-%d %H:%M:%S')
    app.run(host='0.0.0.0')
