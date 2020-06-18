import wikipedia as wiki
import numpy as np
import bs4
import operator
from collections import OrderedDict
import sys

about = {}
blackList={"ISBN (identifier)","Doi (identifier)"}
learnedBL = {}

def wiia(word,depth):
	global about
	nxtWord(word,1,depth)
	outOfSubject()
	short()
	out()

def nxtWord(word, stage, depth):
	global about

	if stage == depth:
		return
	treatment(word, stage, depth)


def treatment(word,stage, depth):
	global about
	sc = score(stage)

	try :
		links = wiki.page(word).links
	
	except (wiki.exceptions.DisambiguationError,wiki.exceptions.PageError):
		#faire une exeption sur les pages qui n'existe pas ou qui sont ambigues
		return
	for l in links:
		
		try : 
			about[l]+=sc
		
		except KeyError:
			about[l]=sc
		
		nxtWord(l,stage+1,depth)

def score(stage):
	return 1/stage


def short():
	global about
	
	about = OrderedDict(sorted(about.items(), key=lambda x: x[1], reverse = True))
	
	maxC = 0;
	for w in about.keys():
		if maxC == 0:
			maxC =about[w]
		about[w]/=(maxC/100)


def out():
	for w in about.keys():	
		print(w+" : " +str(about[w]))


def outOfSubject():
	global about

	for bl in blackList:
		try:
			del about[bl]
		except:
			pass



def learn(session, depth, corresThreshold, recurThreshold):
	global about
	global learnedBL

	for i in range(session):
		about.clear()

		nxtWord(wiki.random(),1,depth)
		short()

		for w in about:
			if about[w] >= corresThreshold:
				try :
					learnedBL[w]+=1;
				except KeyError:
					learnedBL[w]=1
	
	for w in learnedBL:
		if (learnedBL[w]/(session/100)) >= recurThreshold:
			print(w)

def main():
	print("What is it about ?")
	print("By Paul Nautre")
	print("Made in Dol de Bretagne")
	print("-----------------------------")

	try:

		if sys.argv[1]=="learn":
			print("Running learn session...")
			learn(500,3,40,50)
		else:
			print("Searching for correspondences...")
			word=''
			for i in range(1,len(sys.argv)):
				word+=str(sys.argv[i])
			print(word)
			wiia(word,3)
	except IndexError:
		print("Arguments error, please be specific")
		return
	print("Treatment ended, Success")	

main()