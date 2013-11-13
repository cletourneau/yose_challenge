from flask import make_response, jsonify
from yose import APP as app

@app.route('/ping', methods=['GET'])
def alive():
    response = make_response(jsonify({'alive': True}))
    return response