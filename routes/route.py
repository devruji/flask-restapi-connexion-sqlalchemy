import connexion

from flask import render_template

# TODO: Create the application instance
app = connexion.App(__name__, specification_dir='../')

@app.route('/')
def home():
    '''
        `home()` is a function that returns the rendered template `home.html`
        :return: The home.html file is being returned.
    '''
    return render_template('home.html')