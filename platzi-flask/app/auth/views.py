from flask import render_template, session, redirect, url_for
from . import auth
from app.forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': LoginForm(),
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Username successfully registered.')

        return redirect(url_for('index'))

    return render_template('login.html', **context)