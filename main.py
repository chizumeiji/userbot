import os
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions
import pyrogram

from PIL import Image
from pyrogram.raw.functions.messages import GetStickerSet

from pyrogram.raw.types import InputStickerSetShortName
from pyrogram.types import Sticker

import requests
from bs4 import BeautifulSoup as b

import io
import time
from time import sleep
import random

URL = 'https://www.anekdot.ru/last/good/'
def parser(url):
	r = requests.get(url)
	soup = b(r.text, 'html.parser')
	anekdots = soup.find_all('div', class_='text')
	return [c.text for c in anekdots]
list_of_jokes = parser (URL)
random.shuffle (list_of_jokes)
	

api_id = 19576945
api_hash = "07fca730186bb632bcb8e4f78302a84c"

app = Client("my_account", api_id=api_id, api_hash=api_hash)
schid = [-1001396952381]

@app.on_message(filters.command("channel",prefixes="."))
def channe(_,message):
	message.reply(app.get_chat(-1001874029811))
	
	
@app.on_message(filters.command("react",prefixes="."))
def aut(_,message):
	mid = message.id
	cid = message.chat.id
	uid = message.reply_to_message.from_user.id
	with open(f"{uid}-react.txt", "w") as file:
		file.write(message.text.split(".react ",maxsplit=1)[1])
	app.delete_messages(cid,mid)

@app.on_message(filters.command("анекдот",prefixes="."))
def anek(_,message):
	message.reply(random.choice(parser(URL)))
	
@app.on_message(filters.command("тю",prefixes=""))
def tyu(_,message):
	message.reply("тю")

@app.on_message(filters.command("grid",prefixes=".") & filters.me)
def process_image(client, message):
    original_image = client.download_media(message.reply_to_message)
    image = Image.open(original_image)
    square_size = image.size[0] // 5
    cropped_images = []
    for i in range(5):
        for j in range(5):
            left = j * square_size
            top = i * square_size
            right = (j + 1) * square_size
            bottom = (i + 1) * square_size
            cropped_image = image.crop((left, top, right, bottom))
            cropped_images.append(cropped_image)
    for cropped_image in cropped_images:
        output_buffer = io.BytesIO()
        cropped_image.save(output_buffer, format="PNG")
        output_buffer.seek(0)
        client.send_photo(chat_id=message.chat.id, photo=output_buffer)
    os.remove(original_image)




	##няшк милашк
@app.on_message(filters.command("🔼миленько🔼", prefixes="") | filters.command("мило",prefixes="") | filters.command("миленько",prefixes="") | filters.command("милашка",prefixes=""))
def da(_, message):
	message.reply_sticker(random.choice([ "CAACAgIAAxkBAAEJLAtkd6HWbyIH9f8Lys3A1QfPaG4uHgACzjEAAi6EuUv_ywzxqqyoii8E"]))
	
@app.on_message(filters.command("принт",prefixes="."))
def print(_,message):
	ortxt = list(message.text.split(".принт ",maxsplit=1)[1])
	tbp = []
	l = -1
	rtbp = ""
	for i in ortxt:
		tbp+=[""]
		l += 1
	while tbp != ortxt:
		try:
			r = random.randint(0,l)
			tbp[r] = ortxt[r] 
			for i in tbp:
				rtbp += i
			message.edit(rtbp)
			rtbp =""
			time.sleep(0.01)
		except:
			a = 1
			rtbp =""
	ptbp =""
	for i in ortxt:
		ptbp += str(i)
	message.edit(ortxt)
	
@app.on_message(filters.command("пр",prefixes="."))
def prnt(_,message):
	ortxt = list(message.text.split(".пр ",maxsplit=1)[1])
	tbp = []
	l = -1
	rtbp = "#"
	for i in ortxt:
		tbp+=["#"]
		l += 1
	while tbp != ortxt:
		try:
			r = random.randint(0,l)
			tbp[r] = ortxt[r] 
			for i in tbp:
				rtbp += i
			message.edit(rtbp)
			rtbp =""
			time.sleep(0.01)
		except:
			a = 1
			rtbp =""
	ptbp =""
	for i in ortxt:
		ptbp += str(i)
	message.edit(ptxt)
		
	
