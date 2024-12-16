from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite://")

# Create a session factory bound to the engine
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Yinnie/Desktop/SOFTWARE DEVELOPMENT/CODECADEMY/Learn Flask/clothing recommendation project/app/clothing_store.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

table_list = ['Accessories', 'Bags', 'Dresses', 'Footwears', 'Skirts', 'Tops', 'Trousers']

class Accessories(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    type = db.Column(db.String(80), unique = False, nullable = False)
    designer = db.Column(db.String(80), unique = False, nullable = False)
    description = db.Column(db.String(80), unique = False, nullable = False)
    colour = db.Column(db.String(80), unique = False, nullable = False)
    price = db.Column(db.Float, unique = False, nullable = False)

class Bags(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    type = db.Column(db.String(80), unique = False, nullable = False)
    designer = db.Column(db.String(80), unique = False, nullable = False)
    description = db.Column(db.String(80), unique = False, nullable = False)
    colour = db.Column(db.String(80), unique = False, nullable = False)
    price = db.Column(db.Float, unique = False, nullable = False)

class Dresses(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    type = db.Column(db.String(80), unique = False, nullable = False)
    designer = db.Column(db.String(80), unique = False, nullable = False)
    description = db.Column(db.String(80), unique = False, nullable = False)
    colour = db.Column(db.String(80), unique = False, nullable = False)
    price = db.Column(db.Float, unique = False, nullable = False)

class Footwears(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    type = db.Column(db.String(80), unique = False, nullable = False)
    designer = db.Column(db.String(80), unique = False, nullable = False)
    description = db.Column(db.String(80), unique = False, nullable = False)
    colour = db.Column(db.String(80), unique = False, nullable = False)
    price = db.Column(db.Float, unique = False, nullable = False)

class Skirts(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    type = db.Column(db.String(80), unique = False, nullable = False)
    designer = db.Column(db.String(80), unique = False, nullable = False)
    description = db.Column(db.String(80), unique = False, nullable = False)
    colour = db.Column(db.String(80), unique = False, nullable = False)
    price = db.Column(db.Float, unique = False, nullable = False)

class Tops(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    type = db.Column(db.String(80), unique = False, nullable = False)
    designer = db.Column(db.String(80), unique = False, nullable = False)
    description = db.Column(db.String(80), unique = False, nullable = False)
    colour = db.Column(db.String(80), unique = False, nullable = False)
    price = db.Column(db.Float, unique = False, nullable = False)

class Trousers(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    type = db.Column(db.String(80), unique = False, nullable = False)
    designer = db.Column(db.String(80), unique = False, nullable = False)
    description = db.Column(db.String(80), unique = False, nullable = False)
    colour = db.Column(db.String(80), unique = False, nullable = False)
    price = db.Column(db.Float, unique = False, nullable = False)


if __name__ == "__main__":
    with app.app_context():
        trousers = Accessories.query.all()
        print(trousers)

        for trouser in trousers:
            print(trouser.type)
    



