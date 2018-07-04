# -*- coding: utf-8 -*-
from flask import render_template
from app import my_app
from app.forms import RunnerSearch, TrainerSearch, CompetitionSearch, Ranking
# from app.ticket_scraper import get_posts
@my_app.route('/')
@my_app.route('/index')
def index():
	return render_template('index.html')
	# return '''<html><h1>Welcome to 
	# the Taylor Swift Concert Ticket-Price Showdown!</h1></html>'''


# @my_app.route('/search', methods=['GET', 'POST'])
# def search():
# 	posts = False
# 	event = 'form.event_name.data'
# 	location = 'form.location.data'
# 	dob = 'huj'
# 	form = EventSearch()
# 	if form.validate_on_submit():
# 		event = form.event_name.data
# 		location = form.location.data
# 		dob = form.start.data
# 		posts = True
# 		# posts = get_posts(event, location)
# 		# here mthod that queries database and prints the results
# 	return render_template('search.html',
# 	 title='Search for an Event', form=form, posts=posts, event=event, dob=dob,location=location)


@my_app.route('/search_runner', methods=['GET', 'POST'])
def search_runner():
	posts = False
	runner_name = 'runner_name'
	runner_dob = 'runner_dob'
	form = RunnerSearch()
	if form.validate_on_submit():
		runner_name = form.runner_name.data
		runner_dob = form.runner_dob.data
		posts = True
	return render_template('search_runner.html',
	 title='Search for a runner', form=form, posts=posts, runner_name=runner_name, runner_dob=runner_dob)


@my_app.route('/search_trainer', methods=['GET', 'POST'])
def search_trainer():
	posts = False
	trainer_name = 'trainer_name'
	trainer_dob = 'trainer_dob'
	form = TrainerSearch()
	if form.validate_on_submit():
		trainer_name = form.trainer_name.data
		trainer_dob = form.trainer_dob.data
		posts = True
	return render_template('search_trainer.html',
	 title='Search for a trainer', form=form, posts=posts, trainer_name=trainer_name, trainer_dob=trainer_dob)


@my_app.route('/search_competition', methods=['GET', 'POST'])
def search_competition():
	posts = False
	location = 'location'
	competition_date = 'competition_date'
	form = CompetitionSearch()
	if form.validate_on_submit():
		location = form.location.data
		competition_date = form.competition_date.data
		posts = True
	return render_template('search_competition.html',
	 title='Search for a competition', form=form, posts=posts, location=location, competition_date=competition_date)


@my_app.route('/ranking', methods=['GET', 'POST'])
def ranking():
	posts = False
	discipline = 'discipline'
	gender = 'gender'
	year = 'year'
	form = Ranking()
	if form.validate_on_submit():
		discipline = form.discipline.data
		gender = form.gender.data
		year = form.year.data
		posts = True
	return render_template('ranking.html',
	 title='Search for a competition', form=form, posts=posts, 
	 discipline=discipline, gender=gender, year=year)