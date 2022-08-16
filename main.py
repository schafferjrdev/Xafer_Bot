import telebot
from decouple import config
from random import randrange

API_KEY = config("TOKEN_TELEGRAM")

bot = telebot.TeleBot(API_KEY)


def get_message_id(msg):
    print('has reply', msg.reply_to_message)
    try:
        return msg.reply_to_message.message_id
    except (NameError, AttributeError) as e:
        return msg.message_id


@bot.message_handler(commands=["saoko"])
def saoko(msg):
    number = randrange(1, 5)
    saoko = open(f'./assets/saoko/{number}.mp4', 'rb')
    que_dices = open('./assets/que_dices.mp3', 'rb')

    if msg.text.find('hablo') != -1:
        bot.send_audio(msg.chat.id, que_dices,
                       performer='Rosalía', title='Chica, ¿qué dices?', reply_to_message_id=get_message_id(msg))
    else:
        bot.send_animation(
            msg.chat.id, animation=saoko, reply_to_message_id=get_message_id(msg))


@bot.message_handler(commands=["hahaha"])
def hahaha(msg):
    hahaha = open('./assets/hahaha.mp3', 'rb')
    risadas = ['hahaha', 'kkkkk', 'rsrsrs', 'ashuahus']
    number = randrange(len(risadas))
    bot.send_audio(msg.chat.id, hahaha,
                   title=risadas[number], reply_to_message_id=get_message_id(msg))


@bot.message_handler(commands=["quit"])
def hahaha(msg):
    quit = open('./assets/quit.png', 'rb')
    byes = ["Até logo", "Até mais ver", "Bon voyage", "Arrivederci", "Até mais",
            "Adeus", "Boa viagem", "Vá em paz", "Que a porta bata onde o sol não bate"]
    number = randrange(len(byes))
    bot.send_photo(
        msg.chat.id, photo=quit, reply_to_message_id=msg.message_id, caption=byes[number])


@bot.message_handler(commands=["no"])
def no(msg):
    no = open('./assets/no.mp4', 'rb')
    bot.send_animation(
        msg.chat.id, animation=no, reply_to_message_id=get_message_id(msg))


@bot.message_handler(commands=["bait"])
def bait(msg):
    bait = open('./assets/bait.jpg', 'rb')
    bot.send_photo(
        msg.chat.id, photo=bait, reply_to_message_id=get_message_id(msg))


@bot.message_handler(commands=["sentiu"])
def bait(msg):
    sentiu = open('./assets/sentiu.png', 'rb')

    bot.send_message(
        msg.chat.id, "Galvão...")
    bot.send_message(
        msg.chat.id, "Diga lá, Tino.")
    bot.send_photo(
        msg.chat.id, photo=sentiu, reply_to_message_id=get_message_id(msg))

# @bot.message_handler(commands=["google"])
# def google(msg):
#     print(msg)
#     print('=========================================')
#     try:
#         googled = msg.reply_to_message.text.replace(
#             '\n', ' ').replace(' ', '+')
#         url = f"vamos lá, nem é tão complicado assim...\nhttps://letmegooglethat.com/?q={googled}"
#         bot.send_message(
#             msg.chat.id, text=url, reply_to_message_id=msg.reply_to_message.message_id)
#     except:
#         bot.reply_to(
#             msg, "???")

# To send an Audio File
# bot.send_audio(msg.chat.id, que_horas_sao(msg.date),
#                performer='@tio_lu', title='Diga lá, Lu')

# To send a Message File
# bot.reply_to(
#     msg, f"São {semana_encerrada(msg.date)}, Ahh... Semana praticamente encerrada!")


# def alwaysTrue(msg):
#     return True


# @bot.message_handler(func=alwaysTrue)
# def general(msg):
#     print(msg)
#     bot.reply_to(
#         msg, f"{msg.text}?")

bot.polling()
