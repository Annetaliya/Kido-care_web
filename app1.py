from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '9dc2caabe707156fda66b0ceeabda3ff'
"""app.register_blueprint(views)"""
@app.route('/')
def home():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@kido.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check username and password', 'danger')


    return render_template('login.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')