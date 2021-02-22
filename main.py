# imports all the files for the different choices
import GenerateReport
import ViewReport
import ModifyReport

# runs forever until the user chooses to quit
while True:
  # creates user choice variable
  choice = 0
  # if the user did not choose one of the choices it asks the user again
  while choice < 1 or choice > 4:
    # displays the menu to the user
    print('1. Create a Report Card\n2. View a Report Card\n3. Modify a Report Card\n4. Quit')
    # trys to turn the user input into an integer
    try:
      # attempts to cast the input to an integer
      choice = int(input('Enter a number: '))
    # if failed from a value error
    except(ValueError):
      # the input was not a number
      print('Error not a number!')
  
  # if the user chose to quit
  if choice == 4:
    # breaks out of the loop ending the program
    break
  
  # if the user chose the first option
  if choice == 1:
    # calls the generate report function
    GenerateReport.GenerateReport()
    
  # if the user chose the second option
  elif choice == 2:
    # calls the view report function
    ViewReport.ViewReport()
    
  # if the user chose the third option
  elif choice == 3:
    # calls the modify report function
    ModifyReport.ModifyReport()
