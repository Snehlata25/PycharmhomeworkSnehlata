from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pprint import pprint

engine = create_engine('sqlite:////web/Sqlite-Data/example.db')

Base = declarative_base()

Base.metadata.create_all(engine)

Base.metadata.bind = engine

Session = sessionmaker(bind=engine)

session = Session()
