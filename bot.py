#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@ruks3
# Coded by ruks
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# Instagram : https://instagram.com/_v_go?utm_medium=copy_link
# github : https://github.com/mudiv
# ---------------------
# لا يحق لك بيع او سرقة البوت ونسبة اليك
# الرجاء عدم ازالة الحقوق لدعمنا لنشر المزيد
# user telegram @ruks3

import os,certifi
from pyrogram import Client,errors
import telebot
import threading
from telebot import types
import asyncio
from backend import app
from db import database
# user telegram @ruks3
DB = database()
App = app()
# user telegram @ruks3
# user telegram @ruks3
os.environ['SSL_CERT_FILE'] = certifi.where() 
api_id = ''
api_hash = ''
TELEGRAM_TOKEN="" 
bot = telebot.TeleBot(TELEGRAM_TOKEN, threaded=False,num_threads=55,skip_pending=True)
# user telegram @ruks3

# user telegram @ruks3
@bot.message_handler(commands=['admin'])
def Admin(message):
    # user telegram @ruks3
    AddAccount=types.InlineKeyboardButton("👤 ∶ اضافة حساب .",callback_data="AddAccount")
    # user telegram @ruks3
    Accounts=types.InlineKeyboardButton("👥 ∶ عدد الحسابات المسجلة .",callback_data="Accounts")
    # user telegram @ruks3
    inline = types.InlineKeyboardMarkup(keyboard=[[AddAccount],[Accounts]])

# user telegram @ruks3
    bot.send_message(message.chat.id,"""❧ اهلا وسهلا بك عزيزي الادمن .

⟡ ⋮ يمكنك تحكم في البوت من هنا .

⟡ ⋮ يمكنك اضافة اشتراك و حذف اشتراك أيضأ .
                     
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉""",reply_markup=inline)

@bot.message_handler(commands=['start'])
def start(message):
    # user telegram @ruks3
    Start = types.InlineKeyboardButton("▶️ ∶ بدء النقل .",callback_data="a1")
    inline = types.InlineKeyboardMarkup(keyboard=[[Start]])
    # user telegram @ruks3
    bot.send_message(message.chat.id,"""❧ اهلا وسهلا بك عزيزي المستخدم .

⟡ ⋮ يمكنك نقل اعضاء من اكروب الى اكروب بسرعة فائقة .

⟡ ⋮ يمكنك نقل اعضاء غير مخفي .
                     
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉""",reply_markup=inline)
    
# user telegram @ruks3
@bot.callback_query_handler(lambda call:True)
def call(call):
    if call.data =="Accounts":
        num = DB.accounts()
        # user telegram @ruks3
        msg=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"⟡ ⋮ عدد الحسابات المسجة : {num} .")
    if call.data =="AddAccount":
        # user telegram @ruks3
        msg=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="✠ ⊳ ارسل رقم الهاتف مع الترميز الدولي (..+).")
        bot.register_next_step_handler(msg, AddAccount)
        # user telegram @ruks3

    if call.data =="a1":
        msg=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="⟡ ⋮ قم بارسال يوزر الكروب المراد النقل منه .")
        bot.register_next_step_handler(msg, statement)
        # user telegram @ruks3

def statement(message):
    # user telegram @ruks3

    Fromgrob = message.text
    msg =bot.send_message(chat_id=message.chat.id,text="⟡ ⋮ قم بارسال يوزر الكروب المراد النقل اليه .")
    bot.register_next_step_handler(msg, statement2,Fromgrob)


def statement2(message,Fromgrob):
    # user telegram @ruks3
    Ingrob = message.text
    msg=bot.send_message(chat_id=message.chat.id,text="⟡ ⋮ الرجاء الانتظار ..  .")
    # user telegram @ruks3
    T = threading.Thread(target=asyncio.run,args=(App.GETuser(Fromgrob,Ingrob),))
    T.start()
    T.join()
    # user telegram @ruks3
    list = T.return_value
    numUser = len(list)
    bot.send_message(message.chat.id,f"""❧ تم اكتمال سحب يوزرات  .

⟡ ⋮ عدد المستخدمين : {numUser} .

⟡ ⋮ من مجموعة : {Fromgrob} .

⟡ ⋮ جاري ضافة الى مجموعة : {Ingrob} .

⟡ ⋮ الرجاء الانتظار... . """)
    T = threading.Thread(target=asyncio.run,args=(App.ADDuser(list,Ingrob,message.chat.id,bot),))
    T.start()
    # user telegram @ruks3
    
    
    
    
    


def AddAccount(message):
    # user telegram @ruks3
    try:         
        if "+" in message.text:
            # user telegram @ruks3
           
            bot.send_message(message.chat.id,"• قم بارسال الحساب مع الترميز الدولي .")
            _client = Client("::memory::", in_memory=True,api_id=api_id, api_hash=api_hash,lang_code="ar")
            _client.connect()
            # user telegram @ruks3
            SendCode = _client.send_code(message.text)
            Mas = bot.send_message(message.chat.id,"• قم بارسال الكود التحقق .")
            # user telegram @ruks3
            bot.register_next_step_handler(Mas, sigin_up,_client,message.text,SendCode.phone_code_hash,message.text)	
        else:
            Mas = bot.send_message(message.chat.id,"• قم بارسال الحساب مع الترميز الدولي .")
    except Exception as e:
        bot.send_message(message.chat.id,"ERORR : "+e)
# user telegram @ruks3

def sigin_up(message,_client,phone,hash,name):
    try:
        bot.send_message(message.chat.id,"الرجاء الانتظار....")
        _client.sign_in(phone, hash, message.text)
        bot.send_message(message.chat.id," ⊳ تم تسجيل الحساب بنجاح ✅ .")
        ses= _client.export_session_string()
        DB.AddAcount(ses,name,message.chat.id)
        # user telegram @ruks3
    except errors.SessionPasswordNeeded:
        Mas = bot.send_message(message.chat.id,"⊳ قم بإرسال الباسورد الحساب .")
        bot.register_next_step_handler(Mas, AddPassword,_client,name)	
       
# user telegram @ruks3
def AddPassword(message,_client,name):
    try:
        # user telegram @ruks3
        _client.check_password(message.text) 
        
        ses= _client.export_session_string()
        DB.AddAcount(ses,name,message.chat.id)
        try:
            _client.stop()
        except:
            pass
        bot.send_message(message.chat.id,"✠ ⊳ تم تسجيل الحساب بنجاح ✅ .")
    except Exception as e:
        print(e)
        # user telegram @ruks3
        try:
            _client.stop()
        except:
            pass
        bot.send_message(message.chat.id,f"ERORR : {e} ")
# user telegram @ruks3
# user telegram @ruks3
bot.infinity_polling(none_stop=True,timeout=15, long_polling_timeout =15)
