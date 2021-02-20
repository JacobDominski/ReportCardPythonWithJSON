import GenerateReport
import ViewReport
import ModifyReport

while True:
  choice = 0
  while choice < 1 or choice > 4:
    print('1. Create a Report Card\n2. View a Report Card\n3. Modify a Report Card\n4. Quit')
    try:
      choice = int(input('Enter a number: '))
    except(ValueError):
      print('Error not a number!')
  
  if choice == 4:
    break
  
  if choice == 1:
    GenerateReport.GenerateReport()
    
  elif choice == 2:
    ViewReport.ViewReport()
    
  elif choice == 3:
    ModifyReport.ModifyReport()
