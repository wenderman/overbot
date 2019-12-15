import telebot
 
bot = telebot.TeleBot('1019609885:AAH6GOdb30vBJO8EmpkZViTjPNLAMI-WuhY')

aid = 321225997
 
#начало диалога
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, ' + str(message.from_user.first_name) + '!' + '\n' + 'Отправь мне свой вопрос, администрация попробует на него ответить :)\n\nНаш канал @overlamer1')
    bot.send_message(aid, "Здравствуйте, Владелец!\n\nЭто ваш личный бот, который получает вопросы от пользователей.\n\nСтатус:\nСервер - PAW\nРабота: отличная")

@bot.message_handler(commands=['test'])
def testing(message):
	bot.send_message(message.chat.id, "БОТ работает отлично!")

#параметры аргументов команды /quest
def extract_arg(arg):
    return arg.split()[1]
def extract_arg1(arg):
    return arg.split(maxsplit=2)[2]

@bot.message_handler(commands=['quest'])
def quest(message):
    id = extract_arg(message.text)
    text = extract_arg1(message.text)
    check = (message.from_user.id)
    if check != aid:
        bot.send_message(message.chat.id, 'Вы не являетесь администратором!')
    else:
        bot.send_message(id, 'Ответ поддержки:' '\n\n' + text)
        bot.send_message(aid, 'Пользователю дошел ответ!')

@bot.message_handler(content_types=["text"])
def text(message):
    bot.send_message(aid, 'Сообщение от ' +  str(message.from_user.first_name) + '(' + str(message.from_user.id) + ')' + ':\n' + message.text + '\n' + 'Для ответа используйте :' + '\n' + '/send ' + str(message.from_user.id) + ' [TEXT]')
    bot.send_message(message.chat.id, 'Сообщение отправлено администратору, ожидайте!')

bot.polling(True)