##.#
@app.on_message(filters.command("#",prefixes="")& filters.me)
def resh(_,message):
	mes =rmt = message.text.split("# ",maxsplit=1)[1]
	ls = -1
	tbp = "#"
	for i in mes:
		tbp += "#"
		ls += 1
	message.edit(tbp)
	ntbp = ""
	mes = list(mes)
	tbp = list(tbp)
	while tbp != rmt:
		for i in range(ls):
			if random.randint(1,4) == 3:
				tbp[i] = mes[i]
				mess = []
				for i in tbp:
					mess += i
				tbpp = []
				for i in tbp:
					tbpp += [i]
				ms = []
				for i in mes:
					ms += [i]
				mes = ms
				tbpp = tbp
				mees = ""
				for messs in mess:
					mees += messs
	message.edit(rmt)
		
	
	##вентилятор
@app.on_message(filters.command("вентилятор", prefixes=""))
def da(_, message):
	sid = random.choice([ "CAACAgIAAxkBAAEJF1JkbhHc3TU_AYKVby5MhaVSolzKFgACiCoAAmkjqUl4U_fO0M-mvi8E","CAACAgIAAxkBAAEJNihkfUsKtOvxZkiZehOjt2hIvWiMBwACVCkAAs42yUpdSNnGC9W_ci8E"])
	message.reply_sticker(sid)
	
	##да
@app.on_message(~filters.me & filters.command("да", prefixes="") & filters.private)
def da(_, message):
	if message.text == "да":
		if message.chat.id != -1001557590309 and message.chat.id != -1001477515884:
			message.reply_sticker(random.choice([ "CAACAgIAAxkBAAEJKohkd0YSFsu0NZ0Ji2bzRAKjdmwv-QAC0yoAAj9yuEvoq4wLPNjjxS8E"]))
		
		##е
@app.on_message(filters.command("е",prefixes="")|filters.command("e",prefixes=""))
def e(_,message):
		if message.text in ["e","е"]:
			if message.from_user.id != 205087351:
				message.reply("бать")
	


		##избиение
@app.on_message(filters.command("избить",prefixes=".") & filters.me)
def izbt(_,message):
		plak = app.get_messages( -1001975667433,20)
		plt = []
		pl = ""
		for i in plak.text:
			if i == ",":
				plt += [pl]
				pl = ""
			elif i == '"':
				f = 0
			else:
				pl += i
		izbit = plt
		sid = random.choice(izbit)
		mid = message.reply_to_message.id
		cid = message.chat.id
		mesid = message.id
		app.send_sticker(reply_to_message_id=mid, chat_id=cid, sticker=sid)
		app.delete_messages(cid,mesid)

		
		
		##шок
@app.on_message(filters.command("ужс",prefixes=".") & filters.me | filters.command("шок",prefixes=".") & filters.me)
def som(_,message):
		plak = app.get_messages( -1001975667433,4+18)
		plt = []
		pl = ""
		for i in plak.text:
			if i == ",":
				plt += [pl]
				pl = ""
			elif i == '"':
				f = 0
			else:
				pl += i
		shok = plt
		sid= random.choice(shok)
		mid = message.reply_to_message.id
		cid = message.chat.id
		mesid = message.id
		app.send_sticker(reply_to_message_id=mid, chat_id=cid, sticker=sid)
		app.delete_messages(cid,mesid)

		
		##сам
@app.on_message(filters.command("сам",prefixes=".") & filters.me )
def spm(_,message):
		plak = app.get_messages( -1001975667433,6+18)
		plt = []
		pl = ""
		for i in plak.text:
			if i == ",":
				plt += [pl]
				pl = ""
			elif i == '"':
				f = 0
			else:
				pl += i
		sam = plt
		sid= random.choice(sam)
		mid = message.reply_to_message.id
		cid = message.chat.id
		mesid = message.id
		app.send_sticker(reply_to_message_id=mid, chat_id=cid, sticker=sid)
		app.delete_messages(cid,mesid)
		
				
								
	##ладно
