HELP = """
help - напечатать справку по программе.
add/todo - добавить задачу в список (название задачи запрашиваем у пользователя).
print/show - напечатать все добавленные задачи."""

tasks = []
today = []
tomorrow = []
other = {}

while(True):
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "add" or command == "todo":
    task = input("Введите название задачи: ")
    date = input("Введите дату выполнения задачи: ")
    if date == "today":
      today.append(task)
    elif date == "tomorrow":
      tomorrow.append(task)
    else:
      other[task] = date
    # tasks.append(task)
    print("Добавлена задача:", task, "на дату:", date)
  elif command == "exit":
    print("Работа программы завершена.")
    break
  elif command == "show" or command == "print":
    print("Задачи на сегодня:", today, "Задачи на завтра:", tomorrow, "Другие задачи:", other)
  else:
   print("Нет такой команды!")