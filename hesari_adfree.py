# coding=utf-8

#############################
# 		hesari_noads.py		#
#		(c) j0ma, 2015		#
#############################

# import libs
import feedparser as fp
from categories import categoriesDict
from collections import OrderedDict
from textwrap import fill, wrap
from lxml import html
import requests
import time
import sys
import re
import os

# define functions

def printWelcome():
	os.system('clear')
	thingsToPrint = ["\n******************************\n",
					"Lue HS.fi:n sisältöä komentoriviltäsi ilman mainoksia!",
					"(c) j0ma, 2015\n",
					"HUOM: Kaikki uutiset: \n(c) Helsingin Sanomat, a Sanoma Company 2015",
					"\n******************************\n"]
	for thing in thingsToPrint:
		print thing
		time.sleep(.05)

def printCategories(categories):
	"""
	Prints available news categories in Terminal.
	
	categories: a list of news categories
	returns: None
	"""
	assert type(categories) == list
	print "Valitse kategoria:"
	for i, cat in enumerate(categories):
		print str((i+1)) + ". " + categories[i]
		time.sleep(.05)

def getUserChoice(listToBeChosenFrom):
	"""
	returns: an int corresponding to the chosen number
	"""
	userChoice = "blah"
	while userChoice not in [str(i) for i in xrange(1,len(listToBeChosenFrom)+1)] or int(userChoice) <= 0:
		message = '\nValitse syöttämällä numero [1-%i] tai "t" aloittaaksesi alusta: ' % len(listToBeChosenFrom)
		userChoice = raw_input(message)
		if userChoice == "t":
			return "t"
		if userChoice not in [str(i) for i in xrange(1,len(listToBeChosenFrom)+1)] or int(userChoice) <= 0:
			print "Syötä oikeanlainen numero! [1-%i]" % len(listToBeChosenFrom)
	return int(userChoice)

def getTitlesAndUrls(categoriesDict, chosenCategory):
	"""
	categoriesDict: OrderedDict object
	chosenCategory: a string

	returns: an OrderedDict of titles and links
	"""
	assert type(categoriesDict) == OrderedDict
	my_url = categoriesDict[chosenCategory]
	hesari_feed = fp.parse(my_url)
	titles = [post.title for post in hesari_feed.entries]
	links = [post.link for post in hesari_feed.entries]
	return OrderedDict(zip(titles, links))

def printHeadlines(chosenCategory, titles):
	"""
	chosenCategory: string indicating user's category of userChoice
	titles: a list of headlines
	"""
	os.system('clear')
	print "\n******************************\n"
	print "Uusimmat uutiset aiheesta %s:\n" % chosenCategory
	for i, title in enumerate(titles):
		print str(i+1) + ". " + re.sub("&nbsp;", "", re.sub("&shy;", "", title))
		time.sleep(.05)

def getArticle(chosenTitle, titlesUrlsDict):
	"""
	chosenTitle: user-chosen article title (string)
	titlesUrlsDict: OrderedDict of artcicle titles and URLs
	"""
	sourcecode = requests.get(titlesUrlsDict[chosenTitle]).text
	tree = html.fromstring(sourcecode)

	# case: blog post
	if "blogit.hs.fi" in titlesUrlsDict[chosenTitle]:
		xpath = tree.xpath('//*[@class="entry"]//p')
	
	# case: nyt.fi
	elif "nyt.fi" in titlesUrlsDict[chosenTitle]:
		xpath = tree.xpath('//*[(@id = "a1305987325037")]//*[contains(concat( " ", @class, " " ), concat( " ", "text", " " ))]//p')

	# case: normal article
	else:
		xpath = tree.xpath('//*[(@id = "article-text")]//p')

	# print user-chosen article
	os.system('clear')
	articleHeader = "Otsikko:\n" + chosenTitle + "\n\nTeksti:\n" 
	xpathTextContent = [elem.text_content() for elem in xpath if elem.text_content() != ""]
	print articleHeader

	#print xpathTextContent
	for line in xpathTextContent:
		print fill(line, width=80) + "\n"
		time.sleep(0.05)

def main():
	
	# initialize loop
	loopAgain = True

	# loop
	while loopAgain:

		# print welcome
		printWelcome()

		# print categories
		printCategories(categoriesDict.keys())

		# get user's chosen category
		userCategoryNumber = getUserChoice(categoriesDict.keys())
		if userCategoryNumber == "t":
			continue
		chosenCategory = categoriesDict.keys()[userCategoryNumber-1]

		# import feed, print titles
		titlesUrlsDict = getTitlesAndUrls(categoriesDict, chosenCategory)
		
		# print titles
		printHeadlines(chosenCategory, titlesUrlsDict.keys())

		# ask user to choose a title
		userTitleNumber = getUserChoice(titlesUrlsDict.keys())
		if userTitleNumber == "t":
			continue
		chosenTitle = titlesUrlsDict.keys()[userTitleNumber-1]
		
		# get article
		getArticle(chosenTitle, titlesUrlsDict)

		# show another article?
		showAnother = ""
		while showAnother not in ["k", "e"]:
			showAnother = raw_input("Haluatko lukea toisen uutisen? [k/e] ").lower()

		if showAnother == "k":
			os.system("clear")
		else:
			loopAgain = False

	sys.exit("\nKiitos!\n")

if __name__ == "__main__":
	main()
