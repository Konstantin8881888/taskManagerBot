HELP = """
help - Напечатать справку по программе.
add/todo - Добавить задачу в список.
print/show - Напечатать все задачи.
random - Добавить случайную задачу на сегодня."""

RANDOM_TASK = "Поработать с кодом."
tasks = {}
today = []
# tomorrow = []
# other = {}

def appendInDict(date, task):
  if date in tasks:
      tasks[date].append(task)
  else: 
      tasks[date] = [task]
  print("Добавлена задача:", task, "на дату:", date)
  return tasks

while(True):
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "add" or command == "todo":
    task = input("Введите название задачи: ")
    date = input("Введите дату выполнения задачи: ")
    
    # if date in tasks:
    #   tasks[date].append(task)
    # else: 
    #   tasks[date] = [task]
    appendInDict(date, task)
    
    # if date == "today":
    #   today.append(task)
    # elif date == "tomorrow":
    #   tomorrow.append(task)
    # else:
    #   other[task] = date
    
  elif command == "exit":
    print("Работа программы завершена.")
    break
  elif command == "show" or command == "print":
    # print(tasks, "Задачи на сегодня:", today, "Задачи на завтра:", tomorrow, "Другие задачи:", other)
    date = input("Введите дату для отображения списка задач: ")
    if date in tasks:
      for task in tasks[date]:
        print(date, "-", task)
    else:
      print("Такой даты нет в задачах!")
  elif command == "random":
    # if "today" in tasks:
    #   tasks["today"].append(RANDOM_TASK)
    # else:
    #   tasks["today"] = [RANDOM_TASK]
    appendInDict("today", RANDOM_TASK)
  else:
   print("Нет такой команды!")