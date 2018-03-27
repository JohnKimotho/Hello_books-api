from flask_api import FlaskAPI

from config import app_config

def create_app(config_name):
	app = FlaskAPI(__name__, instance _relative config=True )
	app.config.from _object(app_config[config_name])
	app_config[config_name].init_app(app)
	
	return app