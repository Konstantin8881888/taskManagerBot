import random

HELP = """
/help - Напечатать справку по программе.
/add, /todo - Добавить задачу в список.
/print, /show - Напечатать все задачи.
/random - Добавить случайную задачу на сегодня.
/exit - Выход из программы"""

RANDOM_TASKS = ["Поработать с кодом.", "Сходить в бассейн.", "Погулять на улице.", "Позаниматься спортом.", "Посмотреть лекции.", "Почитать книгу."]
tasks = {}

def appendInDict(date, task):
  if date in tasks:
      tasks[date].append(task)
  else: 
      tasks[date] = [task]
  print("Добавлена задача:", task, "на дату:", date)
  
while(True):
  command = input("Введите команду: ")
  if command == "/help":
    print(HELP)
  elif command == "/add" or command == "/todo":
    task = input("Введите название задачи: ")
    date = input("Введите дату выполнения задачи: ")
    appendInDict(date, task)
  elif command == "/exit":
    print("Работа программы завершена.")
    break
  elif command == "/show" or command == "/print":
    date = input("Введите дату для отображения списка задач: ")
    if date in tasks:
      for task in tasks[date]:
        print(date, "-", task)
    else:
      print("Такой даты нет в задачах!")
  elif command == "/random":
    task = random.choice(RANDOM_TASKS)
    appendInDict("today", task)
  else:
   print("Нет такой команды!")