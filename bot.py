# -*- coding: utf-8 -*-
import sys
import os
import socket
import time
import string
from imgurpython import ImgurClient

def uploadToImgur(path):
	CLIENT_ID = os.environ.get('CLIENT_ID')
	CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

	try:
		client = ImgurClient(CLIENT_ID, CLIENT_SECRET)
		image = client.upload_from_path(path)
		return image['link']
	except Exception as e:
		return "Ocorreu um erro: " + e

HOST="localhost"
PORT=6667
NICK="ALEXANDRE"
IDENT="bot"
REALNAME="botdasilva"
readbuffer=""
CHANNEL = "#all"

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))

connected = False
while not connected:
	readbuffer = readbuffer+s.recv(1024)
	temp = string.split(readbuffer, "\n")
	readbuffer = temp.pop()

	if str(temp).find(NICK) != -1:
		s.send("JOIN %s\r\n" % (CHANNEL))
		connected = True

s.send("PRIVMSG %s voltei galera\r\n" % (CHANNEL))

while 1:
	readbuffer=readbuffer+s.recv(1024)
	temp=string.split(readbuffer, "\n")
	readbuffer=temp.pop( )

	for line in temp:
		line=string.rstrip(line)
		line=string.split(line)


		if(line[0]=="PING"):
			s.send("PONG %s\r\n" % line[1])

		else:
			if (line[1] == "PRIVMSG"):
				if(line[3] == ":!comandos"):
					s.send("PRIVMSG %s meus comandos: !sp !mat1 !chr0m1ng !fezMerda !disney\r\n" % (CHANNEL))
				elif(line[3] == ":!sp"):
					s.send("PRIVMSG %s Sэmi.pяo FTW\r\n" % (CHANNEL))
				elif(line[3] == ":!mat1"):
					s.send("PRIVMSG %s Esse tal do mat1 só faz merda slk\r\n" % (CHANNEL))
				elif(line[3] == ":!chr0m1ng"):
					s.send("PRIVMSG %s o tal do chr0m1ng NTC\r\n" % (CHANNEL))
				elif(line[3] == ":!fezMerda"):
					if(len(line) > 4):
						s.send("PRIVMSG %s ihhh ah lá, %s fez merda outra vez\r\n" % (CHANNEL, line[4]))
					else:
						s.send("PRIVMSG %s Ai vc fez merda né meua migo\r\n" % (CHANNEL))
				elif any(NICK in string for string in line):
					s.send("PRIVMSG %s Fala tu %s, me chamou? Para saber meus comandos só digitar !comandos\r\n" % (CHANNEL, line[0].split("!")[0].replace(":", "")))
				elif(line[3] == ":!disney"):
					if(len(line) > 4):
						s.send("PRIVMSG %s %s ta na disney!\r\n" % (CHANNEL, line[4]))
					else:
						s.send("PRIVMSG %s Ai vc ta na disney né\r\n" % (CHANNEL))
				elif(line[3] == ":!mudarNomeBot"):
					if(len(line) > 4):
						if(line[0].split("!")[0] == ":chr0m1ng"):
							NICK = line[4].replace(":", "")
							s.send("NICK %s\r\n" % (NICK))
						else:
							s.send("PRIVMSG %s Sai fora %s otario, tu não manda em mim\r\n" % (CHANNEL, line[0].split("!")[0].replace(":", "")))
				elif(line[3] == ":!enviarImg"):
					if(len(line) > 4):
						s.send("PRIVMSG %s Ai o link da sua imagem meu persa: %s\r\n" % (CHANNEL, uploadToImgur(line[4])))
					else:
						s.send("PRIVMSG %s Coloca o path da imagem arrombed\r\n" % (CHANNEL))
