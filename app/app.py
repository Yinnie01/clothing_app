from flask import Flask, request, render_template, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

from forms import SearchItem, UploadItem
from models import app, db, Accessories, Bags, Dresses, Footwears, Skirts, Tops, Trousers
from helper import get_items, upload_items

app.config['SECRET_KEY'] = 'SECRET_PROJECT'

@app.route('/', methods=["GET"])
@app.route('/home', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/store', methods=["GET", "POST"])
def store():
    search_item = SearchItem()

    if search_item.validate_on_submit() and search_item.description.data:
        input_word = search_item.description.data.strip().lower()
    else:
        input_word = None

    categories = {
        'accessories': get_items(Accessories, input_word),
        'bags': get_items(Bags, input_word),
        'dresses': get_items(Dresses, input_word),
        'footwears': get_items(Footwears, input_word),
        'trousers': get_items(Trousers, input_word),
        'skirts': get_items(Skirts, input_word),
        'tops': get_items(Tops, input_word)
    }
    # if the search returns no items render 404.html
    if all(not items for items in categories.values()):
        return render_template("404.html")
    return render_template('store.html', template_search=search_item, template_categories=categories)

@app.route('/upload', methods=["GET", "POST"])
def upload():
    upload_item = UploadItem()
    search_item = SearchItem()
    if upload_item.validate_on_submit():
        upload_category = upload_item.category.data
        upload_type = upload_item.type.data.lower()
        upload_designer = upload_item.designer.data.lower()
        upload_colour = upload_item.colour.data.lower()
        upload_description = upload_item.description.data.lower()
        upload_price = upload_item.price.data.lower()


        upload_items(upload_category,upload_type,upload_designer,upload_colour,upload_description,upload_price)

        return redirect(url_for('upload'))
    return render_template('upload.html', template_upload=upload_item)

@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)
