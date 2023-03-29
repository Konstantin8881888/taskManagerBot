import telebot
import random

token = "Your Token"

HELP = """
/help - Напечатать справку.
/add, /todo - Добавить задачу в список.
/print, /show - Напечатать все задачи.
/random - Добавить случайную задачу на сегодня."""
RANDOM_TASKS = ["Поработать с кодом.", "Сходить в бассейн.", "Погулять на улице.", "Позаниматься спортом.", "Посмотреть лекции.", "Почитать книгу."]
tasks = {}

def appendInDict(date, task):
  if date in tasks:
      tasks[date].append(task)
  else:
      tasks[date] = [task]

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add", "todo"])
def add(message):
    splCommand = message.text.split(maxsplit=2)
    date = splCommand[1].lower()
    task = splCommand[2]
    if len(task) < 3:
        mess = "Задача слишком короткая!"
    else:
        appendInDict(date, task)
        mess = ("Добавлена задача: " + task + " на дату: " + date)
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=["show", "print"])
def showPrint(message):
    splCommand = message.text.lower().split()
    splCommand.pop(0)
    mess = "Такой даты нет в задачах!"
    # date = splCommand[1]
    for date in splCommand:
         date
         if date in tasks:
            mess = date.upper() + ":\n"
            for task in tasks[date]:
              mess = mess + "- " + task + "\n"
         bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=["random"])
def randomAdd(message):
    task = random.choice(RANDOM_TASKS)
    appendInDict("сегодня", task)
    mess = ("Добавлена задача: " + task + " на дату: Сегодня")
    bot.send_message(message.chat.id, mess)

bot.polling(none_stop=True)