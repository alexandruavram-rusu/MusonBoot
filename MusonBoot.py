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
    

def inspirational_command(update: Update, context: CallbackContext):
    photo_url = 'https://i.imgur.com/iryNRGD.jpg'
    caption = 'TRUE WORDS'
    media = InputMediaPhoto(photo_url, caption=caption)
    update.message.reply_media_group([media])
    
def nepotu_command(update: Update, context: CallbackContext):
    photo_url = 'https://i.imgur.com/N5hBCiC.jpg'
    caption = 'Where nepotu?'
    media = InputMediaPhoto(photo_url, caption=caption)
    update.message.reply_media_group([media])
    
def relansare_economica_command(update: Update, conext: CallbackContext):
    photo_url = 'https://i.imgur.com/vRpmIsl.jpg'
    caption = 'Planul de relansare economica'
    media = InputMediaPhoto(photo_url, caption=caption)
    update.message.reply_media_group([media])
    

def main():
    # Create an Updater object with your bot's token
    updater = Updater('6246555581:AAGB4Fb8B1n9656SbBO8PZ8a41smVbNbqN8')

    updater.dispatcher.add_handler(CommandHandler('multumim', multumim_command))
    updater.dispatcher.add_handler(CommandHandler('inspirational', inspirational_command))
    updater.dispatcher.add_handler(CommandHandler('nepotu', nepotu_command))
    updater.dispatcher.add_handler(CommandHandler('relansare_economica', relansare_economica_command))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
