from sqlalchemy import *
import sqlalchemy as sql
from sqlalchemy.engine.url import URL
import pandas as pd
import datetime


def query_runner(runner_name, runner_dob=None):
    db = sql.engine.url.URL(drivername='mysql+pymysql', username='root', host='localhost', database='kakarekodb')
    metadata = MetaData(db)
    RUNNER = Table('RUNNER', metadata, autoload=True)
    TRAINER = Table('TRAINER', metadata, autoload=True)
    if runner_dob is None:
        statment = select([RUNNER, TRAINER]).where(and_(RUNNER.c.Name == runner_name , RUNNER.c.trener_id == TRAINER.c.trainer_id))
    else:
        statment = select([RUNNER, TRAINER]).where(and_(RUNNER.c.DOB == runner_dob, RUNNER.c.Name == runner_name , RUNNER.c.trener_id == TRAINER.c.trainer_id))
    engine = create_engine(db)
    df = pd.read_sql(statment, engine)
    return df 


def query_runner_results(runner_name, runner_dob=None):
    db = sql.engine.url.URL(drivername='mysql+pymysql', username='root', host='localhost', database='kakarekodb')
    metadata = MetaData(db)
    COMPETITON = Table('COMPETITON', metadata, autoload=True)
    RESULT = Table('RESULT', metadata, autoload=True)
    if runner_dob is None:
        statment = select([RESULT, COMPETITON]).where(and_(RESULT.c.Name == runner_name , RESULT.c.competition_id == COMPETITON.c.competition_id))
    else:
        statment = select([RESULT, COMPETITON]).where(and_(RESULT.c.DOB == runner_dob, RESULT.c.Name == runner_name , RESULT.c.competition_id == COMPETITON.c.competition_id))
    engine = create_engine(db)
    df = pd.read_sql(statment, engine)
#     df = df.sort_values(by=['result_id', 'date_comp'],na_position='first')
    df = df.sort_values(by=['result_id'],na_position='first')
    return df 


def query_trainer(trainer_name, trainer_dob=None):
    db = sql.engine.url.URL(drivername='mysql+pymysql', username='root', host='localhost', database='kakarekodb')
    metadata = MetaData(db)
    TRAINER = Table('TRAINER', metadata, autoload=True)
    if trainer_dob is None:
        statment = select([TRAINER]).where(and_(TRAINER.c.Name == trainer_name))
    else:
        statment = select([TRAINER]).where(and_(TRAINER.c.DOB == trainer_dob, TRAINER.c.Name == trainer_name))
    engine = create_engine(db)
    df = pd.read_sql(statment, engine)
    return df


def query_trainer_runner(trainer_name, trainer_dob=None):
    db = sql.engine.url.URL(drivername='mysql+pymysql', username='root', host='localhost', database='kakarekodb')
    metadata = MetaData(db)
    TRAINER = Table('TRAINER', metadata, autoload=True)
    RUNNER = Table('RUNNER', metadata, autoload=True)
    if trainer_dob is None:
        statment = select([RUNNER]).where(and_(TRAINER.c.Name == trainer_name, TRAINER.c.trainer_id == RUNNER.c.trener_id))
    else:
        statment = select([RUNNER]).where(and_(TRAINER.c.DOB == trainer_dob, TRAINER.c.Name == trainer_name, TRAINER.c.trainer_id == RUNNER.c.trener_id))
    engine = create_engine(db)
    df = pd.read_sql(statment, engine)
    return df


def query_stadiums_names():
    db = sql.engine.url.URL(drivername='mysql+pymysql', username='root', host='localhost', database='kakarekodb')
    metadata = MetaData(db)
#     STADION = Table('STADION', metadata, autoload=True)
    statment = 'SELECT Location FROM STADION;'
    print(statment)
    engine = create_engine(db)
    df = pd.read_sql(statment, engine)
    df = [(i, i) for i in df['Location']]
    return df


