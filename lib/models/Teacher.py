#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base,session

class Teacher(Base):
    __tablename__ = "teachers"

    id= Column(Integer , primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    subject=Column(String)
    email =Column(String,)
    
    
    classes=relationship("Class" ,back_populates="teacher")
    
    def __repr__(self):
        return f"Teacher {self.id}: " \
            + f"First name{self.first_name}, " \
            + f"Last name {self.last_name}" \
            +  f"Subject {self.subject}" \
            +  f"Email {self.email}" 
            
    def all_teachers(self):
        return session.query(Teacher).all()        
        

    def create_teacher(self,first_name,last_name,subject):
       new=Teacher(
           first_name=first_name,
           last_name=last_name,
           subject=subject,
           email=f"{first_name}{last_name}.teacher@schoolname.com"
       )  
       session.add(new)       
       session.commit()
    
    def update_teacher(self,id,first_name,last_name,subject):
        session.query(Teacher).filter_by(id = id).update({
            Teacher.first_name :first_name,
            Teacher.last_name:last_name,
            Teacher.subject: subject,
            Teacher.email:f"{first_name}{last_name}.teacher@schoolname.com",
            
        })
    
        session.commit()
    
        
    def delete_teacher(self,id):
        remove_teacher=  session.query(Teacher).filter_by(id =id).first()
        session.delete(remove_teacher)
        session.commit()