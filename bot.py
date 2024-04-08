from telebot import types
import telebot
import random
import requests

bot = telebot.TeleBot('6845624400:AAES-DjSYrTKU4HjJecyBhvZ3DJLlO31qSw')

# Тут получаю инфу о погоде
def get_weather(city):
    url = f"https://wttr.in/{city}?format=%t+%C"
    response = requests.get(url)
    data = response.text
    return data

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, "Привет, я бот Юми! Хочешь узнать какая погода сейчас в твоем городе?")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Приветик, как у тебя дела?)")
    elif message.text == "/weather":
        bot.send_message(message.from_user.id, "Напиши название города, чтобы я смогла дать тебе информацию.")
    elif message.text.startswith('/weather '):
        city = message.text.replace('/weather ', '')
        weather_info = get_weather(city)
        bot.send_message(message.from_user.id, f'Сейчас погода в городе {city}: {weather_info}')
    elif message.text == "Хорошо":
        responses = ["Я очень рада, надеюсь, что всегда так и будет!", "Это чудесно!"]
        bot.send_message(message.from_user.id, random.choice(responses))
    elif message.text == "Не очень":
        responses = ["Как же так?(", "Почему-же? Что-то случилось?("]
        bot.send_message(message.from_user.id, random.choice(responses))
    elif message.text == "Плохо":
        responses = ["Печально", "Тогда позанимайся любимыми делами и все обязательно наладится", "Нужно отдохнуть и набраться сил."]
    elif message.text == "АХАХ":
        bot.send_message(message.from_user.id, "че ржешь, балбес")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Поможет бог...")

bot.polling(none_stop=True, interval=0)
