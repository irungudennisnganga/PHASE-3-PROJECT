#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String,ForeignKey,Date
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
    # classes = relationship("Class", lazy="dynamic")
    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.first_name}, " \
            + f"{self.last_name}" \
            + f"Email {self.email}" \
            + f"Date of admission {self.date_of_admission}"       
            
    def full_name(self):
        return f"{self.first_name} {self.last_name}"   
    def create_student(self,first_name,last_name,email,date_of_admission):
        date_of_admission = datetime.strptime(date_of_admission, "%Y-%m-%d").date()
        new=Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_admission=date_of_admission
        )
        session.add(new)
        session.commit()
    def create_email(self):
        return f"{self.first_name}{self.last_name}@gmail.com"     
     
    def all_students(self):
        return session.query(Student).all()
        