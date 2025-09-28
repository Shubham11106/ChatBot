import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os


load_dotenv()
API_TOKEN=os.getenv("TOKEN")
#print(API_TOKEN)

#configure logging
logging.basicConfig(level=logging.INFO)

bot=Bot(token= API_TOKEN)
dp= Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.message):
    await message.reply(f"Hello! I'm a bot created with aiogram.")


@dp.message_handler( )
async def echo(message: types.message):
    await message.answer( message.text)



if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)


