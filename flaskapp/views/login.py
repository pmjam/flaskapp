from flask import Blueprint, render_template, redirect, url_for
from flaskapp.services import ServiceUser
from flaskapp.forms import LoginForm


mod = Blueprint('login', __name__)


@mod.route('/login', methods=["GET", "POST"])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        service = ServiceUser()
        if service.login(form.email.data, form.password.data):
            return redirect(url_for('pet.create'))
    return render_template('login/signin.html', form=form)


@mod.route('/logout', methods=["GET"])
def signout():
    service = ServiceUser()
    service.logout()
    return redirect(url_for('login.signin'))
