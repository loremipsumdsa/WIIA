# What Is It About
# An automatic brainstorming to find correlation between concepts
# Programmed Paul Nautré

import wikipedia as wiki
import numpy as np
import bs4
import operator
from collections import OrderedDict
import sys
import time

about = {} # That dictionnary will contain all concepts related to the start one
blackList={"ISBN (identifier)","Doi (identifier)"} # List of subject to avoid : statistic error detected by learn function

def wiia(word,depth): # main function of the process : launch an analys, then short it, then print it
	global about
	nxtWord(word,0,depth)
	outOfSubject()
	short()
	out()

def nxtWord(word, stage, depth): # work with treatment function for a recursive code witch read page and extract keyword while stage is different from depth
	global about

	if stage == depth:
		return
	treatment(word, stage, depth)


def treatment(word,stage, depth): # read page, extract keyword and calculate it score, then read keyword's page...
	global about
	sc = score(stage)

	try :
		links = wiki.page(word).links
	
	except (wiki.exceptions.DisambiguationError,wiki.exceptions.PageError): # Marginal data loss are not important as it is not on the first stage
		if stage == 0:
			print("Warning : Unable to find First level concept") # It could cause total fail on a search, protected on a learn session
		return
	for l in links:
		
		try : 
			about[l]+=sc
		
		except KeyError:
			about[l]=sc
		
		nxtWord(l,stage+1,depth)

def score(stage): # that should be the most important part of the code as it is the main statistic's application 
	return 1/(stage+1)


def short(): # short keyword by proximity rate and calibrate int %
	global about
	
	about = OrderedDict(sorted(about.items(), key=lambda x: x[1], reverse = True))
	
	maxC = 0;
	for w in about.keys():
		if maxC == 0:
			maxC =about[w]
		about[w]/=(maxC/100)


def out(): # Basically a print  
	for w in about.keys():	
		print(w+" : " +str(about[w]))


def outOfSubject(): # Remove keywords presents in blacklist
	global about

	for bl in blackList:
		try:
			del about[bl]
		except:
			pass



def learn(session, depth, corresThreshold, recurThreshold): # Find keywords witch are statistic aberration
	global about

	learnedBL = {} # Temporary potential blacklist  

	for i in range(session):
		about.clear()
		try:
			p=wiki.random()
			wiki.page(p)
			nxtWord(p,0,depth)
			short()

			for w in about:
				if about[w] >= corresThreshold:
					try :
						learnedBL[w]+=1;
					except KeyError:
						learnedBL[w]=1
		
		except (wiki.exceptions.DisambiguationError,wiki.exceptions.PageError):
			session-=1

	for w in learnedBL:
		if (learnedBL[w]/(session/100)) >= recurThreshold:
			print(w)

def main(): # Read parameter to decide what to execute : search on additionnal parameter, learn or return error

	print("What is it about ?")
	print("By Paul Nautre")
	print("Made in Dol de Bretagne")
	print("-----------------------------")

	try:

		if sys.argv[1]=="learn":
			t = str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)
			print(t+" : Running learn session...")
			print("---------------------------------")
			learn(1,2,30,40)
		
		else:
			word=''
			for i in range(1,len(sys.argv)):
				word+=str(sys.argv[i])+" "
			t = str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)
			print(t+" : Searching matches on "+ word)
			print("---------------------------------")

			wiia(word,2)

	except SyntaxError:
		print("Arguments error, please be specific")
		return
	t = str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)
	print("---------------------------------")
	print(t+" : Treatment ended, Success")	

main()