import os
from flask import Flask
from links import link
from admin import admin
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = SECRET_KEY

jwt = JWTManager(app)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config['PROPAGATE_EXCEPTIONS'] = True

app.config["JWT_TOKEN_LOCATION"] = ['cookies']

app.register_blueprint(link.link_bp)

app.register_blueprint(admin.admin_bp)

app.run(debug=True)