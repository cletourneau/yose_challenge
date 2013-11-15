from flask import make_response, jsonify
from yose import APP as app

@app.route('/primeFactors', methods=['GET'])
def power_of_two():
    response = make_response(jsonify({
        'number': 16,
        'decomposition': [2, 2, 2, 2]
    }))
    return response