@app.on_message(~filters.me & filters.command("ладно", prefixes="") & filters.private)
def da(_, message):
	message.reply_sticker(random.choice([ "CAACAgIAAxkBAAEJKopkd0YVmwU7-MX88e9F6Txajd-l6AACkysAAuDHuUtfVcVmi_GH4S8E"]))
@app.on_message(~filters.me & filters.command("ладно", prefixes="") & ~filters.user(1320961187))
def da(_, message):
	if message.chat.id == -1001756452907:
		message.reply_sticker(random.choice([ "CAACAgIAAxkBAAEJKopkd0YVmwU7-MX88e9F6Txajd-l6AACkysAAuDHuUtfVcVmi_GH4S8E"]))
		

	#ди отсюда
@app.on_message(filters.command("иди нахуй", prefixes="") & filters.private)
def da(_, message):
	sid = (random.choice(["CAACAgIAAxkBAAEJNKFke-WD-oCtbj0fERLyD0akrc362wACOicAAvqD0UsfXJumKb9JNC8","CAACAgIAAxkBAAEJNKdke-ZLF5c69JmjKq148yq1fysQDgACsTIAArUG4UtmZKqd0Bv0qi8E","CAACAgIAAxkBAAEJLBdkd6hle6ltCKIW9YxxeF1N-pMJjAACQCkAAvPgwEtISbUINBgpFS8E","CAACAgIAAxkBAAEJLB9kd6hsF2HDRtJTSmTPcMtomxuj9wACzS0AAjajwUuwMbSXbPrN1S8E","CAACAgIAAxkBAAEJLB1kd6hqhuUuE6Pbj4eJYGoqWFzeiwACdiwAAtsXwUubluQFlDDepi8E""CAACAgIAAxkBAAEJKoRkd0YOqeznMpyA9jrbWC7LrQZJawACUykAAq05uUsX_isNERGXvy8E","CAACAgIAAxkBAAEJKoZkd0YQzYD9Dx4QqYN6SJGm1TMBvQACeS0AAtpuwUsrseugpZrSMi8E"]))
	if message.chat.id != -1001557590309 and message.chat.id != -1001477515884:
		message.reply_sticker(sid)
	
	##привкиє и покиє
@app.on_message(filters.command("привет", prefixes=".") & filters.me | filters.command("прив", prefixes=".") & filters.me | filters.command("ку", prefixes=".") & filters.me | filters.command("привки", prefixes=".") & filters.me)
def privs(_, message):
		plak = app.get_messages( -1001975667433,10+18)
		plt = []
		pl = ""
		for i in plak.text:
			if i == ",":
				plt += [pl]
				pl = ""
			elif i == '"' or i == " ":
				f = 0
			else:
				pl += i
		privet = plt
		sid = random.choice(privet)
		mid = message.reply_to_message.id
		cid = message.chat.id
		mesid = message.id
		app.send_sticker(reply_to_message_id=mid, chat_id=cid, sticker=sid)
		app.delete_messages(cid,mesid)

	##пздц
@app.on_message(filters.command("пиздец", prefixes="") & filters.private)
def pzdc(_,message):
		if message.chat.id != -1001557590309 and message.chat.id != -1001477515884:
			message.reply_sticker(random.choice(["CAACAgIAAxkBAAEJNKlke-ZTWZ9m0VhdX8Vh7y3vl1LEvgACOi4AAnKY4Es3OJJnBvLZIy8E","CAACAgIAAxkBAAEJNK1ke-ZaLlxa4qvaHm_MK-EXvGrBAQACODIAApsQ4UtFPmBaVva5pi8E","CAACAgIAAxkBAAEJLBtkd6ho9E6K7aKs5Eh4OtplptR6EgACVC4AAk-fuEsNeMbnMA7Eli8E"]))
		
		
		
		##смех
