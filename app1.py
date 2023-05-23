from flask import Flask, render_template
'''from forms import RegistrationForm, LoginForm'''

'''app.config['SECRET_KEY'] = '9dc2caabe707156fda66b0ceeabda3ff' '''
app = Flask(__name__)
"""app.register_blueprint(views)"""
@app.route('/')
def home():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

"""
@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)
"""

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')