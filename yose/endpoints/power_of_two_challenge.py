from httplib import BAD_REQUEST
from flask import make_response, jsonify, request
from yose import APP as app
from yose.prime_factors import prime_factors_of

BIGGEST_SUPPORTED_NUMBER = 1e6


@app.route('/primeFactors', methods=['GET'])
def power_of_two():
    number = request.args.get('number')

    if not is_a_number(number):
        return not_a_number_error(number)
    elif number_is_too_big(int(number)):
        return number_too_big_error(number)
    else:
        return prime_factors_response(int(number))


def prime_factors_response(number):
    return make_response(jsonify({
        'number': number,
        'decomposition': prime_factors_of(number),
    }))


def is_a_number(s):
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


def number_is_too_big(number):
    return number > BIGGEST_SUPPORTED_NUMBER


def number_too_big_error(number):
    return make_response(jsonify({
        'number': number,
        'error': 'too big number (>1e6)'
    }), BAD_REQUEST)


