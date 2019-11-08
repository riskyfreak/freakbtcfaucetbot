from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from bs4 import BeautifulSoup
from time import sleep
import requests, json, re, sys, os, time

if not os.path.exists('session'):
    os.makedirs('session')

api_id = 1121458
api_hash = '546ffed83f4c5a9c89a42f2e88f13d74'
phone_number = '+6283159415465'

client = TelegramClient('session/'+phone_number,api_id,api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number,input('Masukan Code Anda >> '))
    except SessionPasswordNeededError:
        password = input('Masukan Password 2fa Anda >> ')
        me = client.start(phone_number,password)

myself = client.get_me()
print(myself)

channel_username = '@BTC_Faucet_v7_bot'
channel_entity = client.get_entity(channel_username)
for ulang in range(999999999):
    print ('Mencoba Mengambil Faucet')
    client.send_message(entity=channel_entity,message='💦 Faucet')
    sleep(3)
    message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
    if message_history.messages[0].message.find('Congratulation! You've got') != -1:
        print ('Sukses Mendapatkan Coin!')
    time.sleep(30)