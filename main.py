from flask import Flask, current_app, request, jsonify
import logging
import traceback
import json
import sys

app = Flask(__name__)

@app.before_first_request
def setup_logging():
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.DEBUG)

@app.route('/', methods=['POST'])
def predict():
    data = {}
    try:
        name = request.get_json()["name"]
        
    
    except Exception:
        #print(traceback.format_exc())
        return jsonify(status_code='400', msg='Bad Request'), 400
    
    try:
        current_app.logger.info('Output: Welcome %s', name)
        #print('received_data_from ',request.form)
        return jsonify(Output="Welcome "+name)
	
    except Exception:
        print(traceback.format_exc())
        return jsonify(errorrr=traceback.format_exc())
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8585, debug=True)
