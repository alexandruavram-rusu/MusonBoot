import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Define the command handler function
def multumim_command(update: Update, context: CallbackContext):
    # Send a message
    update.message.reply_text('Multumim Cristi pentru serviciul tau!')

    # Send a picture
    photo_url = 'https://github.com/alexandruavram-rusu/MusonBoot/blob/main/pictures/multumim_cristi.jpg'
    update.message.reply_photo(photo_url)

def main():
    # Create an Updater object with your bot's token
    updater = Updater('6246555581:AAGB4Fb8B1n9656SbBO8PZ8a41smVbNbqN8')

    updater.dispatcher.add_handler(CommandHandler('multumim', multumim_command))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
