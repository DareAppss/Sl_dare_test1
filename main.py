from aiogram import Bot, Dispatcher, executor, types
import webdriver

bot = Bot(token='key')
dp = Dispatcher(bot)





@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    user_name = message.from_user.first_name if message.from_user.first_name else "there"
    start_text = (
        f"Hello, {user_name}!\n"
        "I'm Gunther Bot, here to assist you.\n"
        "Here are some things you can do:\n"
        "- /subscribe: Subscribe to my YT channel\n"
        "- /about: Learn more about me\n"
        "- /help: Get help and instructions\n"
    )
    await message.reply(start_text, parse_mode='Markdown')

@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    await message.reply("Thanks for subscribing to my YT channel! 🎉📺")

@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    about_text = (
        "I'm Gunther Bot, a friendly bot designed to help you stay updated and entertained.\n"
        "Feel free to explore my features and interact with me!\n"
        "For more information, visit [my website](https://www.example.com).\n"
    )
    await message.reply(about_text, parse_mode='Markdown')


@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    await message.answer_photo('https://avatars.githubusercontent.com/u/62240649?v=4')
# Define a function to handle messages containing a URL
@dp.message_handler(regexp=r'https?://[^\s/$.?#].[^\s]*')
async def handle_url(message: types.Message):
    url = message.text

    # Call the get_website_title function to retrieve the title
    title =webdriver.get_website_title(url)

    # Send the retrieved title back to the user
    await message.answer(f"Website title: {title}")





if __name__ == '__main__':
    executor.start_polling(dp)
