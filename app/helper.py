
from models import app, db, Accessories, Bags, Dresses, Footwears, Skirts, Tops, Trousers

from sqlalchemy import or_


categories = {
    'Accessories': Accessories,
    'Bags': Bags,
    'Dresses': Dresses,
    'Footwears': Footwears,
    'Trousers': Trousers,
    'Skirts': Skirts,
    'Tops': Tops
    }

def find_clothing_item(model, input_word):
    pattern = f"%{input_word}%"

    results = model.query.filter(or_(
                                            model.type.like(pattern),
                                            model.designer.like(pattern),
                                            model.description.like(pattern),
                                            model.colour.like(pattern)
                                                                            )).all()
    
    return results

def get_items(model, input_word=None):
    if input_word:
        return find_clothing_item(model, input_word)
    return model.query.limit(5).all()


def upload_items(upload_category,upload_type,upload_designer,upload_colour,upload_description,upload_price):
    new_item = categories[upload_category](type = upload_type,
                            designer = upload_designer,
                            colour = upload_colour,
                            description = upload_description,
                            price = upload_price)
    db.session.add(new_item)
    try:
        db.session.commit()
    except:
        db.session.rollback()

