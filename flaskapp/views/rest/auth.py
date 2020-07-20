from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flaskapp import schemas
from flaskapp.services import ServiceUser
from flask_jwt_extended import create_access_token
from mongoengine import DoesNotExist


mod = Blueprint(
    'auth', 'auth',
    description='Access Token'
)


@mod.route('/obtain_token')
class ObtainToken(MethodView):

    @mod.arguments(schemas.LoginArgsSchema)
    @mod.response(schemas.TokenSchema, code=201)
    def post(self, data):
        """Obtain access token"""
        username = data['email']
        password = data['password']
        try:
            service = ServiceUser()
            user = service.login(username, password)
            if user:
                access_token = create_access_token(identity=username)
                token = {'access_token': access_token}
                return token
            else:
                abort(401)
        except DoesNotExist:
            abort(401)
