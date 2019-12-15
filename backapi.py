import telebot
 
bot = telebot.TeleBot('Тут могло быть ваше порно')
 
#начало диалога
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, ' + str(message.from_user.first_name) + '!' + '\n' + 'Это бот обратной связи, который может получить твой вопрос и передать администрации Lamerland.')
 
#параметры аргументов команды /send
def extract_arg(arg):
    return arg.split()[1]
def extract_arg1(arg):
    return arg.split(maxsplit=2)[2]

@bot.message_handler(commands=['send'])
def send(message):
    id = extract_arg(message.text)
    text = extract_arg1(message.text)
    check = (message.from_user.id)
    if check != 1037451240:
        bot.send_message(message.chat.id, 'Вы не являетесь администратором!')
    else:
        bot.send_message(id, 'Ответ поддержки:' '\n\n' + text)
        #оповещениеоо успешной отправке ответа
        bot.send_message(1037451240, 'Пользователю дошел ответ!')

@bot.message_handler(content_types=["text"])
def text(message):
    bot.send_message(1037451240, 'Сообщение от ' +  str(message.from_user.first_name) + '(' + str(message.from_user.id) + ')' + ':\n' + message.text + '\n' + 'Для ответа используйте :' + '\n' + '/send ' + str(message.from_user.id) + ' [TEXT]')
    bot.send_message(message.chat.id, 'Сообщение отправлено администратору, ожидайте!')
 
bot.polling(True)