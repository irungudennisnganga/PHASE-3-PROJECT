#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String,Date
from sqlalchemy.orm import relationship
from .base import Base,session
from datetime import datetime

class Student(Base):
    __tablename__ = "students"

    id= Column(Integer , primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    email =Column(String)
    date_of_admission=Column(Date)
    

    
    classes=relationship("Class", back_populates="student")

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"Fist name {self.first_name}, " \
            + f"Last name {self.last_name}" \
            + f"Email {self.email}" \
            + f"Date of admission {self.date_of_admission}"       
            
    
    def create_student(self,first_name,last_name,date_of_admission):
        date_of_admission = datetime.strptime(date_of_admission, "%Y-%m-%d").date()
        new=Student(
            first_name=first_name,
            last_name=last_name,
            email=f"{first_name}{last_name}.student@schoolname.com",
            date_of_admission=date_of_admission
        )
        session.add(new)
        session.commit()
    
    def all_students(self):
        return session.query(Student).all()
    
    def update_student(self,id,first_name,last_name,date_of_admission):
        pass
        date_of_admission = datetime.strptime(date_of_admission, "%Y-%m-%d").date()
        session.query(Student).filter_by(id = id).update({
            Student.first_name :first_name,
            Student.last_name:last_name,
            Student.email:f"{first_name}{last_name}.student@schoolname.com",
            Student.date_of_admission:date_of_admission
        })
    
        session.commit()
    
        
    def delete_student(self,id):
        remove_student=  session.query(Student).filter_by(id =id).first()
        session.delete(remove_student)
        session.commit()