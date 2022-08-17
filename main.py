import telebot
import requests
from decouple import config
from random import randrange
from bs4 import BeautifulSoup

API_KEY = config("TOKEN_TELEGRAM")

bot = telebot.TeleBot(API_KEY)


def get_message_id(msg):
    try:
        return msg.reply_to_message.message_id
    except (NameError, AttributeError) as e:
        return msg.message_id


@bot.message_handler(commands=["saoko"])
def saoko(msg):
    que_dices = open('./assets/que_dices.mp3', 'rb')
    bot.send_audio(msg.chat.id, que_dices,
                   performer='Rosalía', title='Chica, ¿qué dices?', reply_to_message_id=get_message_id(msg))


@bot.message_handler(commands=["rosalia"])
def bizcochito(msg):
    number = randrange(1, 5)
    bizcochito = open(f'./assets/saoko/{number}.mp4', 'rb')
    bot.send_animation(
        msg.chat.id, animation=bizcochito, reply_to_message_id=get_message_id(msg))


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
    name = 'bait'
    if msg.text.find('?') != -1 or msg.text.find('❓') != -1:
        name = 'is_bait'
    if msg.text.find('⭐') != -1 or msg.text.find('excellent') != -1:
        name = 'excellent_bait'
    if msg.text.find('🐳') != -1 or msg.text.find('🐋') != -1 or msg.text.find('big') != -1:
        name = 'bigger_bait'
    if msg.text.find('low') != -1:
        name = 'low_bait'
    if msg.text.find('high') != -1:
        name = 'high_bait'
    if msg.text.find('nice') != -1:
        name = 'nice_bait'

    bait = open(f'./assets/baits/{name}.png', 'rb')
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


def get_person_name(text):
    try:
        list = text.split('@')
        if len(list) <= 1:
            return ''
        txt = list[-1].lstrip()
        person = f"@{txt}"
        if person.find('tio_lu_bot') == -1:
            return person
        else:
            return ''
    except:
        return ''


@bot.message_handler(commands=["parabens"])
def parabens(msg):

    extra = ['', 'amigo/', 'amiga/', 'aniversario-irma/', 'irmao/',
             'filha/', 'filho/', 'mae/', 'prima/', 'sobrinha/', 'sobrinho/']
    page = randrange(len(extra))
    URL = f"https://www.frasesdeaniversario.com.br/{extra[page]}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("img")
    number = randrange(1, len(results))
    parabens = results[number]['src']
    bot.send_photo(
        msg.chat.id, caption=get_person_name(msg.text), photo=parabens, reply_to_message_id=get_message_id(msg))


@bot.message_handler(commands=["triste"])
def triste(msg):
    triste = open('./assets/triste.png', 'rb')
    bot.send_photo(
        msg.chat.id, photo=triste, caption='🎉🎉🎉', reply_to_message_id=get_message_id(msg))


@bot.message_handler(commands=["encerrada"])
def encerrada(msg):
    semana = open('./assets/semana.mp3', 'rb')
    bot.send_audio(msg.chat.id, semana, title='São 4 horas da tarde de uma quarta-feira',
                   reply_to_message_id=get_message_id(msg))


@bot.message_handler(commands=["peito"])
def peito(msg):
    peito = open('./assets/peito.mp3', 'rb')
    bot.send_audio(msg.chat.id, peito, performer='peito', title='vai se abᵣᵢᵣ...',
                   reply_to_message_id=get_message_id(msg))


@bot.message_handler(commands=["vazio"])
def vazio(msg):
    vazio = open('./assets/vazio.mp3', 'rb')
    bot.send_audio(msg.chat.id, vazio, title='Ahh o Vazio.',
                   reply_to_message_id=get_message_id(msg))


@bot.message_handler(commands=["macetar"])
def macetar(msg):
    macetar = open('./assets/posso_macetar.mp4', 'rb')
    bot.send_video(msg.chat.id, video=macetar, caption='Posso... macetar?',
                   reply_to_message_id=get_message_id(msg))


@bot.message_handler(commands=["feliz"])
def feliz(msg):
    feliz = open('./assets/felicidade.mp4', 'rb')
    bot.send_video(msg.chat.id, video=feliz, caption='😁😆😁🤪',
                   reply_to_message_id=get_message_id(msg))

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
