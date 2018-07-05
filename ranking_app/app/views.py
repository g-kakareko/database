# -*- coding: utf-8 -*-
from flask import render_template
from app import my_app
from app.forms import RunnerSearch, TrainerSearch, CompetitionSearch, Ranking
import pandas as pd
import app.db as db
# from app.ticket_scraper import get_posts
@my_app.route('/')
@my_app.route('/index')
def index():
	return render_template('index.html')


@my_app.route('/search_runner', methods=['GET', 'POST'])
def search_runner():
	posts = False
	runner_name = 'runner_name'
	runner_dob = 'runner_dob'
	df_runner = pd.DataFrame()
	df_result = pd.DataFrame()
	form = RunnerSearch()
	if form.validate_on_submit():
		runner_name = form.runner_name.data
		runner_dob = form.runner_dob.data
		df_runner = db.query_runner(runner_name=runner_name, runner_dob=runner_dob)
		df_result = db.query_runner_results(runner_name=runner_name, runner_dob=runner_dob)

		posts = True
	return render_template('search_runner.html',
	 title='Search for a runner', form=form, posts=posts, 
	 runner_name=runner_name, runner_dob=runner_dob, 
	 tables=[df_runner.to_html(classes='table1'), df_result.to_html(classes='table2')],
	  titles = ['na', 'Runner', 'Results'])


@my_app.route('/search_trainer', methods=['GET', 'POST'])
def search_trainer():
	posts = False
	trainer_name = 'trainer_name'
	trainer_dob = 'trainer_dob'
	form = TrainerSearch()
	df_trainer = pd.DataFrame()
	df_trainer_run = pd.DataFrame()
	if form.validate_on_submit():
		trainer_name = form.trainer_name.data
		trainer_dob = form.trainer_dob.data

		df_trainer = db.query_trainer(trainer_name=trainer_name, trainer_dob=trainer_dob)
		df_trainer_run = db.query_trainer_runner(trainer_name=trainer_name, trainer_dob=trainer_dob)

		posts = True
	return render_template('search_trainer.html',
	 title='Search for a trainer', form=form, posts=posts, trainer_name=trainer_name, 
	 trainer_dob=trainer_dob, tables=[df_trainer.to_html(classes='table1'), df_trainer_run.to_html(classes='table2')],
	  titles = ['na', 'Trainer', 'Trained runners'])


@my_app.route('/search_competition', methods=['GET', 'POST'])
def search_competition():
	posts = False
	location = 'location'
	competition_date = 'competition_date'
	form = CompetitionSearch()
	df_100F = pd.DataFrame()
	df_200F = pd.DataFrame()
	df_400F = pd.DataFrame()
	df_800F = pd.DataFrame()
	df_1000F = pd.DataFrame()
	df_1500F = pd.DataFrame()
	df_100M = pd.DataFrame()
	df_200M = pd.DataFrame()
	df_400M = pd.DataFrame()
	df_800M = pd.DataFrame()
	df_1000M = pd.DataFrame()
	df_1500M= pd.DataFrame()
	if form.validate_on_submit():
		location = form.location.data
		competition_date = form.competition_date.data
		(df_100F, df_200F, df_400F, df_800F, df_1000F, 
		df_1500F, df_100M, df_200M, df_400M, df_800M, 
		df_1000M, df_1500M) = db.query_comp_res(comp_loc=location, comp_date=competition_date)
		posts = True
	return render_template('search_competition.html',
	 title='Search for a competition', form=form, posts=posts, 
	 location=location, competition_date=competition_date,
	 tables=[df_100F.to_html(classes='table2'), 
	 df_200F.to_html(classes='table2'),
	 df_400F.to_html(classes='table2'),
	 df_800F.to_html(classes='table2'),
	 df_1500F.to_html(classes='table2'),
	 df_100M.to_html(classes='table2'),
	 df_200M.to_html(classes='table2'),
	 df_400M.to_html(classes='table2'),
	 df_800M.to_html(classes='table2'),
	 df_1000M.to_html(classes='table2'),
	 df_1500M.to_html(classes='table2')
	 	], titles = ['na', '100F', '200F',
	 	 '400F','800F', '1000F', '1500F',
	 	 '100M','200M','400M','800M','1000M','1500M'])


@my_app.route('/ranking', methods=['GET', 'POST'])
def ranking():
	posts = False
	discipline = 'discipline'
	gender = 'gender'
	year = 'year'
	form = Ranking()
	df_ranking = pd.DataFrame()

	if form.validate_on_submit():
		discipline = form.discipline.data
		gender = form.gender.data
		year = form.year.data
		df_ranking = db.query_ranking_sing(comp_year=year, disc=discipline, gend=gender)
		posts = True
	return render_template('ranking.html',
	 title='Search for a competition', form=form, posts=posts, 
	 discipline=discipline, gender=gender, year=year,
	 tables=[df_ranking.to_html(classes='table1')],
	  titles = ['na', 'Ranking'])

