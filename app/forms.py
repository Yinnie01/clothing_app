from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class FieldsRequiredForm(FlaskForm):
    """Require radio fields to have content. This works around the bug that WTForms radio fields don't honor the `DataRequired` or 
    `InputRequired` validators."""
    class Meta:
        def render_field(self, field, render_kw):
            if field.type == "_Option":
                render_kw.setdefault("required", True)
            return super().render_field(field, render_kw)

class SearchItem(FlaskForm):
    description = StringField("", render_kw={"placeholder": "Search for items and brands"}, validators=[DataRequired()])
    submit = SubmitField("Search")

class UploadItem(FieldsRequiredForm):
    clothing_category = [("Accessories", "Accessories"), ("Bags", "Bags"), ("Dresses", "Dresses"),
                         ("Footwears", "Footwears"), ("Skirts", "Skirts"), ("Tops", "Tops"),("Trousers", "Trousers")]
    category = RadioField("Category of clothing", choices=clothing_category)
    type = StringField("Clothing Type", validators=[DataRequired()])
    designer = StringField("Designer", validators=[DataRequired()])
    colour = StringField("Colour of clothing", validators=[DataRequired()])
    description = TextAreaField("Clothing Description", validators=[DataRequired()])
    price = StringField("Price ($)", validators=[DataRequired()])
    submit = SubmitField("Upload Item")
