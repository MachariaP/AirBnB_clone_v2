#!/usr/bin/ env python3


from sqlalchemy import create_engine
from models import Base  # assuming your BaseModel class is defined in a models.py script

# setup the database engine
engine = create_engine('mysql+pymysql://username:password@localhost/dbname')

# create all tables in the database which don't exist yet
Base.metadata.create_all(engine)
