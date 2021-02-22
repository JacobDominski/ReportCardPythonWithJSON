import json
import inputs
from os import path, listdir, getcwd
from os.path import isfile, join

def ModifyReport():

  allFiles = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f)) and f.endswith(".json")]
  while True:
    print('\nall files\n')
    for i in allFiles:
      print(i)
    fileName = input('Enter the name of the file (without the extension): ')
    if path.exists(fileName+'.json'):
      break
    else:
      print('Error! File not found...')
  
  file = open(fileName+'.json', 'r+')
  ReportCardData = json.load(file)

  data1 = [*ReportCardData.keys()]

  while True:
    choice = inputs.choices(data1)
      
    if choice == len(data1)+1:
      json.dump(fileName+".json", ReportCardData, indent=2)
      file.close()
      print('\nModification Complete\n')
      return
    
    choice -= 1

    if data1[choice] == "Subjects":
      subjectChoice = inputs.choices(['Add a subject', 'Subtract a subject', 'Alter a subject'])

      if subjectChoice == 4:
        print('\nModification Complete\n')

      if subjectChoice == 1:
        ReportCardData['Subjects'].update(addSubject())
      
      elif subjectChoice == 2:
        ReportCardData['Subjects'].update(subSubject())

      elif subjectChoice == 3:
        ReportCardData['Subjects'].update(modSubject())
      
    else:
      newData = input(f'Enter new {data1[choice]}')
      ReportCardData[data1[choice]] = newData

def addSubject():
  subkey = input('Enter the subject: ')
  classval = input('Enter the class name: ')
  teachername = input("Enter the teacher's name: ")
  grade = input('Enter the grade: ')

  subdict = {{"Class" : classval}, {"Teacher" : teachername}, {"Grade" : grade}}

  return {subkey : subdict}

def subSubject():
  subkey = input('Enter the subject you want to delete: ')
  

def modSubject(data):
  pass
