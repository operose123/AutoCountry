allowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
optionSelection = 0
vehicleToSearch = ""
vehicleIndexNumber = 0
authorizedVehicleMessage = "\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:\n" 
optionSelectionPrompt = "Please enter 1, 2 or 3 to select an option: "
vehicleSearchPrompt = "\nPlease enter the full vehicle name: "
authorizedVehicleFound = " is an authorized vehicle"
authorizedVehicleNotFound = " is not an authorized vehicle, if you received this in error please check the spelling and try again"
inputErrorMessage = "\nInvalid input.\n"
exitMessage = "\nThank you for using the AutoCountry Vehicle Finder, good-bye! Press Ctrl+C to end program.\n"
mainMenu = """********************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. Exit
"""  
while True:
  print(mainMenu)
  try:
    optionSelection = int(input(f"{optionSelectionPrompt}"))
  except:
    print(inputErrorMessage)
    continue
  if optionSelection == 1:
    print(authorizedVehicleMessage)
    for vehicle in allowedVehiclesList:
      print(vehicle + "\n")
  elif optionSelection == 2:
    vehicleToSearch = input(vehicleSearchPrompt)
    try:
      vehicleIndexNumber = allowedVehiclesList.index(vehicleToSearch)
      print(f"\n{vehicleToSearch}{authorizedVehicleFound}\n")
    except ValueError:
      print(f"\n{vehicleToSearch}{authorizedVehicleNotFound}\n")
  elif optionSelection == 3:
    print(exitMessage)
    try:
      while True:
        pass
    except KeyboardInterrupt:
      break
  else:
    print(inputErrorMessage)
