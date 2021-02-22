import json
from os import path

def GenerateReport():
  fileName = ''
  name = input('Enter students full name: ')
  gradeLevel = input('Enter students grade level: ')
  semester = input('Enter which semester: ')
  subjects = tuple(input('Enter a list of subjects seperated by commas: ').split(','))

  reportCard = {"Name" : name, "Grade Level" : gradeLevel, "Semester" : semester, "Subjects" : {}}

  for i in subjects:
    Class = input(f'Enter the class name for {i}: ')
    teacher = input("Enter the teacher's name: ")
    grade = int(input('Enter the grade of the student: '))
    reportCard['Subjects'].update({'Class' : Class, "Teacher" : teacher, "Grade" : grade})
  
  
  while True:
    fileName = input('Enter the name of the file: ')
    if not path.exists(fileName):
      break
    else:
      print('Error! File already created...')
  
  with open(fileName+'.json', 'w') as file:
    json.dump(reportCard, file, indent=2)
  
  print(f'File created! Data stored under {fileName}')
