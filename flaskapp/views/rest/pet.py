from flask.views import MethodView
from flask_smorest import Blueprint
from flaskapp import schemas
from flask_jwt_extended import jwt_required
from flaskapp.services import ServicePet


mod = Blueprint(
    'pets', 'pets',
    description='Operations on pets'
)


@mod.route('/')
class Pets(MethodView):

    @mod.arguments(schemas.PetQueryArgsSchema, location='query')
    @mod.response(schemas.PetSchema(many=True))
    @jwt_required
    def get(self, args):
        """List pets"""
        service = ServicePet()
        qs = service.list(**args)
        return qs

    @mod.arguments(schemas.PetSchema)
    @mod.response(schemas.PetSchema, code=201)
    @jwt_required
    def post(self, data):
        """Add a new pet"""
        service = ServicePet()
        item = service.save(data)
        return item
