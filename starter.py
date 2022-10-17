from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import and_,or_

engine = create_engine("sqlite:///test.db")
Base=declarative_base()
session=sessionmaker(bind=engine)()
Base.metadata.create_all(engine)
#****************** make tables *********************
class students(Base):
	__tablename__="students"
	id=Column('id',Integer,unique=True,primary_key=True)
	name=Column('name',String(30))
class workers(Base):
	__tablename__="workers"
	id=Column('id',Integer,unique=True,primary_key=True)
	name=Column('name',String(30))
#**************************************************


#****************** select ******************

#.........select all rows.............
students=session.query(students).all()
for student in students:
	print(student.id,student.name)

#.........select single rows.............
# student=session.query(students).filter(students.name=='sina').first()
# print(student.id,student.name)

#.........select single rows.............
# student=session.query(students).filter_by(name='sina').first()
# print(student.id,student.name)

# ************************************

#****************** insert ******************

#.....insert a single row......
# student1 = students(name='sina')
# session.add(student1)
# session.commit()

#.....insert multi row......
# student2=students(name='ali')
# student3=students(name='sara')
# session.add_all([student2,student3])
# session.commit()
#*********************************************

#****************** delete **************

#.....delete a single row......
# student=student=session.query(students).filter_by(name='sina').first()
# session.delete(student)
# session.commit()

#.....delete a single row......
# session.query(students).filter_by(name='sara').delete()
# session.commit()
#****************************************


#***************** update ***************
# student=session.query(students).filter_by(name='hadi').update({'name':'hamed'})
# session.commit()

# student=student=session.query(students).filter_by(name='hamed').first()
# student.name='ehsan'
# session.commit()
#****************************************