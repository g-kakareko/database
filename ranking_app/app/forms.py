# from flask.ext.wtf import Form
from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class EventSearch(Form):
	event_name = StringField('event_name', validators=[DataRequired()])
	location = SelectField('location', 
		choices=[('tallahassee', 'Tallahassee'), ('orlando', 'Orlando')])