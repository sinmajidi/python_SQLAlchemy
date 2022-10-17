from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

engine = create_engine("sqlite:///test.db")
Base=declarative_base()

class students(Base):
	__tablename__="students"
	id=Column('id',Integer,unique=True,primary_key=True)
	name=Column('name',String(30))
class workers(Base):
	__tablename__="workers"
	id=Column('id',Integer,unique=True,primary_key=True)
	name=Column('name',String(30))

Base.metadata.create_all(engine)