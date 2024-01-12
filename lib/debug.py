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


@click.command(help="Add new student")
@click.option('--first_name',required=True,prompt="Enter first name") 
@click.option('--last_name',required=True,prompt="Enter last name") 
@click.option('--date_of_admission',required=True, prompt="Enter date of admission")

def new_student(first_name,last_name,date_of_admission):
    student.create_student(first_name,last_name ,date_of_admission)       
all_methods.add_command(new_student)

@click.command(help="Update student")
@click.option('--id',required=True,prompt="Enter Student id ") 
@click.option('--first_name',required=True,prompt="Enter first name ") 
@click.option('--last_name',required=True,prompt="Enter last name ") 
@click.option('--date_of_admission',required=True, prompt="Enter date of admission ")

def update_student_info(id,first_name,last_name,date_of_admission):
    student.update_student(id,first_name,last_name,date_of_admission)

all_methods.add_command(update_student_info)

@click.command(help='Delete student')
@click.option('--id',required=True,prompt="Enter Student id ") 
def del_student(id):
    student.delete_student(id)
all_methods.add_command(del_student)   
  
  
    
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

@click.command(help="Update Teacher")
@click.option('--id',required=True,prompt="Enter Teacher id ") 
@click.option('--first_name',required=True,prompt="Enter first name ") 
@click.option('--last_name',required=True,prompt="Enter last name ") 
@click.option('--subject',required=True, prompt="Enter subject ")

def update_teacher_info(id,first_name,last_name,subject):
    student.update_student(id,first_name,last_name,subject)

all_methods.add_command(update_teacher_info)

@click.command(help='Delete Teacher')
@click.option('--id',required=True,prompt="Enter Teacher id ") 
def del_teacher(id):
    teacher.delete_teacher(id)
all_methods.add_command(del_teacher)   


# CLASS METHODS
@click.command(help="New class")
def new_class():
    classes.create_class('103',2,4)
all_methods.add_command(new_class)  

@click.command(help="Filter by class")
@click.option('--name',required=True,prompt="Enter Class name ") 
def filter_by_class(name):
    click.echo(classes.filter_by_class(name))

all_methods.add_command(filter_by_class)

@click.command(help="Update Class ")
@click.option('--id',required=True,prompt="Enter Class id ") 
@click.option('--name',required=True,prompt="Enter Class name ") 
@click.option('--teachers_id',required=True,prompt="Enter teachers id ") 
@click.option('--students_id',required=True,prompt="Enter students id ") 


def update_classes_info(id,name,teachers_id,students_id):
    classes.update_class_details(id,name,teachers_id,students_id)

all_methods.add_command(update_classes_info)

@click.command(help='Delete Class')
@click.option('--id',required=True,prompt="Enter Class id ") 
def del_classes(id):
    classes.delete_class(id)
all_methods.add_command(del_classes)



if __name__ == '__main__':
    all_methods()