#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from .base import Base,session

class Class(Base):
    __tablename__='classes'

    id=Column(Integer, primary_key=True)
    name=Column(String)
    
    teachers_id=Column(Integer ,ForeignKey("teachers.id"))
    students_id=Column(Integer, ForeignKey("students.id"))
    
    student=relationship("Student" , back_populates="classes")
    teacher=relationship("Teacher", back_populates="classes")
    
    def __repr__(self):
        return f"class {self.id}: " \
            + f"{self.name}, " 
            
    # query student based on a specific  class they belong ( include filtering)
    def filter_by_class(self,class_name):
        return session.query(Class.name,Class.teachers_id,Class.students_id).filter_by(name = class_name).all()
    
    # create a new instance of the class relationship to add a student to class and identify the teacher and also give the student a class
    def create_class(self,name,teachers_id,students_id):
        new=Class(
            name=name,
            teachers_id=teachers_id,
            students_id=students_id
        )
        session.add(new)
        session.commit()
    
    # delete method 
    def update_class_details(self,id,name,teachers_id,students_id):
        session.query(Class).filter_by(id = id).update({
            Class.name :name,
            Class.teachers_id:teachers_id,
            Class.students_id: students_id,
        })
    
        session.commit()
    
    def delete_class(self,id):
        remove_student_from_class=  session.query(Class).filter_by(id =id).first()
        session.delete(remove_student_from_class)
        session.commit()
            