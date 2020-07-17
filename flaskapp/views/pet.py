from flask import Blueprint, render_template, redirect
from flaskapp.services import ServicePet
from flaskapp.forms import PetForm


mod = Blueprint('pet', __name__)


@mod.route('/')
def list():
    service = ServicePet()
    qs = service.list_pets()
    return render_template('pets/list.html', items=qs)


@mod.route('/create', methods=('GET', 'POST'))
def create():
    form = PetForm()
    if form.validate_on_submit():
        data = form.data
        service = ServicePet()
        service.save(data)
        return redirect('/')
    return render_template('pets/create.html', form=form)
