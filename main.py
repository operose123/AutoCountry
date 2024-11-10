import sys

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
)

carIndexVal = 0
menuOption = 0
newCar = ""
searchFor = ""

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
    with open(openDB(), 'r') as carDB:
      carIndexVal = [line.strip() for line in carDB]
      searchFor = input(ENTERCAR).strip()
      if searchFor in carIndexVal:
        print("\n" + f"{searchFor}{ISAUTHORIZED}")
      else:
        print("\n" + f"{searchFor}{NOTAUTHORIZED}")
      
  elif menuOption == 3:
    newCar = input(ADDCAR)
    with open(openDB(), 'a') as carDB:
      carDB.write(newCar + '\n')
    print(f"\nYou have added '{newCar}' as an authorized vehicle")

  elif menuOption == 4:
   print(GOODBYE)
   try:
    while True:
      pass
   except KeyboardInterrupt:
    break
  
  else:
    print(INVALIDINPUT)
