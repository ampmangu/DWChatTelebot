#!/usr/bin/env python
# encoding: utf-8

import logging
import telegram
import random
import json
from giphypop import translate
with open('quotes.json') as data_file:
    quotes = json.load(data_file)
    first = quotes["First"]
    second = quotes["Second"]
    third = quotes["Third"]
    fourth = quotes["Fourth"]
    fifth = quotes["Fifth"]
    sixth = quotes["Sixth"]
    seventh = quotes["Seventh"]
    eighth = quotes["Eighth"]
    war = quotes["War"]
    ninth = quotes["Ninth"]
    tenth = quotes["Tenth"]
    eleven = quotes["Eleven"]
    twelfth = quotes["Twelfth"]

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    bot = telegram.Bot(token='145555617:AAHwQupsAqrUFCoajzyohWB_A3vLbIoapuc')

    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=5):
            text = update.message.text
            chat_id = update.message.chat.id
            update_id = update.update_id

            if '/start' in text:
                custom_keyboard = [["/quote", "/gif"]]
                reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
                bot.sendMessage(chat_id=chat_id,
                                text="Chose.",
                                reply_markup=reply_markup)
                LAST_UPDATE_ID = update_id + 1

            elif '/quote' in text:
                answer = quote()
                bot.sendMessage(chat_id=chat_id,
                                text=answer)
                LAST_UPDATE_ID = update_id + 1

            elif '/gif' in text:
                bot.sendMessage(chat_id=chat_id,
                                text="All time and space, there must be a gif around.")
                img = translate('doctor who')
                bot.sendDocument(chat_id=chat_id,
                                 document=img.fixed_height.url)
                print "Enviar Gif " + img.fixed_height.url
                LAST_UPDATE_ID = update_id + 1


def quote():
    docnumber = random.randint(0,12)
    if docnumber == 0:
        return "War Doctor: " + random.choice(war)
    elif docnumber == 1:
        return "First Doctor: "  + random.choice(first)
    elif docnumber == 2:
        return "Second Doctor: " + random.choice(second)
    elif docnumber == 3:
        return "Third Doctor: " + random.choice(third)
    elif docnumber == 4:
        return "Fourth Doctor: " + random.choice(fourth)        
    elif docnumber == 5:
        return "Fifth Doctor: " + random.choice(fifth)
    elif docnumber == 6:
        return "Sixth Doctor: " + random.choice(sixth)
    elif docnumber == 7:
        return "Seventh Doctor: " + random.choice(seventh)
    elif docnumber == 8:
        return "Eighth Doctor: " + random.choice(eighth)
    elif docnumber == 9:
        return "Ninth Doctor: " + random.choice(ninth)
    elif docnumber == 10:
        return "Tenth Doctor: " + random.choice(tenth)
    elif docnumber == 11:
        return "Eleventh Doctor: " + random.choice(eleven)
    else:
        return "Twelfth Doctor: " + random.choice(twelfth)
if __name__ == '__main__':
    main()