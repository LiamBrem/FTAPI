from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://liambrem:pass@localhost:5432/ft"
app.config["SECRET_KEY"] = "secret"
db = SQLAlchemy(app)

migrate = Migrate(app, db)
