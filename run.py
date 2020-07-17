import os
from flaskapp import create_app

os.environ['APP_CONFIG_FILE'] = '../config/development.py'
app = create_app()
app.run()
