"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings
from datetime import datetime
from telegram.ext import Updater


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def get_date():
    return str(datetime.now().date()).replace('-','/')

# def get_planetlist ():
#     list_planets = []
#     for i in ephem._libastro.builtin_planets():
#         list_planets.append(i[-1])
#     return list_planets


# def talk_to_me(update, context):
#     user_text = update.message.text
#     print(user_text)
#     update.message.reply_text(user_text)

def constellation_info(update, context):
    user_text = update.message.text.split()[-1]
    print(user_text)
    print(f'Планета {user_text} в созвездии:')
    program = f'update.message.reply_text(ephem.constellation(ephem.{user_text}(get_date())))'
    exec(program)
    # update.message.reply_text(ephem.constellation(ephem.Mars(get_date())))

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

# def constellation_info(update, context):
#     # print(f'Вызван {update.message.text}')
#     planet = update.message.text.split()[-1]
#     print(planet)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellation_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
