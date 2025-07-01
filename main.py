def show_menu():
  print("TO-DO LIST")
  print("1.Add a new task")
  print("2. view all the task")
  print("3. Mark task as complete")
  print("4.Delete a task")
  print("5.Exit")

  while True:
    show_menu()
    choice=input("Enter your  choice (1-5)")

    if choice =='1':
      pass
    elif choice =='2':
      pass
    elif choice =='3':
      pass
    elif choice =='4':
      pass
    elif choice=='5':
      print("Exiting the app")
    else:
      print("invalid choice.Try again")