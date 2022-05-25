import helperV1, helperV2

choice = 0
while choice < 1 or choice >2:
  try:
    choice = int(input("Choose a version to play\n1. New\n2. Old\n"))
  except:
    print("Invalid Input")
if choice ==1:
  helperV2.menu()
if choice ==2:
  helperV1.menu()