import telebot as tb
from requests import exceptions as requests_exc
from datetime import datetime

with open('TOKEN.txt') as token_file:
    token = token_file.read()

bot = tb.TeleBot(token, threaded=False)
bot_user = bot.get_me().username


def passed_time(date):
    dtime = datetime.now() - date
    return f"Прошло с отправки:\n{dtime}"


@bot.message_handler(commands=['ftime'])
def command_ftime(message):
    try:
        ts = message.reply_to_message.forward_date
        date = datetime.fromtimestamp(ts)
    except AttributeError:
        bot.reply_to(message, 'Ответь на пересланное сообщение')
    else:
        bot.reply_to(message, f'Дата отправки:\n{date}\n{passed_time(date)}')


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()
