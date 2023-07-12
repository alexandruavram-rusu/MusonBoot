from telegram.ext import Updater, MessageHandler, Filters
from telegram import InputMediaPhoto
from triggers import triggers  # Import the triggers from the separate file



def message_handler(update, context):
    text = update.message.text.lower()
    chat_id = update.message.chat_id

    for trigger, data in triggers.items():
        if isinstance(trigger, list):
            if any(t in text for t in trigger):
                image_path = data['image_path']
                caption = data['caption']
                context.bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'), caption=caption)
                break

        
# Create an Updater object with your bot's API token
updater = Updater(token='6246555581:AAGB4Fb8B1n9656SbBO8PZ8a41smVbNbqN8', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register the message handler function
message_handler = MessageHandler(Filters.text, message_handler)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()