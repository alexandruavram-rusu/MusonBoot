import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from triggers import triggers  # Import the triggers from the separate file

TOKEN = '6246555581:AAGB4Fb8B1n9656SbBO8PZ8a41smVbNbqN8'
BOT_USERNAME = '@MusonulBot'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create a bot instance
bot = Bot(token=TOKEN)

# Create a dispatcher instance
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

@dispatcher.message_handler(content_types=types.ContentTypes.TEXT)
async def message_handler(message: types.Message):
    text = message.text.lower()
    chat_id = message.chat.id

    for trigger, data in triggers.items():
        if isinstance(trigger, list):
            if all(t in text for t in trigger):
                image_path = data['image_path']
                caption = data['caption']
                with open(image_path, 'rb') as photo:
                    await bot.send_photo(chat_id=chat_id, photo=photo, caption=caption)
                break

async def startup(dp):
    await bot.send_message(chat_id='@channel', text='Bot started!')

async def shutdown(dp):
    await bot.send_message(chat_id='@channel', text='Bot stopped!')
    await dp.storage.close()
    await dp.storage.wait_closed()

# Start the bot
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dispatcher, on_startup=startup, on_shutdown=shutdown)
