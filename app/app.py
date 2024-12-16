from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from forms import SearchItem, UploadItem
from models import app, db, Accessories, Bags, Dresses, Footwears, Skirts, Tops, Trousers

app.config['SECRET_KEY'] = 'SECRET_PROJECT'

# @app.route('/dresses/<colour>')
# def books(year):
#     dresses = Dresses.query.filter_by(colour = colour).first_or_404(description = "There is no user with this ID.")
#     emails = Reader.query.filter(Reader.email.like('%.%@%')).all()
#     return render_template('display_books.html', colour = colour, Dresses = Dresses)

@app.route('/', methods=["GET"])
@app.route('/home', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/store', methods=["GET", "POST"])
def store():
    search_item = SearchItem()
    if search_item.validate_on_submit():
        pass
    else:
        accessories = Accessories.query.limit(5).all()
        bags = Bags.query.limit(5).all()
        dresses = Dresses.query.limit(5).all()
        footwears = Footwears.query.limit(5).all()
        trousers = Trousers.query.limit(5).all()
        skirts = Skirts.query.limit(5).all()
        tops = Tops.query.limit(5).all()

        categories = {
            'accessories': accessories,
            'bags': bags,
            'dresses': dresses,
            'footwears': footwears,
            'trousers': trousers,
            'skirts': skirts,
            'tops': tops
            }

    return render_template('store.html', template_search = search_item, template_categories=categories)

@app.route('/upload', methods=["GET", "POST"])
def upload():
    upload_item = UploadItem()
    search_item = SearchItem()
    if upload_item.validate_on_submit():
        # pass
        return redirect(url_for('store', template_search=search_item, _external=True, _scheme='http'))
    return render_template('upload.html', template_upload = upload_item)


@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)
