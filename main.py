import helperV1, helperV2

choice = 0
while choice < 1 or choice >3:
  try:
    choice = int(input("Choose a version to play\n1. New\n2. Old\n3. Exit\n"))
  except:
    print("Invalid Input")
if choice ==1:
  helperV2.menu()
elif choice ==2:
  helperV1.menu()
elif choice ==3:
  pass