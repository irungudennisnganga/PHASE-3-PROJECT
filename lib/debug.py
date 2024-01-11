#!/usr/bin/env python3
import click
from models.Class import Class
from models.Student import Student
from models.Teacher import Teacher

student=Student()
classes=Class()
teacher=Teacher()

@click.group()
def all_methods():
    pass

# STUDENTS METHODS
@click.command(help='Find all students')
def students():
    click.echo(student.all_students())
all_methods.add_command(students)

@click.command(help='Student full names')
def students_name():
    click.echo(student.full_name())
all_methods.add_command(students_name)

@click.command(help="Add new student")
@click.option('--first_name',required=True,prompt="Enter first name") 
@click.option('--last_name',required=True,prompt="Enter last name") 
@click.option('--date_of_admission',required=True, prompt="Enter date of admission")

def new_student(first_name,last_name,date_of_admission):
    student.create_student(first_name,last_name ,date_of_admission)       
all_methods.add_command(new_student)



# TEACHERS METHODS
@click.command(help="All teacher")
def teachers():
    click.echo(teacher.all_teachers())
all_methods.add_command(teachers)

@click.command(help='Add new teacher')
@click.option('--first_name',required=True,prompt="Enter first name")
@click.option('--last_name',required=True,prompt="Enter last name")
@click.option('--subject',required=True,prompt="Enter subject")

def new_teacher(first_name,last_name,subject):
    teacher.create_teacher(first_name,last_name,subject)  
all_methods.add_command(new_teacher)  



# CLASS METHODS
@click.command(help="New class")
def new_class():
    classes.create_class('103',2,4)
all_methods.add_command(new_class)  

@click.command(help="Filter by class")
def filter_by_class():
    click.echo(classes.filter_by_class('103'))

all_methods.add_command(filter_by_class)





if __name__ == '__main__':
    all_methods()