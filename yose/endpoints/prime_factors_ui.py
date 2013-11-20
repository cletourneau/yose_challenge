from flask import render_template, request
from yose import APP as app
from yose.prime_factors import prime_factors_of


@app.route('/primeFactors/ui', methods=['GET', 'POST'])
def display_form():
    if request.method == 'POST':
        number = request.form['number']
        prime_factors = prime_factors_of(int(number))
        result = "{number} = {factors}".format(number=number, factors=' x '.join([str(p) for p in prime_factors]))
        return render_template('primeFactorsForm.jade', result=result)
    return render_template('primeFactorsForm.jade')