@app.on_message(filters.command("ахах", prefixes=".") & filters.me)
def sahah(_,message):
	sm = ""
	sme = []
	ss = app.get_messages(-1001975667433,12+18)
	for i in ss.text :
	   if i == ",":
	   	sme += [sm]
	   	sm = ""
	   elif i == '"':
	   	f = 1
	   else:
	   	sm+= i
	
	sid = random.choice(sme)
	mid = message.reply_to_message.id
	cid = message.chat.id
	mesid = message.id
	app.send_sticker(reply_to_message_id=mid, chat_id=cid, sticker=sid)
	app.delete_messages(cid,mesid)

		
		##плач
@app.on_message(filters.command("плак", prefixes=".") & filters.me)
def plack(_,message):
		plak = app.get_messages( -1001975667433,14+18)
		plt = []
		pl = ""
		for i in plak.text:
			if i == ",":
				plt += [pl]
				pl = ""
			elif i == '"':
				f = 0
			else:
				pl += i
		sid = random.choice(plt)
		mid = message.reply_to_message.id
		cid = message.chat.id
		mesid = message.id
		app.send_sticker(reply_to_message_id=mid, chat_id=cid, sticker=sid)
		app.delete_messages(cid,mesid)

		##кринж
@app.on_message(filters.command("кринш", prefixes=".") & filters.me)
def crinzh(ctx,message):
		kring =[]
		plak = app.get_messages( -1001975667433,16+18)
		plt = []
		pl = ""
		for i in plak.text:
			if i == ",":
				kring += [pl]
				pl = ""
			elif i == '"':
				f = 0
			else:
				pl += i
		if 1 == 1:
			sid = random.choice(kring)
			mid = message.reply_to_message.id
			cid = message.chat.id
			mesid = message.id
			app.send_sticker(reply_to_message_id=mid, chat_id=cid, sticker=sid)
			app.delete_messages(cid,mesid)



@app.on_message(filters.command("ид",prefixes=".") | filters.command("ID", prefixes=".") | filters.command("айди", prefixes="."))
def id(_,message):
	cid = message.chat.id
	myid = message.from_user.id
	try:
		yid= message.reply_to_message.from_user.id
		iddata = f"ваш ид: `{myid}` \nего ид:`{yid}`"
		try:
			sid= message.sticker.file_id
			iddata += "\nид стикера: ` {sid} `"
		except:
			f = 1
		message.reply(iddata)
	except:
		try:
			message.edit(f"ваш ид: `{myid}` \nид группы:`{cid}`")
		except:
			message.reply(f"ваш ид: `{myid}` \nид группы:`{cid}`")


