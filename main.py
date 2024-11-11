import sys

from data.config import REMOVE

sys.path.append('data')

from config import (
  ADDCAR,
  CHOOSEOPTION,
  ENTERCAR,
  GOODBYE,
  INVALIDINPUT,
  ISAUTHORIZED,
  MAINMENU,
  NOTAUTHORIZED,
  openDB,
  REMOVE,
  searchDB,
)

carIndexVal = 0
menuOption = 0
newCar = ""
searchFor = ""
yesOrNo = ""

while True:
  print(MAINMENU)
  try:
    menuOption = int(input(f"{CHOOSEOPTION}"))
  except Exception:
    print(INVALIDINPUT)
    continue
    
  if menuOption == 1:
    with open(openDB(), 'r') as carDB:
      print("\n" + carDB.read())
    
  elif menuOption == 2:
    searchFor = input(ENTERCAR).strip()
    if searchDB(searchFor):
      print("\n" + f"{searchFor}{ISAUTHORIZED}")
    else:
      print("\n" + f"{searchFor}{NOTAUTHORIZED}")
      
  elif menuOption == 3:
    newCar = input(ADDCAR)
    with open(openDB(), 'a') as carDB:
      carDB.write(newCar + '\n')
    print(f"\nYou have added '{newCar}' as an authorized vehicle")

  elif menuOption == 4:
    searchFor = input(REMOVE)
    if searchDB(searchFor):
      with open(openDB(), 'r') as carDB:
        carIndexVal = [line.strip() for line in carDB]
      yesOrNo = input(
        '\nAre you sure you want to remove "' + searchFor +
        '" from the authorized vehicles list? '
        )
      if yesOrNo == "yes":
        carIndexVal.remove(searchFor)
        print(f'\nYou have REMOVED "{searchFor}" as an authorized vehicle')
        with open(openDB(), 'w') as carDB:
          for vehicle in carIndexVal:
            carDB.write(vehicle + '\n')
      elif yesOrNo == "no":
        print("\nAction cancelled.")
      else:
        print("\nInvalid input. Returning to main menu...")
    else:
      print("\nVehicle not found. Returning to Main Menu")

  elif menuOption == 5:
   print(GOODBYE)
   try:
    while True:
      pass
   except KeyboardInterrupt:
    break
  
  else:
    print(INVALIDINPUT)
