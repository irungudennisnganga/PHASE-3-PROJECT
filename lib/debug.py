#!/usr/bin/env python3
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Class import Class
from models.Student import Student
from models.Teacher import Teacher

student=Student()
classes=Class()
teacher=Teacher()

@click.group()
def all_methods():
    pass


@click.command(help='Find all students')
def students():
    click.echo(student.all_students())
all_methods.add_command(students)

@click.command(help="Add new student") 
# @click.option(--"first_name",last_name,email,date_of_admission)
def new_student():
    student.create_student('dennis','irungu','dennis@gmail.com' ,'2024-4-22')
       
       
all_methods.add_command(new_student)

@click.command(help="All teacher")
def teachers():
    click.echo(teacher.all_teachers())
all_methods.add_command(teachers)

  
if __name__ == '__main__':
    all_methods()