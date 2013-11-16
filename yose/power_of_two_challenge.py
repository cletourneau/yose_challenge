from flask import make_response, jsonify, request
from yose import APP as app
from yose.prime_factors import prime_factors_of


@app.route('/primeFactors', methods=['GET'])
def power_of_two():
    number = int(request.args.get('number'))
    return make_response(jsonify({
        'number': number,
        'decomposition': (prime_factors_of(number))
    }))