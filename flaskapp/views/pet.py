from flask import Blueprint, render_template
from flaskapp.services import ServicePet


mod = Blueprint('pet', __name__)


@mod.route('/')
def index():
    service = ServicePet()
    qs = service.list_pets()
    return render_template('list.html', items=qs)
