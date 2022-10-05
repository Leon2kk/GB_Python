# Семинар 9.
# Задание № 1.

# Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)
# Создайте программу для игры с конфетами человек против бота(интелект). (Дополнительно)
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования(Дополнительно)


# В консоле выполняем команду
# pip install pytelegrambotapi

import telebot;
bot = telebot.TeleBot('удалено')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    message_list = message.text.split()
    message_result = list()

    for item in message_list:
        if 'абв' not in item:
            message_result.append(item)
    
    bot.send_message(message.from_user.id,  " ".join(message_result))
    
bot.polling(none_stop=True, interval=0)