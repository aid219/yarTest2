
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///hackSecret.db', echo=True)

Base = declarative_base()

meta = Base.metadata
meta.create_all(engine)
session = sessionmaker(bind=engine)
