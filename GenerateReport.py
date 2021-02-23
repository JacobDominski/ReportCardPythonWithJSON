# imports json for storing data
import json
# imports path for checking if a file exists
from os import path

# function to create report cards and insert info
def GenerateReport():
  # variable to store name of file
  fileName = ''
  # gets students name, grade level, semester, and list of subjects
  name = input('Enter students full name: ')
  gradeLevel = input('Enter students grade level: ')
  semester = input('Enter which semester: ')
  subjects = tuple(input('Enter a list of subjects seperated by commas: ').split(','))
  # puts all data into a dictionary
  reportCard = {"Name" : name, "Grade Level" : gradeLevel, "Semester" : semester, "Subjects" : {}}
  # gets the class teacher and grade for each subject and adds it to the dictionary
  for i in subjects:
    Class = input(f'Enter the class name for {i}: ')
    teacher = input("Enter the teacher's name: ")
    grade = int(input('Enter the grade of the student: '))
    reportCard['Subjects'].update({'Class' : Class, "Teacher" : teacher, "Grade" : grade})
  
  # gets the user input for the file name
  while True:
    # get the file name
    fileName = input('Enter the name of the file: ')
    # check if the file name exists
    if not path.exists(fileName):
      # if not then exit the loop
      break
     # if not display error to the user
    else:
      print('Error! File already created...')
  
  # open the file as a json file
  with open(fileName+'.json', 'w') as file:
    # add all the data inside the json file
    json.dump(reportCard, file, indent=2)
  
  # let the user know the data has been stored
  print(f'File created! Data stored under {fileName}')
