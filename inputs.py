def choices(lst):
  choice = 0
  while choice < 1 or choice > len(lst)+1:
    for i in range(len(lst)):
      print(f'{i+1}. {lst[i]}')
    print(f'{len(lst)+1}. Quit')

    try:
      choice = int(input('select a number: '))
    except (ValueError):
      print('Error! Enter a number!')
  
  return choice
