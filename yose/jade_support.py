def add_jade_support(app):
    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
