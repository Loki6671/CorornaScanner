import telebot
from telebot import types
list=[]
bot = telebot.TeleBot('1796607232:AAGGmADNw9ObvNsGXQR8ZzQ0rW3J-etOw_M')
keyboard1 = telebot.types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('/geo')
itembtn2 = types.KeyboardButton('/number')
itembtn3 = types.KeyboardButton('/status')
keyboard1.add(itembtn1, itembtn2, itembtn3)
close_keyboard = telebot.types.ReplyKeyboardRemove(0)
@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.send_message(message.chat.id, 'Здравствуй, ' + message.from_user.first_name, reply_markup = keyboard1)


@bot.message_handler(commands=["geo"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)

@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        bot.send_message(message.chat.id,
                         'Благодарим,' + message.from_user.first_name + '  можете отправить номер. ',
                         reply_markup=keyboard1)
        print(message.location)
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))



@bot.message_handler(commands=['number'])  # Объявили ветку для работы по команде <strong>number</strong>
def phone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)  # Подключаем клавиатуру
    button_phone = types.KeyboardButton(text="Отправить телефон",
                                        request_contact=True)  # Указываем название кнопки, которая появится у пользователя
    keyboard.add(button_phone)  # Добавляем эту кнопку

    bot.send_message(message.chat.id, 'Номер телефона',
                     reply_markup=keyboard)  # Дублируем сообщением о том, что пользователь сейчас отправит боту свой номер телефона (на всякий случай, но это не обязательно)


@bot.message_handler(content_types=[
    'contact'])  # Объявили ветку, в которой прописываем логику на тот случай, если пользователь решит прислать номер телефона :)
def contact(message):
    if message.contact is not None:  # Если присланный объект <strong>contact</strong> не равен нулю



        print(message.contact)
        bot.send_message(message.chat.id, 'Благодарим,'+message.from_user.first_name+'  можете отправить геолакацию. ' , reply_markup = keyboard1)
        # Выводим у себя в панели контактные данные. А вообщем можно их, например, сохранить или сделать что-то еще
@bot.message_handler(commands=['status'])  # Объявили ветку для работы по команде <strong>number</strong>
def status(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)  # Подключаем клавиатуру
    button1 = types.KeyboardButton(text="Заржен")  # Указываем название кнопки, которая появится у пользователя
    button2 = types.KeyboardButton(text="Вакцинирован")  # Указываем название кнопки, которая появится у пользователя
    button3 = types.KeyboardButton(text="Невакцинированный ")  # Указываем название кнопки, которая появится у пользователя
    button4=types.KeyboardButton(text="Назад")

    keyboard.add(button1, button2, button3, button4)  # Добавляем эту кнопку


    bot.send_message(message.chat.id, 'Ваш статус на данный момент',
                     reply_markup=keyboard)  # Дублируем сообщением о том, что пользователь сейчас отправит боту свой номер телефона (на всякий случай, но это не обязательно)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text is not  None and message.text!='Назад':

        print(message.text)
        bot.send_message(message.chat.id, 'Благодарим,'+message.from_user.first_name+'  можете отправить геолакацию. ' , reply_markup = keyboard1)

    elif message.text=='Назад':
        bot.send_message(message.chat.id, "Не забудьте позже подтвердить свой статус", reply_markup = keyboard1 )
bot.polling()