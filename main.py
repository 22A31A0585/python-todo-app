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
    task=input("Enter your Task")
    with open("tasks.txt","a") as file:
      file.write(task+"\n")
      print("Task added successfully")
  elif choice =='2':
    print("\n Your Tasks")
    try:
      with open("tasks.txt","r") as file:
        tasks=file.readlines()
        if not tasks:
          print("No tasks Found")
        else:
          for index,task in enumerate (tasks,start=1):
            print(f"{index}.{task.strip()}")
    except FileNotFoundError:
      print("No task file found yet .add a task first")
  elif choice =='3':
    try:
      with open("tasks.txt","r") as file:
        tasks=file.readlines()
        if not tasks:
          print("no tasks to mark as completed")
        else:
          for index,task in enumerate(tasks,start=1):
            print(f"{index}.{task.strip()}")
          task_num=int(input("enter the number to mark as completed:"))

          if 1<=task_num<=len(tasks):
            tasks[task_num-1]=tasks[task_num-1].strip()+"✅\n"
            with open("tasks.txt","w") as file:
              file.writelines(tasks)
            print("✅ task marked as completed")
          else:
            print("invalid task number")
    except FileNotFoundError:
      print("Task file not found.please add tasks first")
    except ValueError:
      print("please enter a valid number")
  elif choice =='4':
    try:
      with open("tasks.txt","r") as file:
        tasks=file.readlines()
      if not tasks:
        print("No tasks to delete")
      else:
        for index,task in enumerate (tasks,start=1):
          print(f"{index}.{task.strip()}")
        task_num=int(input("enter the task number to delete"))
        if 1<=task_num <=len(tasks):
          removed_task=tasks.pop(task_num -1)
          with open("tasks.txt","w") as file:
            file.writelines(tasks)
            print(f"Deleted : {removed_task.strip()}")
        else:
          print("invalid task number")
    except FileNotFoundError:
      print("Task file not found add tasks first ")
    except ValueError:
      print("Please enter a valid number")
  elif choice=='5':
    print("Exiting the app")
    break
  else:
    print("invalid choice.Try again")