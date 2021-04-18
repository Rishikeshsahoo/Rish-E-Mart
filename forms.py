from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,ValidationError,validators
from wtforms.validators import Length, DataRequired

class item_form(FlaskForm):
    name=StringField('Item Name: ', validators=[DataRequired(),Length(min=3,max=35)])
    supplier=StringField('Supplier Name: ', validators=[DataRequired(),Length(min=3,max=20)])
    description= StringField('Description',validators=[DataRequired(),Length(min=5,max=1024)])
    price=IntegerField('Price of Item: ',validators=[DataRequired()])
    url=StringField('URL: ',validators=[DataRequired()])
    submit=SubmitField('Submit')