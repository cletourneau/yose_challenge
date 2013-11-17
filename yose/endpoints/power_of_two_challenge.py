from httplib import OK
from flask import make_response, request
from flask.json import dumps
from yose import APP as app
from yose.prime_factors import prime_factors_of

BIGGEST_SUPPORTED_NUMBER = 1e6


@app.route('/primeFactors', methods=['GET'])
def power_of_two():
    query_string_numbers = request.args.getlist('number')
    response = [response_for(number) for number in query_string_numbers]

    if len(response) == 1:
        response = response[0]

    return make_response(dumps(response), OK, {'content-type': 'application/json'})


def response_for(number):
    if not is_a_number(number):
        return not_a_number_error(number)
    elif number_is_too_big(int(number)):
        return number_too_big_error(number)
    else:
        return prime_factor_response_for(int(number))


def prime_factor_response_for(number):
    return {
        'number': number,
        'decomposition': prime_factors_of(number),
    }


def is_a_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def not_a_number_error(number):
    return {
        'number': number,
        'error': 'not a number'
    }


def number_is_too_big(number):
    return number > BIGGEST_SUPPORTED_NUMBER


def number_too_big_error(number):
    return {
        'number': number,
        'error': 'too big number (>1e6)'
    }


