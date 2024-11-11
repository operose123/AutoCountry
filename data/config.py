def openDB():
  return ('data/car_db.txt')

def searchDB(searchFor):
  with open('data/car_db.txt', 'r') as carDB:
    carIndexVal = [line.strip() for line in carDB]
    return searchFor in carIndexVal

ADDCAR = (
"\nPlease Enter the full Vehicle name you would like to add: "
)

AUTHCARS = (
"\nThe AutoCountry sales manager has authorized the purchase \
and selling of the following vehicles:\n"
)

CHOOSEOPTION = "\nPlease enter a number to select an option: "

ENTERCAR = "\nPlease enter the full vehicle name: "

GOODBYE = (
"\nThank you for using the AutoCountry Vehicle Finder, \
good-bye! Press Ctrl+C to end program.\n"
)

INVALIDINPUT = "\nInvalid input.\n"

ISAUTHORIZED = " is an authorized vehicle"

MAINMENU = """
********************************
AutoCountry Vehicle Finder v0.4
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit

********************************
"""

NOTAUTHORIZED = (
" is NOT an authorized vehicle, if you received this in error \
please check the spelling and try again"
)

REMOVE = "\nPlease Enter the full Vehicle name you would like to REMOVE: "