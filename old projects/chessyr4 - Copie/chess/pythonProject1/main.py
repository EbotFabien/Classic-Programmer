#from pythonProject1 import constant as keys
from telegram.ext import *
from telegram import *
from pythonProject1 import responses as r




def start_command(update, context):
    update.message.reply_text("Get started")


def help_command(update, context):
    update.message.reply_text("Let's get started")





def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main(keys):
        def handle_message(update, context,keys=keys):
            try:
                text = str(update.message.text).lower()
                print(text)
            except:
                text = str(update.message.chat.text).lower()
                print(text)
            try:
                name = str(update.message.chat.first_name)
            except:
                name = 'None'
            response = r.sample_responses(text,keys,name)
            update.message.reply_text(response)
        print("Started...")
        updater = Updater(keys, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start_command))
        dp.add_handler(CommandHandler("help", help_command))

        dp.add_error_handler(error)

        dp.add_handler(MessageHandler(Filters.text, handle_message))
        updater.start_polling()






