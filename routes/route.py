from flask import (
    Flask,
    render_template
)

# TODO: Create the application instance
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    '''
        `home()` is a function that returns the rendered template `home.html`
        :return: The home.html file is being returned.
    '''
    return render_template('home.html')