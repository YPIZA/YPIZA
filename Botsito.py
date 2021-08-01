from BotAmino import *
from fancy_text import fancy
import sys
import emoji
import urllib.request
import time
from pathlib import Path
from google_trans_new import google_translator
import random
import os
from os import path
from random import uniform, choice, randint
email = "jjravt2d6jh@yoggm.com"
password = "lollollol1"
client = BotAmino(email=email, password=password)
vers = "2.0.4"
print(f"Bot Version = {vers}")

@client.command("Comandos")
def Comandos(data):
    data.subClient.send_message(data.chatId, message="""
[C]Comandos, grr.

[C]!comandos [Mira los comandos]

[C]!game [Jugador1, Jugador2] - Juego ramdom

[C]!snus [Usuario] - Proyecto termonuclear, lol.

[C]!randemoji - Emojis ramdom

[C]!fancytext [Texto] - Haz que el bot decore un mensaje.

[C]!luv [Usuario - 1, Usuario - 2] - Comprueba que probabilidad hay de que dos usuarios de amen.

[C]!google [Texto] - Busca algo en Google.

[C]!qs [Texto] - Hazle una pregunta al bot.

[C]!joinallchats - Haz que el bot se una a todos los chats.

[C]!leaveallchats - Haz que el bot abandone todos los chats.

[C]!chatinfo - Informacion del chat.

[C]!text [Texto] - Hаz que el bot diga algo.

[C]!comandos2 [Pagina de comandos 2]
""")

@client.command("comandos2")
def Comandos2(data):
	data.subClient.send_message(data.chatId, message="""
[C]!follow - Te voy a seguir como simp a e-girl.

[C]!unfollow - Me voy a volver un Chad y conseguire una buena novia.

[C]!joinchat [Link del chat/Chat Link] 

[C]!backgr - Comando para tener el fondo del chat.

[C]!staffask [Texto] - Escribe un mensaje anonimo al staff.

[C]!cum - Que podra ser que esta tanto en tu boca.

[C]!gay/!lesbiana - descubre que tan gay o lesbiana eres.

[C]!stickmg - Conseguir un sticker en imagen.

[C]!reboot - Reiniciar el bot.

[C]!comment - Comando para obtener un comentario del bot.

[C]!msgtypes - Tipos de mensajes.

[c]!randemojis - Emojis ramdom
[c]
""")


@client.on_member_join_chat()
def privet(data):
    data.subClient.send_message(data.chatId, f"Bienvenido {data.author} usa !comandos)")


@client.on_member_leave_chat(["chatId"]) # the chatId is not necessary, put one if you want a specified chat only
def poka(data):
    data.subClient.send_message(data.chatId,f"Oh,no {data.author} se fue detras de una polla..")



@client.command("luv")
def luv(data):
		msg = data.message + " null null "
		msg = msg.split(" ")
		msg[2] = msg[1]
		msg[1] = msg[0]
		try:
			data.subClient.send_message(chatId=data.chatId, message=f"La probabilidad de que {msg[1]}  Ame a {msg[2]} es {random.randint(0,100)}%")
		except:
			pass

@client.command("hate")
def hate(data):
		msg = data.message + " null null "
		msg = msg.split(" ")
		msg[2] = msg[1]
		msg[1] = msg[0]
		try:
			data.subClient.send_message(chatId=data.chatId, message=f"La probabilidad de que {msg[1]}  odie a {msg[2]} es {random.randint(0,100)}%")
		except:
			pass

@client.command("hug")
def hug(data):
		msg = data.message + " null null "
		msg = msg.split(" ")
		msg[2] = msg[1]
		msg[1] = msg[0]
		try:
			data.subClient.send_message(chatId=data.chatId, message=f" {data.author}  le da un calido abrazo a {msg[1]}")
		except:
			pass

@client.command("kiss")
def kiss(data):
		msg = data.message + " null null "
		msg = msg.split(" ")
		msg[2] = msg[1]
		msg[1] = msg[0]
		try:
			data.subClient.send_message(chatId=data.chatId, message=f"{data.author} besa apasionadamente a {msg[1]}")
		except:
			pass

@client.command("marry")
def marry(data):
		msg = data.message + " null null "
		msg = msg.split(" ")
		msg[2] = msg[1]
		msg[1] = msg[0]
		try:
			data.subClient.send_message(chatId=data.chatId, message=f"{data.author} le propone matrimonio a {msg[1]} :0")
		except:
			pass

@client.command("google")
def google(data):
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    data.subClient.send_message(chatId=data.chatId, message=f"https://www.google.com/search?q={msg}")

