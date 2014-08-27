#! -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
    # return create_engine(URL(**settings.DATABASE))
    return create_engine("mysql://root:root@127.0.0.1:3306/douban_movie")


def create_movies_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class Movies(DeclarativeBase):
    __tablename__ = "movies"
    
    id       = Column(Integer, primary_key=True)
    title_cn = Column('title_cn', String)
    title_en = Column('title_en', String, nullable=True)