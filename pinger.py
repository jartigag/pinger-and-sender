#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# to log output, RUN WITH:
# nohup python3 pinger.py > pingeroutput.log &

from bs4 import BeautifulSoup
import urllib.request
from time import sleep
from datetime import datetime
from telegram import Bot

oclock = 1
bot = Bot(token='123456789:mytelegramto-ken')
bot.chat_id='001122334'

def message(text):
	bot.send_message(chat_id=bot.chat_id, text=text)

while True:
	r = urllib.request.Request("https://websi.te",
		headers={'Cookie':"yourSession=c0ok1eV4lu3"})
	html = urllib.request.urlopen(r).read()
	soup = BeautifulSoup(html, 'html.parser')

	# parse HTML to find course content
	sections = soup.find_all('span', {'class':'instancename'})

	'''
	here i'm checking if there's more than 4 sections in a moodle site,
	just as an example. soup.find() and following conditional statement
	must be adapted to your particular case
	'''

	if len(sections)==4: # if nothing changes
		print(datetime.now().strftime('%a, %d %b %Y %H:%M:%S')+' - nothing changes on websi.te')
		if oclock==60:
			message('nothing changes on websi.te')
			oclock=1
		else:
			oclock+=1

	else: # if there's news
		list = []
		for s in sections:
			list.append(s.text)
		print(datetime.now().strftime('%a, %d %b %Y %H:%M:%S')+' sth new in websi.te! https://websi.te '+str(list))
		message('sth new in websi.te! https://websi.te '+str(list))

	sleep(60)
