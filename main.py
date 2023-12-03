#pylint:disable=W0702
#pylint:disable=E0102
import os
from pyrogram import Client, filters

from pyrogram.raw.functions.messages import GetStickerSet

from pyrogram.raw.types import InputStickerSetShortName
from pyrogram.types import Sticker

import time
import random
def parser(a):
	z =0
	a =random.randint(0,1)
	if a ==0:
		while z!=2:
			try:
				anek = app.get_messages(-1001574767565,random.randint(1,2102))
				try:
					a = anek.entities.url
				except:
					z =1
				if len(anek.text)> 1:
					if z ==1:
						return anek.text
						z=2
			except:
				pass
	elif a==1:
		while z!=2:
			try:
				anek = app.get_messages(-1001966027405,random.randint(1,484))
				try:
					a = anek.entities.url
				except:
					z =1
				if len(anek.text)> 1:
					if z ==1:
						return anek.text
						z=2
			except:
				pass
		
	

api_id = 19576945
api_hash = "07fca730186bb632bcb8e4f78302a84c"

app = Client("my_account", api_id=api_id, api_hash=api_hash)
schid = [-1001396952381]

@app.on_message(filters.command("мем",prefixes="."))
def mem(_,message):
	file = open(f"{os.getcwd()}/ids/memes/1.txt")
	message.reply_document(file.read())
	
	
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
def anik(_,message):
	message.reply(parser(1))
	
@app.on_message(filters.command("тю",prefixes=""))
def tyu(_,message):
	message.reply("тю")





	##няшк милашк
@app.on_message(filters.command("🔼миленько🔼", prefixes="") | filters.command("мило",prefixes="") | filters.command("миленько",prefixes="") | filters.command("милашка",prefixes=""))
def da(_, message):
	message.reply_sticker(random.choice([ "CAACAgIAAxkBAAEJLAtkd6HWbyIH9f8Lys3A1QfPaG4uHgACzjEAAi6EuUv_ywzxqqyoii8E"]))
	
@app.on_message(filters.command("принт",prefixes="."))
def prent(_,message):
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
			rtbp =""
	ptbp =""
	for i in ortxt:
		ptbp += str(i)
	message.edit(ortxt)
	
	##вентилятор
@app.on_message(filters.command("вентилятор", prefixes=""))
def da(_, message):
	sid = random.choice([ "CAACAgIAAxkBAAEJF1JkbhHc3TU_AYKVby5MhaVSolzKFgACiCoAAmkjqUl4U_fO0M-mvi8E","CAACAgIAAxkBAAEJNihkfUsKtOvxZkiZehOjt2hIvWiMBwACVCkAAs42yUpdSNnGC9W_ci8E"])
	message.reply_sticker(sid)
	
	##да
@app.on_message(~filters.me & filters.command("да", prefixes="") & filters.private)
def da(_, message):
	if message.text == "да":
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

sticks = ['nebagibuappu_by_fStikBot','kitski2023_by_fStikBot', 'kitski23_by_fStikBot','kitttens20232_by_fStikBot', 'kitski202310_by_fStikBot', 'kitttens20234_by_fStikBot', 'kitttens20235_by_fStikBot', 'kitttens20236_by_fStikBot', 'kitttens20237_by_fStikBot', 'kitten202315_by_fStikBot', 'kitten202316_by_fStikBot', 'kitten202317_by_fStikBot', 'kitten202318_by_fStikBot', 'kitten202319_by_fStikBot', 'kitten202320_by_fStikBot', 'kitten202321_by_fStikBot', 'kitten202322_by_fStikBot', 'kitten202323_by_fStikBot',]
@app.on_message(filters.command(["кот","кіт"],prefixes="."))
async def hello(_, message):
    try:
        # print(message)
        
        if 1==1:
            sticker_set = await app.invoke(
                GetStickerSet(
                    stickerset=InputStickerSetShortName(short_name=random.choice(sticks)),
                    hash=0
                )
            )
            sticker = random.choice(sticker_set.documents)
            if message.chat.id != -1001862327325:
            	await app.send_sticker(message.chat.id, sticker=(
             	   await Sticker._parse(app, sticker, {type(i): i for i in sticker.attributes})).file_id,
                                   reply_to_message_id=message.id)

             	
    except Exception as e:
        print(e)		
		
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
		
def de(tittle):
	output =""
	for i in tittle:
		output+=chr(ord(i)+200)
	return output

def en(tittle):
	output =""
	for i in tittle:
		output+=chr(ord(i)-200)
	return output
				
								
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
			sid= message.reply_to_message.sticker.file_id
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
		try:
			app.send_message(reply_to_message_id=message.reply_to_message.id, chat_id=message.chat.id, text=tbs)
		except:
			app.send_message(message.chat.id,tbs)

		

## логгинг

@app.on_message(filters.command("json",prefixes="."))
def json(_,message):
	try:
		print("{message.reply_to_message}")
	except:
		pass
	try:
		message.edit(message.reply_to_message)
	except:
		try:
			message.reply(message.reply_to_message)
		except:
			pass

@app.on_message()
def alls(_,message):
	try:
		cid = message.chat.id
		mid = message.id
		mt = message.text
	except:
		pass
	try:
		uid = message.from_user.id
	except:
		pass
	try:
		r = open(f"{uid}-react.txt")
		rid = r.read()
		app.send_reaction(cid,mid,random.choice(rid))
	except:
		pass
	try:
		if message.sender_chat.id in schid:
			message.reply_sticker(f"CAACAgIAAxkBAAEJschksfG3vkR2BpLRBDleMkCVD5Sb_AACiCoAAmkjqUl4U_fO0M-mvi8E")
	except:
		pass

	#app.update_profile(bio=time.ctime())
	
	
	try:
		for word in mt:
			if word.startswith("краб") or word.endwith("краб") or word.startswith("rust") or word.starswith("раст"):
				message.reply_sticker(random.choice([]))
	except:
		pass

app.run()
