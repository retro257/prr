import telebot
import time
import threading

# Создаем экземпляр бота
bot = telebot.TeleBot('5601989977:AAG3CWDDyv05VYdveARQd4nDL3r05giMZeY')
# Функция, обрабатывающая команду /start

def sending(m):
    while True:
        file = open("new_repo.txt", "r")
        reps = file.readlines()
        for i in reps:
            bot.send_message(m.chat.id, 'https://github.com/'+i)
        file.close()
        file = open("new_repo.txt", "w")
        file.close()
        time.sleep(3)

users = []

@bot.message_handler(commands=["start"])
def start(m, res=False):
    users.append(m)
    thread = threading.Thread(target=sending, args=(users[-1],))
        
    thread.start()
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)