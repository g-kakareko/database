# -*- coding: utf-8 -*-
from flask import render_template
from app import my_app
from app.forms import EventSearch
# from app.ticket_scraper import get_posts
@my_app.route('/')
@my_app.route('/index')
def index():
	return render_template('index.html')
	# return '''<html><h1>Welcome to 
	# the Taylor Swift Concert Ticket-Price Showdown!</h1></html>'''


@my_app.route('/search', methods=['GET', 'POST'])
def search():
	posts = False
	event = 'form.event_name.data'
	location = 'form.location.data'
	form = EventSearch()
	if form.validate_on_submit():
		event = form.event_name.data
		location = form.location.data
		posts = True
		# posts = get_posts(event, location)
		# here mthod that queries database and prints the results
	return render_template('search.html',
	 title='Search for an Event', form=form, posts=posts, event=event, location=location)