from httplib import OK
from flask import make_response, request
from flask.json import dumps
from yose import APP as app
from yose.prime_factors import prime_factors_of

MAX_NUMBER_VALUE = 1e6


@app.route('/primeFactors', methods=['GET'])
def power_of_two():
    numbers = extract_numbers_from_query_string()

    response = [response_for(number) for number in numbers]
    response = first_element_if_only_one(response)

    return json_response_for(response)


def first_element_if_only_one(response):
    return response[0] if len(response) == 1 else response


def extract_numbers_from_query_string():
    return request.args.getlist('number')


def json_response_for(response):
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
    return number > MAX_NUMBER_VALUE


def number_too_big_error(number):
    return {
        'number': number,
        'error': 'too big number (>1e6)'
    }