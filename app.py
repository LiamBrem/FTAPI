from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://liambrem:pass@localhost:5432/ft"
db = SQLAlchemy(app)