##реакты
@app.on_message(filters.command("смех",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="🤣")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("сердце",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="❤️")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("лайк",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="👍")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("диз",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="👎")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("огонь",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="🔥")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("гавно",prefixes=",") | filters.command("говно",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="💩")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("клоун",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="🤡")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("шок",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="😱")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("стыд",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="😳") | filters.me
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("плачь",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="😭")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("крут",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="😎")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("поцелуй",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="💋")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("слеза",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="😢")
 	app.delete_messages(chat_id, message.id)
@app.on_message(filters.command("очкарик",prefixes=",") & filters.me)
def repid(client,message):
 	chat_id = message.chat.id
 	mesid = message.reply_to_message_id
 	client.send_reaction(
 	chat_id=chat_id,
 	message_id=mesid,
 	emoji="🤓")
 	app.delete_messages(chat_id, message.id)
 	
@app.on_message(filters.command("спам",prefixes=".") & filters.me)
def spam(_,message):
	app.delete_messages(message.chat.id,message.id)
	a = [0]
	b = 1
	c = 0
	d = ""
	chis = message.text.split(".спам ",maxsplit=1)[1]
	for i in chis:
		try:
			a += [int(i)*b]
			c += 1
		except:
			break
	for i in a:
		d += str(i)
	d = int(d)
	tbs = ""
	tbc = list(message.text)
	for i in range(7+c):
		tbc[i] =""
	for i in tbc:
		tbs+= i
	for i in range(d):
		app.send_message(message.chat.id,tbs)

@app.on_message(filters.command("рспам",prefixes=".") & filters.me)
def spam(_,message):
	app.delete_messages(message.chat.id,message.id)
	a = [0]
	b = 1
	c = 0
	d = ""
	chis = message.text.split(".рспам ",maxsplit=1)[1]
	for i in chis:
		try:
			a += [int(i)*b]
			c += 1
		except:
			break
	for i in a:
		d += str(i)
	d = int(d)
	tbs = ""
	tbc = list(message.text)
	for i in range(8+c):
		tbc[i] =""
	for i in tbc:
		tbs+= i
	for i in range(d):
		app.send_message(reply_to_message_id=message.reply_to_message.id, chat_id=message.chat.id, text=tbs)
@app.on_message(filters.command("logging",prefixes=".") & filters.me)
def to_log(_,message):
	global logging
	if logging==0:
		logging=1
		message.edit("✅")
	elif logging == 1:
		logging =0
		message.edit("❌")
	time.sleep(0.5)
	app.delete_messages(message.chat.id,message.id)
## логгинг

@app.on_message(filters.command("json",prefixes="."))
def json(_,message):
	try:
		message.edit(message.reply_to_message)
	except:
		try:
			message.reply(message.reply_to_message)
		except:
			try:
				os.system(f"echo {message.reply_to_message}")
			except:
				pass
logging = 1
@app.on_edited_message()
def edtd(_,edited_message):
	if logging == 1:
		try:
			with open(f"{edited_message.chat.first_name}[{edited_message.chat.id}]/{edited_message.id}.txt", "a") as file:
				file.write(f"\n{edited_message.from_user.username}[{edited_message.from_user.id}] изменил  сообщение[{edited_message.id}]:{edited_message.text},время изменения:{time.ctime()}")
				
		except:
				try:
					with open(f"{edited_message.chat.first_name}[{edited_message.chat.id}]/{edited_message.id}.txt", "w") as file:
						file.write(f"{edited_message.from_user.username}[{edited_message.from_user.id}] отправил сообщение[{edited_message.id}]:{edited_message.text},время отправки:{time.ctime()}")
				except:
					os.system(f"mkdir {edited_message.chat.first_name}[{edited_message.chat.id}]")
	
@app.on_message()
def alls(_,message):
	global logging
	try:
		cid = message.chat.id
		mid = message.id
		uid = message.from_user.id
		mt = message.text
	except:
		f=0
	if logging==1:
		try:
			with open(f"{message.chat.first_name}[{message.chat.id}]/{message.id}.txt", "a") as file:
				file.write(f"\n{message.from_user.username}[{message.from_user.id}] отправил сообщение[{message.id}]:{message.text},время отправки:{time.ctime()}")
				
		except:
				try:
					message.print("___")
					with open(f"{message.chat.first_name}[{message.chat.id}]/{message.id}.txt", "w") as file:
						file.write("{message.from_user.username}[{message.from_user.id}] отправил сообщение[{message.id}]:{message.text},время отправки:{time.ctime()}")
				except:
					os.system(f"mkdir {message.chat.first_name}[{message.chat.id}]")
				
	#app.update_profile(bio=time.ctime())
	try:
		r = open(f"{uid}-react.txt")
		rid = r.read()
		app.send_reaction(cid,mid,random.choice(rid))
	except:
		f =1
	try:
		if message.sender_chat.id in schid:
			message.reply_sticker("CAACAgIAAxkBAAEJschksfG3vkR2BpLRBDleMkCVD5Sb_AACiCoAAmkjqUl4U_fO0M-mvi8E")
	except:
		f = 0
	try:
		for word in mt:
			if word.startswith("краб") or word.endwith("краб") or word.startswith("rust") or word.starswith("раст"):
				message.reply_sticker(random.choice([]))
	except:
		f=0

app.run()
