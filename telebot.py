from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from openai import OpenAI  # NEW IMPORT
import sys


class Reference:
    def __init__(self) -> None:
        self.response = ""


load_dotenv()

# NEW DEEPSEEK CLIENT SETUP
client = OpenAI(
    api_key=os.getenv("Deepseek_API_Key"),
    base_url="https://api.deepseek.com"  # DeepSeek endpoint
)

reference = Reference()
TOKEN = os.getenv("TOKEN")
MODEL_NAME = "deepseek-chat"

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


def clear_past():
    reference.response = ""


@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Hi! I'm TeleBot! Powered by DeepSeek AI and create by Shubham Maurya. How can I assist you?")


@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    clear_past()
    await message.reply("I've cleared the past conversation and context.")


@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    help_command = """
    Hi There, I'm DeepSeek Telegram bot! Commands:
    /start - Start conversation
    /clear - Clear conversation history
    /help - Show this help
    """
    await message.reply(help_command)


@dispatcher.message_handler()
async def deepseek_chat(message: types.Message):
    print(f">>> USER: \n\t{message.text}")
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": reference.response},
            {"role": "user", "content": message.text}
        ]
    )
     
        
    reference.response = response.choices[0].message.content
    print(f">>> DeepSeek: \n\t{reference.response}")
    await bot.send_message(chat_id=message.chat.id, text=reference.response)

     

if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=False)