def query_comp_res(comp_loc, comp_date=None):
    db = sql.engine.url.URL(drivername='mysql+pymysql', username='root', host='localhost', database='kakarekodb')
    metadata = MetaData(db)
    COMPETITON = Table('COMPETITON', metadata, autoload=True)
    RESULT = Table('RESULT', metadata, autoload=True)
    STADION = Table('STADION', metadata, autoload=True)
    if comp_date is None:
        statment = select([RESULT]).where(and_(STADION.c.Location == comp_loc, COMPETITON.c.stadium_id == STADION.c.stadium_id,
                                              COMPETITON.c.competition_id==RESULT.c.competition_id))
    else:
        statment = select([RESULT]).where(and_(STADION.c.Location == comp_loc, COMPETITON.c.stadium_id == STADION.c.stadium_id,
                                              COMPETITON.c.date_comp==comp_date, COMPETITON.c.competition_id==RESULT.c.competition_id))
    engine = create_engine(db)
    df = pd.read_sql(statment, engine)
    
    df_100F = df[(df['discipline']=='100') & (df['gender'] == 'F')]
    df_100F = df_100F.sort_values(by=['result'],na_position='first')
    
    df_200F = df[(df['discipline']=='200') & (df['gender'] == 'F')]
    df_200F = df_200F.sort_values(by=['result'],na_position='first')
    df_400F = df[(df['discipline']=='400') & (df['gender'] == 'F')]
    df_400F = df_400F.sort_values(by=['result'],na_position='first')
    df_800F = df[(df['discipline']=='800') & (df['gender'] == 'F')]
    df_800F = df_800F.sort_values(by=['result'],na_position='first')
    df_1000F = df[(df['discipline']=='1000') & (df['gender'] == 'F')]
    df_1000F = df_1000F.sort_values(by=['result'],na_position='first') 
    df_1500F = df[(df['discipline']=='1500') & (df['gender'] == 'F')]
    df_1500F = df_1500F.sort_values(by=['result'],na_position='first')
    
    df_100M = df[(df['discipline']=='100') & (df['gender'] == 'M')]
    df_100M = df_100M.sort_values(by=['result'],na_position='first')
    df_200M = df[(df['discipline']=='200') & (df['gender'] == 'M')]
    df_200M = df_200M.sort_values(by=['result'],na_position='first')
    df_400M = df[(df['discipline']=='400') & (df['gender'] == 'M')]
    df_400M = df_400M.sort_values(by=['result'],na_position='first')
    df_800M = df[(df['discipline']=='800') & (df['gender'] == 'M')]
    df_800M = df_800M.sort_values(by=['result'],na_position='first')
    df_1000M = df[(df['discipline']=='1000') & (df['gender'] == 'M')]
    df_1000M = df_1000M.sort_values(by=['result'],na_position='first')
    df_1500M = df[(df['discipline']=='1500') & (df['gender'] == 'M')]
    df_1500M = df_1500M.sort_values(by=['result'],na_position='first')

    return df_100F, df_200F, df_400F, df_800F, df_1000F, df_1500F, df_100M, df_200M, df_400M, df_800M, df_1000M, df_1500M


def query_ranking(comp_year):
    db = sql.engine.url.URL(drivername='mysql+pymysql', username='root', host='localhost', database='kakarekodb')
    metadata = MetaData(db)

    statment = 'SELECT * FROM RESULT WHERE YEAR(date_comp) = ' + str(comp_year)
    engine = create_engine(db)
    df = pd.read_sql(statment, engine)

    df_100F = df[(df['discipline']=='100') & (df['gender'] == 'F')]
    df_100F = df_100F.sort_values(by=['result'],na_position='first')
    
    df_200F = df[(df['discipline']=='200') & (df['gender'] == 'F')]
    df_200F = df_200F.sort_values(by=['result'],na_position='first')
    df_400F = df[(df['discipline']=='400') & (df['gender'] == 'F')]
    df_400F = df_400F.sort_values(by=['result'],na_position='first')
    df_800F = df[(df['discipline']=='800') & (df['gender'] == 'F')]
    df_800F = df_800F.sort_values(by=['result'],na_position='first')
    df_1000F = df[(df['discipline']=='1000') & (df['gender'] == 'F')]
    df_1000F = df_1000F.sort_values(by=['result'],na_position='first') 
    df_1500F = df[(df['discipline']=='1500') & (df['gender'] == 'F')]
    df_1500F = df_1500F.sort_values(by=['result'],na_position='first')
    
    df_100M = df[(df['discipline']=='100') & (df['gender'] == 'M')]
    df_100M = df_100M.sort_values(by=['result'],na_position='first')
    df_200M = df[(df['discipline']=='200') & (df['gender'] == 'M')]
    df_200M = df_200M.sort_values(by=['result'],na_position='first')
    df_400M = df[(df['discipline']=='400') & (df['gender'] == 'M')]
    df_400M = df_400M.sort_values(by=['result'],na_position='first')
    df_800M = df[(df['discipline']=='800') & (df['gender'] == 'M')]
    df_800M = df_800M.sort_values(by=['result'],na_position='first')
    df_1000M = df[(df['discipline']=='1000') & (df['gender'] == 'M')]
    df_1000M = df_1000M.sort_values(by=['result'],na_position='first')
    df_1500M = df[(df['discipline']=='1500') & (df['gender'] == 'M')]
    df_1500M = df_1500M.sort_values(by=['result'],na_position='first')

    return df_100F, df_200F, df_400F, df_800F, df_1000F, df_1500F, df_100M, df_200M, df_400M, df_800M, df_1000M, df_1500M


def query_ranking_sing(comp_year, disc, gend):
    db = sql.engine.url.URL(drivername='mysql+pymysql', username='root', host='localhost', database='kakarekodb')
    metadata = MetaData(db)

    statment = """SELECT * FROM RESULT WHERE YEAR(date_comp) = '""" + str(comp_year) + """' AND discipline = '""" +  str(disc) +"""' AND gender = '""" +str(gend) + """'""" 
    print(statment)
    engine = create_engine(db)
    df = pd.read_sql(statment, engine)
    df = df.sort_values(by=['result'],na_position='first').iloc[:10]

    return df