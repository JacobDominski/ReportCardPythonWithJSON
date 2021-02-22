import json
import inputs
from os import path

def ViewReport():
  while True:
    fileName = input('Enter the name of the file: ')
    if path.exists(fileName+'.json'):
      break
    else:
      print('Error! File not found...')

  with open(fileName+'.json', 'r') as file:
    data = json.load(file)

  subjects = [*data['Subjects'].keys()]
  userData = [*data.items()]
  print()
  for i in range(3):
    print(f'{userData[i][0]} - {userData[i][1]}')

  subjectChoice = 0
  while True:

    subjectChoice = inputs.choices(subjects)

    if subjectChoice == len(subjects)+1:
      break

    subjectChoice -= 1

    Class = [*data['Subjects'][subjects[subjectChoice]].items()]

    print()
    for i in range(3):
      print(f'{Class[i][0]} - {Class[i][1]}')
