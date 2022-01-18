from telegram import *
from telegram.ext import *


bot = Bot('1791911591:AAGJMfo7jnrr7Jtl1Xg8sYjMRKEQhkbqA3E')

#print(bot.get_me())
updater =Updater("1791911591:AAGJMfo7jnrr7Jtl1Xg8sYjMRKEQhkbqA3E",use_context=True)

dispatcher = updater.dispatcher

def test_function(update:Update , context:CallbackContext):
    print(update)
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi "+update.effective_chat.last_name+" This is the tutorial link : https://www.youtube.com/watch?v=81znEpRT0_s"
        )

start_value=CommandHandler('chesliefilm',test_function)

dispatcher.add_handler(start_value)

def test_function2(update:Update , context:CallbackContext):
    print(update)
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi "+update.effective_chat.last_name+",please how can we help you,leave a message for cheslie?"
        )

start_value1=CommandHandler('hello',test_function2)

dispatcher.add_handler(start_value1)

def test_function3(update:Update , context:CallbackContext):
    print(update)
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Good morning "+update.effective_chat.last_name+",please how can we help you,leave a message for cheslie?"
        )

start_value2=CommandHandler('goodmorning',test_function3)

dispatcher.add_handler(start_value2)

updater.start_polling()
