from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant import Restaurant
from models import Customer
from review import Review
from sqlalchemy.ext.declarative import declarative_base
base = declarative_base()
engine = create_engine("sqlite:///database.db")
session = sessionmaker(bind = engine)