@client.command("snus")
def snus(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[1] = msg[0]
	try:
		data.subClient.send_message(chatId=data.chatId, message=f"{msg[1]} Hizo una mezcla super ramdom de.. ¿Esperma?")
	except:
		pass
#command
@client.command("game")
def game(data):
	msg = data.message + " null null "
	msg = msg.split(" ")
	try:
		rounds = int(msg[0])
	except (TypeError, ValueError):
		rounds = 5
		msg[2] = msg[1]
		msg[1] = msg[0]
		msg[0] = 5
	data.subClient.send_message(chatId=data.chatId, message=f"Hay una pelea entre {msg[1]} y {msg[2]}...")
	win1 = 0
	win2 = 0
	round = 0
	agress = ''
	defens = ''
	for zabiv in range(0, rounds):
		round = round + 1
		data.subClient.send_message(chatId=data.chatId, message=f"[bc]Round {round}/{rounds}")
		punch = randint(0, 1)
		if punch == 0:
			win1 = win1 + 1
			agress = msg[1]
			defens = msg[2]
		else:
			     	win2 = win2 + 1
			     	agress = msg[2]
			     	defens = msg[1]
		time.sleep(4)
		data.subClient.send_message(chatId=data.chatId, message=f"[ic] {agress} Golpea! {defens}!")
		if win1 > win2:
		  data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[1]} Gano!")
		elif win1 < win2:
		  	data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[2]} Gano puntos!")
		elif win1 == win2:
		  		data.subClient.send_message(chatId=data.chatId, message=f"[iC]Solo el mejor chupa pollas gana la batalla.")
#Команда для вопросов для бота

@client.command("qs")
def qs(data):
	lis = ['Tal vez', 'Si', 'No', 'Claro', 'Nunca', 'buscalo en google']
	msg = data.message + "null?"
	msg = data.message.split(" ")
	data.subClient.send_message(chatId=data.chatId, message=str(random.choice(lis)))


@client.command("gay")
def gay(data):
	lis = ['🏳‍🌈 eres gay en un: 0%', '🏳‍🌈 eres gay en un: 0.5%', '🏳‍🌈 eres gay en un: 1%', '🏳‍🌈 eres gay en un: 2.56%', '🏳‍🌈 eres gay en un: 3%', '🏳‍🌈 eres gay en un: 5%', '🏳‍🌈 eres gay en un: 13.45%', '🏳‍🌈 eres gay en un: 23.75%', '🏳‍🌈 eres gay en un: 35.93%', '🏳‍🌈 eres gay en un: 41.99%', '🏳‍🌈 eres gay en un: 49%', '🏳‍🌈 eres gay en un: 69.34%', '🏳‍🌈 eres gay en un: 79.33%', '🏳‍🌈 eres gay en un: 95.55%', '🏳‍🌈 eres gay en un: 100%']
	msg = data.message + "null?"
	msg = data.message.split(" ")
	data.subClient.send_message(chatId=data.chatId, message=str(random.choice(lis)))

@client.command("lesbiana")
def lesbiana(data):
	lis = ['🏳‍🌈 eres lesbiana en un: 0%', '🏳‍🌈 eres lesbiana en un: 0.5%', '🏳‍🌈 eres lesbiana en un: 1%', '🏳‍🌈 eres lesbiana en un: 2.56%', '🏳‍🌈 eres lesbiana en un: 3%', '🏳‍🌈 eres lesbiana en un: 5%', '🏳‍🌈 eres lesbiana en un: 13.45%', '🏳‍🌈 eres lesbiana en un: 23.75%', '🏳‍🌈 eres lesbiana en un: 35.93%', '🏳‍🌈 eres lesbiana en un: 41.99%', '🏳‍🌈 eres lesbiana en un: 49%', '🏳‍🌈 eres lesbiana en un: 69.34%', '🏳‍🌈 eres lesbiana en un: 79.33%', '🏳‍🌈 eres lesbiana en un: 95.55%', '🏳‍🌈 eres lesbiana en un: 100%']
	msg = data.message + "null?"
	msg = data.message.split(" ")
	data.subClient.send_message(chatId=data.chatId, message=str(random.choice(lis)))

