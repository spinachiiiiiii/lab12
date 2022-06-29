import telebot
from text_question import questions, patter_for_true, patter_for_false, answers
import random
from telebot import types
from datetime import datetime,timedelta
from time import time

token = '5452367281:AAGoH1z4781CS4OVWqFZow7JDOmLdho_gX4'
bot = telebot.TeleBot(token)
ans_id = 0


@bot.message_handler(commands=['start'])
def start(message):
    start_time = round(time())
    global flag, complete, total
    complete = False
    total = 0
    if message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Hello, it is bot for testing.I have 10 questions for you.And we start now!")
    random.shuffle(questions)
   """ for i in range(len(questions)):
        random.shuffle(questions[i].variants)
        bot.send_message(message.chat.id, questions[i].text, reply_markup = buttons(questions[i].variants))
        flag = 1
        while flag == 1:
            pass
        if i == len(questions) - 1:
            complete = True
            markup = types.ReplyKeyboardRemove(selective = False)
            test_time = round(time()) - start_time
            bot.send_message(message.chat.id, f"You pass the test.🎉\nYour time is {test_time} seconds.⌛\nToday date:{datetime.now().strftime('%d-%m-%Y,%H:%M:%S')}.\nYour goal is {total}/10!👍\nCongrats!🥳", reply_markup = markup)

"""
def buttons(variants):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(variants[0])
    btn2 = types.KeyboardButton(variants[1])
    btn3 = types.KeyboardButton(variants[2])
    btn4 = types.KeyboardButton(variants[3])
    markup.add(btn1, btn2, btn3, btn4)
    return markup


def check(message):
    global flag,total
    random.shuffle(patter_for_true)
    random.shuffle(patter_for_false)
    if message.text in answers:
        bot.send_message(message.chat.id, patter_for_true[0])
        flag = 0
        total += 1
    else:
        bot.send_message(message.chat.id, patter_for_false[0])
        flag = 0


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if not complete:
        check(message)
    else:
        bot.send_message(message.chat.id,"Your are finish test.Enter the '/start', if you want pass the test again!")

"""
bot.infinity_polling(True)
