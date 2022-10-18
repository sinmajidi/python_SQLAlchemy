from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.sql.expression import and_,or_

engine = create_engine("sqlite:///relation.db")
Base=declarative_base()
session=sessionmaker(bind=engine)()
#****************** make tables *********************
class student(Base):
	__tablename__="student"
	id=Column('id',Integer,unique=True,primary_key=True)
	name=Column('name',String(30))
	classroom_id=Column('ClassRoom_id',Integer,ForeignKey('ClassRoom.id'))
class ClassRoom(Base):
	__tablename__="ClassRoom"
	id=Column('id',Integer,unique=True,primary_key=True)
	name=Column('name',String(30))
	students=relationship('student',backref='ClassRoom')
Base.metadata.create_all(engine)


#******************* insert *******************************
# classs=session.query(ClassRoom).filter_by(name='class1').first()
# session.add(classs)
# session.commit()
# student1 = student(name='hamed',ClassRoom=classs)
# session.add(student1)
# session.commit()

#*******************************************************
#******************* select *******************************
students=session.query(student).all()
for student in students:
	print(student.id,student.name,student.classroom_id)


classes=session.query(ClassRoom).all()
for clas in classes:
	print(clas.id,clas.name)

classs=session.query(ClassRoom).filter_by(name='class1').first()
for student in classs.students:
	print(student.name," is in class1")

#*******************************************************