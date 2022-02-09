#package imports

from flask import Blueprint, flash, redirect, render_template, request, redirect, url_for

# project file imports
from car_collectors.forms import UserLoginForm
from car_collectors.models import User, db

auth = Blueprint('auth', __name__, template_folder = 'auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            # add user to db
            user = User(email, password = password)
            db.session.add(user)
            db.session.commit()

            flash(f'Congratulations! You have successfully created an account for {email}.','user-created')
            return redirect(url_for('auth.signin'))

    except:
        raise Exception('Ivalid Form Data: Please check your credentials')


    return render_template('signup.html', form=form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    return render_template('signin.html', form=form)