# encoding=utf-8

# categories.py
# zips category names and URLs into a nice OrderedDict
# (c) Jonne Saleva

from collections import OrderedDict
import re

# initialize categories and urls
categories = ["Yleinen", "Kotimaa","Politiikka", "Kaupunki", "Ulkomaat", 
"Talous", "Urheilu", "Kulttuuri","Ruoka",
"Elämä & Terveys", "Kuluttaja", "Tiede", "Autot", "Tekniikka", "Sunnuntai", "Kuukausiliite"]

urls = ["http://www.hs.fi/uutiset/rss/",
"http://www.hs.fi/rss/?osastot=kotimaa",
"http://www.hs.fi/rss/?osastot=politiikka",
"http://www.hs.fi/rss/?osastot=kaupunki",
"http://www.hs.fi/rss/?osastot=ulkomaat",
"http://www.hs.fi/rss/?osastot=talous",
"http://www.hs.fi/rss/?osastot=urheilu",
"http://www.hs.fi/rss/?osastot=kotimaa",
"http://www.hs.fi/rss/?osastot=ruoka",
"http://www.hs.fi/uutiset/osastoittain/rss?osastot=elama,koti,terveys,tyyli,matka,ihmiset",
"http://www.hs.fi/rss/?osastot=kuluttaja",
"http://www.hs.fi/rss/?osastot=tiede",
"http://www.hs.fi/rss/?osastot=autot",
"http://www.hs.fi/rss/?osastot=tekniikka",
"http://www.hs.fi/rss/?osastot=sunnuntai",
"http://www.hs.fi/rss/?osastot=kuukausiliite"]

urls = [re.sub("hs.fi/rss/", "hs.fi/uutiset/osastoittain/rss", url) for url in urls]

categoriesDict = OrderedDict(zip(categories,urls))
