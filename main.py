import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Men haqimda")
    btn2 = types.KeyboardButton("Loyihalarim")
    btn3 = types.KeyboardButton("Kontakt")
    btn4 = types.KeyboardButton("Bilimlarim")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    text = "Assalom alaykum, men Asadbek Rakhimov. \nBu mening portfolio botim. \nQuyidagi bo'limlardan birini tanlang"

    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda m: m.text == "Men haqimda")
def aboutme_handler(message):
    text = "Men frontend engineermen. React.js & Next.js specialistman"
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: m.text == "Loyihalarim")
def projects_handler(message):
    text = """
Loyihalarim

Tibbiy yordam xizmati vebsayti: [Website](https://medical-assistance2.vercel.app)
Matnni lotindan kirilga yoki kirildan lotinga o'tkazuvchi Telegram bot: [Bot](https://t.me/cyrillic_to_latin_converters_bot)
"""
    
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "Kontakt")
def contact_handler(message):
    text = "Aloqa qism tez orada qo'shiladi"

    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Telegram", url="https://t.me/asadbekodev")
    btn2 = types.InlineKeyboardButton("Linkedin", url="https://www.linkedin.com/in/asadbek-rakhimov")
    keyboard.add(btn1, btn2)

    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda m: m.text == "Bilimlarim")
def skills_handler(message):
    text = "Men HTML, CSS, Python texnologiyalarini bilaman"

    bot.send_message(message.chat.id, text)
	
bot.infinity_polling()