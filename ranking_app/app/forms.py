# from flask.ext.wtf import Form
from flask_wtf import Form
from wtforms import StringField, SelectField,SubmitField
# , DateField
from wtforms.validators import DataRequired
from wtforms import validators
from wtforms.fields.html5 import DateField
import app.db as db

from flask import url_for, redirect, render_template
from flask_wtf import Form
from flask_wtf.file import FileField
from werkzeug import secure_filename

# class EventSearch(Form):
# 	event_name = StringField('event_name', validators=[DataRequired()])
# 	location = SelectField('location', 
# 		choices=[('tallahassee', 'Tallahassee'), ('orlando', 'Orlando')])
# 	start = DateField('Plan Start', validators=[DataRequired()])


class RunnerSearch(Form):
	runner_name = StringField('runner_name', validators=[DataRequired()])
	# runner_dob = DateField('runner_dob', validators=[DataRequired()])
	runner_dob = DateField('runner_dob', validators=[DataRequired()])
	delete_form = SubmitField()


class TrainerSearch(Form):
	trainer_name = StringField('trainer_name', validators=[DataRequired()])
	trainer_dob = DateField('trainer_dob', validators=[DataRequired()])
	delete_form = SubmitField()


class CompetitionSearch(Form):
	locations = db.query_stadiums_names() 
	location = SelectField('location',
	        choices=locations,
	        validators=[DataRequired()])
	# location = StringField('location', validators=[DataRequired()])
	competition_date = DateField('competition_date', validators=[DataRequired()])
	delete_form = SubmitField()


class Ranking(Form):
	discipline = SelectField('discipline', 
		choices=[('100', '100'), ('200', '200'), ('400', '400'), ('800', '800'),
		('1000', '1000'), ('1500', '1500')]
		)
	gender = SelectField('gender', 
		choices=[('M', 'Male'), ('F', 'Female')])
	# year = DateField('competition_date', format="%Y",validators=[DataRequired()])
	# years = [('2001', '2001') ,('2000', '2000')]
	years = [(str(i), str(i)) for i in range(2010,2019)]
	year = SelectField('discipline',
	        choices=years,
	        validators=[DataRequired()])


# class PhotoForm(FlaskForm):
#     photo = FileField(validators=[FileRequired()])

class UploadForm(Form):
    file = FileField()


class delete(Form):
	delete_form = SubmitField()