@client.command("cum")
def sperm(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[2] = msg[1]
	msg[1] = msg[0]
	try:
		data.subClient.send_message(chatId=data.chatId, message=f"{msg[1]} Conseguiste cum en la boca y te dieron varios golpes...")
	except:
		pass
		
#Команда чтобы бот заходил во все активные чаты
@client.command("joinallchats")
def joinallchats(data):
	print(type(data))
	data.subClient.send_message(chatId=data.chatId, message="En eso estoy...")
	data.subClient.join_all_chat()
	data.subClient.send_message(chatId=data.chatId, message="Conectado a todos los chats!")
@client.command("leaveallchats")
def joinallchats(data):
	print(type(data))
	data.subClient.send_message(chatId=data.chatId, message="En eso estoy...")
	data.subClient.leave_all_chats()
	data.subClient.send_message(chatId=data.chatId, message="he abandonado todos los chats!")
@client.command("joinchat")
def joinchat(data):
	try:
		data.subClient.send_message(chatId=data.chatId, message="Ahora entro!")
		data.subClient.join_chatroom(data.message)
		data.subClient.send_message(chatId=data.chatId, message="Listo!")
	except:
		data.subClient.send_message(chatId=data.chatId, message="No es posible entrar al chat!")
		pass

@client.command("follow")
def follow(data):
	try:
		data.subClient.send_message(data.chatId, f'Siguiendo a {data.author}')
		data.subClient.follow_user(data.authorId)
	except:
		data.subClient.send_message(data.chatId, f'No se puede seguir a {data.author}')
		pass

@client.command("chatinfo")
def chatinfo(data):
	data.subClient.send_message(data.chatId, f"chatId = {data.chatId}")

@client.command("backgr")
def backgr(data):
        image = data.subClient.get_chat_thread(chatId=data.chatId).backgroundImage
        if image:
            filename = path.basename(image)
            urllib.request.urlretrieve(image, filename)
            with open(filename, 'rb') as fp: data.subClient.send_message(data.chatId, file=fp, fileType="image")
            os.remove(filename)

@client.command("staffask")
def staffask(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[2] = msg[1]
	msg[1] = msg[0]
	data.subClient.ask_amino_staff(message=msg[1])
	data.subClient.ask_amino_staff(message=f"Este mensaje fue enviado por {data.author} soy un bot, tenga buen dia.")

@client.command("translate")
def translate(data):
    translator = google_translator()
    translate_text = translator.translate(data.message)
    data.subClient.send_message(data.chatId, f"Перевод: {translate_text}")

@client.command("stickmg")
def stickmg(data):
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	reply_message = info.json['extensions']
	if reply_message:
	   image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
	   filename = image.split("/")[-1]
	   filetype = image.split(".")[-1]
	   if filetype!="gif":
	   	filetype = "image"
	   	urllib.request.urlretrieve(image, filename)
	   	with open(filename, 'rb') as fp: data.subClient.send_message(data.chatId, file=fp, fileType="image")
	os.remove(filename)

#########Команда для изменения ника бота/Command to change the bot's nickname############
@client.command("nckname")
def nckname(data):
	data.subClient.subclient.edit_profile(nickname=data.message)
	data.subClient.send_message(chatId=data.chatId,message=f"El apodo del bot se cambio {data.message}")

@client.command("unfollow")
def unfollow(data):
    data.subClient.send_message(data.chatId, f'Dejando de simpear a {data.author}')
    data.subClient.unfollow_user(data.authorId)

@client.command("welcome")
def welcome(data):
        data.subClient.set_welcome_message(data.message)
        data.subClient.send_message(data.chatId, "Приветственное сообщение изменено")

@client.command("randemoji")
def randemoji(data):
	lis = ['😰😨😱😓🤯', '😎🤡🥴🤕🌚', '🌝🥸👻🎃', '😺👹😈😇💩', '😛😉😊😘🥳', '🤣😀😆🥰🙂', '☺️😑🙃😶🤗', '🤩😋😔😌☺️', '🤫🤐🥺🙄🤔', '🧐😤😠😳🤯', '😓😥😩😖😵', '🌞🤮🤧🤒🎃', '😍😚🤭🥲😄', '😃😂🤣😭😰', '🤬😡😮😯😲', '🤓🤑🤠😇😷', '🥵🥶👺☠️👽', '😸😹😺😻😼', '😽🙀😿😾💀', '❤️🧡💛💚💙', '💜🤎🖤🤍♥️', '💘💝💖💗💓', '💞💕💌💟❣️', '💔💋👅👄👀', '🦾🦠🦷🏵️💐', '🧝🧙🧛🧟🥷', '😪😴🥱🤤🙄', '👿😈🔥⭐🌟', '🎊🎉🕳️💤💦', '🌜👻🤖💢⚡', '✨💫👁️🍂☀️', '🧠🫀🫁🩸🌡️', '👉👌🍺🍷👄', '🦁🐻🐼🐨🐹', '🐭🐷🐸🙉🐶', '🌌🌠🌉🌆🌃', '🕊️🦅🐦🦥🦏', '🐲🦖🐢🦮🐈', '🐐🦬🐖🐑🐆', '🦍🦧🐿️🦦🦈', '🐝🐠🐋🦋🐜', '🍔🍖🍗🌭🥪', '🥞🍳🫓🌮🍕', '🍉🍓🍒🫐🍎', '🧆🥙🥘🍜🦪', '🍧🍱🥟🍚🍢', '🍰🍙🍡🍣🍟', '🧇🥯🌯🥟🥡', '🍭🍩🍪🥮🍨', '🥗🍲🫕🍥🍿', '🥃🍾🍹🍸🍻', '🅿️🅾️🆘ℹ️🖕🏿', '🤏✋👊🙌👇', '👾🕹️🎮🎲🃏', '💵💴💶💷💰', '🇺🇸🇹🇨🇸🇻🇺🇦🇼🇸', '🏤🏣🏨🏥🏩']
	data.subClient.send_message(data.chatId, message=str(random.choice(lis)))

@client.command("fancytext")
def fancytext(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[1] = msg[0]
	data.subClient.send_message(data.chatId, message=fancy.light(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.bold(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.box(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.sorcerer(msg[1]))


@client.command("reboot")
def reboot(data):
    data.subClient.send_message(data.chatId, "Bot reiniciado.")
    os.execv(sys.executable, ["None", os.path.basename(sys.argv[0])])

@client.command("comment")
def comment_profile(data):
	list = ["que lindas piernas, a que hora se abren??", "por la sombrita que el sol derrite a los bombones como tu", "quien fuera cemento para sostener semejante monumento", "Quiero que nuestra relación sea como el mar, que se vea el inicio pero nunca el final", "Dios se arrepiente de no haberte puesto como sol para iluminar la tierra"]
	data.subClient.comment(message=str(random.choice(list)), userId=data.authorId)
	data.subClient.send_message(data.chatId, message="El bot te dejo un comentario")

@client.command("msgtypes")
def msgtypes(data):
	data.subClient.send_message(data.chatId, message="""
[BC]--MESSAGETYPES--
[C]0 - BASE
[C]1 - STRIKE
[C]50 - UNSUPPORTED_MESSAGE
[C]57 - REJECTED_VOICE_CHAT
[C]58 - MISSED_VOICE_CHAT
[C]59 - CANCELED_VOICE_CHAT
[C]100 - DELETED_MESSAGE
[C]101 - JOINED_CHAT
[C]102 - LEFT_CHAT
[C]103 - STARTED_CHAT
[C]104 - CHANGED_BACKGROUND
[C]105 - EDITED_CHAT
[C]106 - EDITED_CHAT_ICON
[C]107 - STARTED_VOICE_CHAT
[C]109 - UNSUPPORTED_MESSAGE
[C]110 - ENDED_VOICE_CHAT
[C]113 - EDITED_CHAT_DESCRIPTION
[C]114 - ENABLED_LIVE_MODE
[C]115 - DISABLED_LIVE_MODE
[C]116 - NEW_CHAT_HOST
[C]124 - INVITE_ONLY_CHANGED
[C]125 - ENABLED_VIEW_ONLY
[C]126 - DISABLED_VIEW_ONLY
""")

@client.command("text")
def say_text(data):
	data.subClient.send_message(data.chatId, message=data.message)

@client.command("profile")
def profileinfo(data):
	repa = data.subClient.get_user_info(data.authorId).reputation
	lvl = data.subClient.get_user_info(data.authorId).level
	crttime = data.subClient.get_user_info(data.authorId).createdTime
	followers = data.subClient.get_user_achievements(data.authorId).numberOfFollowersCount
	profilchange = data.subClient.get_user_info(data.authorId).modifiedTime
	commentz = data.subClient.get_user_info(data.authorId).commentsCount
	posts = data.subClient.get_user_achievements(data.authorId).numberOfPostsCreated
	followed = data.subClient.get_user_info(data.authorId).followingCount
	sysrole = data.subClient.get_user_info(data.authorId).role
	data.subClient.send_message(data.chatId, message=f"""
[C]Nickname: {data.author}
[C]UserId: {data.authorId}
[C]Fecha de creacion: {crttime}
[C]Ultimos cambios: {profilchange}
[C]Numero de reputacion: {repa}
[C]Nivel: {lvl}
[C]Numero de posts creados: {posts}
[C]Numeros de comentarios en el perfil: {commentz}
[C]Nombre de personas que sigue: {followed}
[C]Numero de personas que lo/a siguen: {followers}
[C]Numero de cuenta en el sistema: {sysrole}
	""")

client.launch()
################################################commands/команды################################################
time.sleep(10)
print("Bot started")

#socket
def restart():
    while True:
        time.sleep(120)
        count = 0
        for i in threading.enumerate():
            if i.name == "restart_thread":
                count += 1
        if count <= 1:
            print("Restart")
            client.socket.close()
            client.socket.start()