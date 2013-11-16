from httplib import BAD_REQUEST
from flask import make_response, jsonify, request
from yose import APP as app
from yose.prime_factors import prime_factors_of


@app.route('/primeFactors', methods=['GET'])
def power_of_two():
    number = request.args.get('number')

    if not a_number(number):
        return not_a_number_error(number)
    else:
        return prime_factors_response(int(number))


def a_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def not_a_number_error(number):
    return make_response(jsonify({
        'number': number,
        'error': 'not a number'
    }), BAD_REQUEST)


def prime_factors_response(number):
    return make_response(jsonify({
        'number': number,
        'decomposition': prime_factors_of(number)
    }))