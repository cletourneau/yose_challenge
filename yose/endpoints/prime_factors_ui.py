from flask import render_template, request
from yose import APP as app
from yose.prime_factors import prime_factors_of


@app.route('/primeFactors/ui', methods=['GET', 'POST'])
def display_form():
    return render_template('primeFactorsForm.jade')
