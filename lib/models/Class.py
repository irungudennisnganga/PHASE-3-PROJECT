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
    
    # create a new instance of the class relationship to add a student to class and identify the teacher and also give the student a class
    
    # 
            