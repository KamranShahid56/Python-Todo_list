Todo = []

def addtask():
  task=input('Enter Task: ')
  Todo.append(task)
  print(f"Task '{task}' added")

def alltasks():
   if len(Todo)==0:
     print('No Tasks Currently')
   else:
     for i in range(len(Todo)):
       print(f"{i+1}. {Todo[i]}")

def removetask():
  alltasks()
  try:
     delete=int(input('Enter task number to delete: '))
     if delete>0 and delete<=len(Todo):
        Todo.pop(delete)
        print(f"Task no.{delete} deleted")
     else:
        print(f"Task no.{delete} not found")
  except:
    print('Invalid input')

if __name__ == "__main__":
   print('Welcome to Todo List App')
   while True:
      print('\n')
      print('------------------------')
      print('Please select one of the options: ')
      print('1. Add a task')
      print('2. Remove a task')
      print('3. View all tasks')
      print('4. Exit')
      print('\n')

      choice = int(input('Enter your choice: '))
      if (choice==1):
         addtask()
      elif (choice==2):
         removetask()
      elif (choice==3):
         alltasks()
      elif (choice==4):
         break
      else:
         print('Invalid choice')
         print('\nPlease try again')
   print('Goodbye 👋👋')
        
