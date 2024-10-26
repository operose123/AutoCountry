optionSelection = 0
allowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
authorizedVehicleMessage = "\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:\n" 

inputPrompt = "Please enter 1 or 2 to select an option: "
inputErrorMessage = "\nInvalid input.\n"
exitMessage = "\nThank you for using the AutoCountry Vehicle Finder, good-bye! Press Ctrl+C to end program.\n"
mainMenu = """********************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. Exit

"""
while True:
  print(mainMenu)
  try:
    optionSelection = int(input(f"{inputPrompt}"))
  except:
    print(inputErrorMessage)
    continue
  if optionSelection == 1:
    print(authorizedVehicleMessage)
    for vehicle in allowedVehiclesList:
      print(vehicle + "\n")
  elif optionSelection == 2:
    print(exitMessage)
    try:
      while True:
        pass
    except KeyboardInterrupt:
      break
  else:
    print(inputErrorMessage)
