#!/usr/bin/python

print '#########################################################'
print '#                                                       #'
print '#                                                       #'
print '#                                                       #'
print '#     REVERSE IP ADMIN FINDER                           #'
print '#                         --Coded By Angelo King        #'
print '#                                                       #'
print '#                                                       #'
print '#########################################################'

import socket
import urllib
from bs4 import BeautifulSoup
import mechanize
import subprocess

site = raw_input('Enter the target url: ')
site = site.replace('http://','')
subprocess.call('clear', shell='True')

def getip(host):
	tx = socket.gethostbyname(host)
	return tx

def reverse(url):
	br = mechanize.Browser()
	br.open('https://hackertarget.com/reverse-ip-lookup/')
	br.select_form(nr=1)
	br.form['theinput'] = url
	br.submit()
	res = br.response().read()
	bt = BeautifulSoup(res, 'lxml')
	php = bt.find('pre')
	tl = php.get_text()
	file = open('ip.txt', 'w')
	file.write(tl)
	file.close()

def getdata():
	num_lines =sum(1 for line in open('ip.txt'))
	print 'Total domains found: ' + str(num_lines)
	print '-'*60
	came = open('ip.txt', 'r')
	for item in came:
		try:
			html = urllib.urlopen('http://'+item.strip()+'/admin')
			if html.code == 200:
				print '[+]'+'http://'+item.strip()+'/admin' 
		except:
			print '[+]'+'http://'+item.strip()+'/admin'+ ' Unable to connect'

def main():
	tf = getip(site)
	print '-'*60
	print 'Please wait while scanning target url: ' + tf
	print '-'*60
	reverse(site)
	getdata()

if __name__ == '__main__':
    main()
	
	
