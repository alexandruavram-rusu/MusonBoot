import logging
from telegram import Update, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Define the command handler function
def multumim_command(update: Update, context: CallbackContext):
    # Send a message
    # update.message.reply_text('Multumim Cristi pentru serviciul tau!')

    # Send a picture
    photo_url = 'https://i.imgur.com/AsrxH00.jpg'
    caption = 'Multumim Cristi pentru serviciul tau!'
    media = InputMediaPhoto(photo_url, caption=caption)
    update.message.reply_media_group([media])
    

def inspirational(update: Update, context: CallbackContext):
    photo_url = 'https://i.imgur.com/03l3sLO.jpg'
    caption = 'TRUE LEADERS'
    media = InputMediaPhoto(photo_url, caption=caption)
    update.message.reply_media_group([media])
    

def main():
    # Create an Updater object with your bot's token
    updater = Updater('6246555581:AAGB4Fb8B1n9656SbBO8PZ8a41smVbNbqN8')

    updater.dispatcher.add_handler(CommandHandler('multumim', multumim_command))
    updater.dispatcher.add_handler(CommandHandler('inspirational', multumim_command))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
