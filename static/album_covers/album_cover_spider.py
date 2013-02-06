#-*- coding: UTF-8 -*-
import urllib
import db

dataconn = db.DB()

def getCovers():
	sql = "SELECT cover FROM album"
	result = dataconn.read(sql)

	for item in result:
		url = item['cover']
		comicName = url.split('/')[-1]
		print 'url:',url
		print 'comicName:',comicName

	image=urllib.URLopener()
	image.retrieve(url,comicName) 

if __name__ == "__main__":
	getCovers()