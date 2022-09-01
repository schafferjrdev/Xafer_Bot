import telebot
import requests
from decouple import config
from random import randrange
from bs4 import BeautifulSoup
from io import BytesIO
from gtts import gTTS
from pydub import AudioSegment
from pydub.utils import which
import pytz
from datetime import datetime

AudioSegment.converter = which("ffmpeg")

API_KEY = config("TOKEN_TEST")

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
def rosalia(msg):
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
def quit(msg):
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
def sentiu(msg):
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
    semana = open('./assets/semana.mp4', 'rb')
    bot.send_video(msg.chat.id, video=semana)


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


@bot.message_handler(commands=["aniversariantes"])
def aniversariante(msg):
    aniversariantes = ["Carol,02/01,Capricórnio",
                       "Dennys,09/02,Aquário",
                       "Mariana,14/02,Aquário",
                       "Nayeli,13/03,Peixes",
                       "Thetheu,28/03,Áries",
                       "Iza,30/04,Touro",
                       "Schaffer,10/06,Gêmeos",
                       "Rafael,19/07,Câncer",
                       "Luana,24/07,Leão",
                       "Rayane,28/07,Leão",
                       "Vinícius,01/08,Leão",
                       "Letícia,16/08,Leão",
                       "Bruna,24/08,Virgem",
                       "Marcos,31/08,Virgem",
                       "Aquiles,01/09,Virgem",
                       "Saulo,17/09,Virgem",
                       "Paolla,30/09,Libra",
                       "Estela,01/10,Libra",
                       "Renato,15/10,Libra",
                       "Marília,09/12,Sagitário",
                       "Bia,22/12,Capricórnio"]

    date = datetime.now(pytz.timezone('America/Sao_Paulo'))

    def current_birthdays(p):
        month = p.split(",")[1].split('/')[1]
        current_month = date.strftime("%m")
        return month == current_month

    aniversariantes_mes = filter(current_birthdays, aniversariantes)

    def birthday(i):
        name = i.split(",")[0]
        day = i.split(",")[1].split('/')[0]
        return f"{name} no dia {day}"

    lista_aniversario = list(map(birthday, aniversariantes_mes))

    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    msg_mes = f"Para o mês de {meses[int(date.strftime('%m'))-1]}"
    msg_aniversariantes = 'Ninguém...'

    if len(lista_aniversario) > 0:
        msg_aniversariantes = '\n'.join(list(lista_aniversario))

    final_msg = f"{msg_mes}\n{msg_aniversariantes}"

    bot.reply_to(
        msg, final_msg)

# @bot.message_handler(commands=["piadoca"])
# def piadoca(msg):
#     pensar = ['Lá vai...', 'Deixa eu pensar...', 'Vou ver aqui...',
#               'Hm...', 'Deixe-me ver...', 'Tem essa aqui...']
#     n_pensar = randrange(len(pensar))

#     bot.reply_to(
#         msg, pensar[n_pensar])

#     URL = f"https://trocadil.io/api/aleatorio"
#     piada = requests.get(URL).json()[0]

#     mp3_fp = BytesIO()
#     answer_tts = gTTS(piada['answer'], lang='pt')
#     answer_tts.write_to_fp(mp3_fp)
#     mp3_fp.seek(0)
#     answer = AudioSegment.from_mp3(mp3_fp)

#     mp3_fp2 = BytesIO()
#     question_tts = gTTS(piada['question'], lang='pt')
#     question_tts.write_to_fp(mp3_fp2)
#     mp3_fp2.seek(0)
#     question = AudioSegment.from_mp3(mp3_fp2)

#     risadas = ['hahaha', 'kkkkk', 'rsrsrs', 'hehehe']
#     number = randrange(len(risadas))

#     mp3_fp3 = BytesIO()
#     risada_tts = gTTS(risadas[number], lang='pt')
#     risada_tts.write_to_fp(mp3_fp3)
#     mp3_fp3.seek(0)
#     risada = AudioSegment.from_mp3(mp3_fp3)

#     piada = question+answer+risada
#     mp3IO = BytesIO()
#     piada.export(mp3IO, format="mp3")

#     bot.send_audio(msg.chat.id, mp3IO.getvalue(), performer='Cão',
#                    title=risadas[number])


@bot.message_handler(commands=["comandos"])
def comandos(msg):
    bot.reply_to(
        msg, """    O Cão é muito bem articulado.
/comandos - Quer saber por que?
/no - No. Nope. Não. Nein. Não mesmo. Sério, não.  
/sentiu - Diga lá, Lú  
/rosalia - Yo no soy y ni vi'a ser tu bizcochito
/saoko - Chica, ¿qué dices?
/bait - Wow, nice bait  
/hahaha - HAHAHAHA KKKKK ASUHASHUHUAS
/quit - Até logo, até mais ver, bon voyage
/parabens - Aê, hora de apagar a velinha 😈
/triste - Fico muito triste com isso 🎉🎉
/encerrada - ...semana praticamente encerrada
/peito - meu peito vai se abᵣᵢᵣ...
/vazio - Ahh o vazio.
/macetar - Posso macetar?
/feliz - 😁😆😁🤪
/aniversariante - Quem tá de parabéns?
    """)

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
