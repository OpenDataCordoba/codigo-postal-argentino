from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql:///cpa")

Base = declarative_base()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()
