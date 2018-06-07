#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# IMPORTANT! it only works on python2
# based on email-osint-ripper by @Quantika14
# i tried to port it to python3, but it didn't work..

import mechanize,cookielib
from bs4 import BeautifulSoup

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
'''
here i'm filling and sending email-passwd to linkedin, just as an example.
you must be adapted this to your particular case
'''
def login(email):
	r = br.open('https://www.linkedin.com')
	br.select_form(nr=0)
	br.form["session_key"] = email
	br.form["session_password"] = "123456"
	br.submit()
	if "captcha" in br.response().geturl():
		print("\033[93mcaptcha..\033[0m")
	else:
		html = br.response().read()
		soup = BeautifulSoup(html, "html.parser")
		for data in soup.find_all("span", {"class", "error"}):
			if "password" in str(data):
				print(email,"\033[92m EXISTS\033[0m in linkedin")
			if "recognize" in str(data):
				print(email,"\033[93m DOESN'T\033[0m exist in linkedin")

def main():
	file = open("emails.txt", 'r')
	for email in file.readlines():
		login(email.replace("\n", ""))

if __name__ == "__main__":
	main()
