from flask import Blueprint, render_template, redirect
from flaskapp.services import ServicePet
from flaskapp.forms import PetForm


mod = Blueprint('pet', __name__)


@mod.route('/')
def list():
    service = ServicePet()
    qs = service.list()
    return render_template('pets/list.html', items=qs)


@mod.route('/create', methods=('GET', 'POST'))
def create():
    form = PetForm()
    if form.validate_on_submit():
        data = form.data
        service = ServicePet()
        service.create(data)
        return redirect('/')
    return render_template('pets/add.html', form=form)


@mod.route('/<id>/update', methods=('GET', 'POST'))
def update(id):
    service = ServicePet()
    obj = service.get(id)

    form = PetForm(obj=obj)
    if form.validate_on_submit():
        data = form.data
        service.update(obj, data)
        return redirect('/')
    return render_template('pets/edit.html', form=form)


@mod.route('/<id>/delete', methods=('GET',))
def delete(id):
    service = ServicePet()
    obj = service.get(id)
    service.delete(obj)
    return redirect('/')
