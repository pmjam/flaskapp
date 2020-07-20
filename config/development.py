SECRET_KEY = 'development key'
DEBUG = True
API_TITLE = 'My API'
API_VERSION = 'v1'
OPENAPI_VERSION = '3.0.2'
OPENAPI_URL_PREFIX = '/api'
OPENAPI_SWAGGER_UI_PATH = '/swagger'
OPENAPI_SWAGGER_UI_URL = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/'
API_SPEC_OPTIONS = {
    'security': [{"bearerAuth": []}],
    'components': {
        "securitySchemes":
            {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
            }
    }
}

MONGODB_SETTINGS = {
    'db': 'dbflaskapp',
    'host': 'localhost',
    'port': 27017,
    'username': 'test',
    'password': ''
}
