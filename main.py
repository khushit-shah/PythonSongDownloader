from bs4 import BeautifulSoup
import requests as req


songUrl = []
baseLink = "https://omarmik.blogspot.com/p/blog-page_26.html?m=1"

basePage = req.get(baseLink).text
# print(basePage)

soup = BeautifulSoup(basePage, "html.parser")

for link in soup.find_all('a'):
	try:
		if(link["href"].__contains__(".mp3")):
			songUrl.append(link["href"])
			# print(link.href)
	except:
		continue

import os

basePath = "/path/to/folder/"

for link in songUrl:
	# Extract the file name:
	fileTitle = link.split("/")[-1].split("?")[0]
	try:
		# check if the file is already there?
		if os.path.exists(basePath + fileTitle) and os.path.isfile(basePath + fileTitle):
			print(fileTitle, "is Already Downloaded")
			continue

		file = open(basePath + fileTitle, "wb")
		print("Started Downloading",fileTitle+"...")
		b = req.get(link).content
		file.write(b)
		file.close()
		print("Successfully Downloaded",fileTitle+"!")
	except:
		os.remove(basePath + fileTitle)
		print("Can't Download", link)
