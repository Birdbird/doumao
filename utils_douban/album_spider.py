#-*- coding: UTF-8 -*-
from pyquery import PyQuery as pq
from lxml import etree
import urllib

import db

# import codes.db

dataconn = db.DB()


def getAlbumLike(url=""):
	if url != "":		
		d = pq(url=url)
		q = d('.fav-list li')
		for item in q:
			item_pq = pq(item)
			if item_pq('.fav-thumb a'):
				try:
					if "/photos/album" in item_pq('.fav-thumb a').attr('href'):
						authUIDInfo = pq(item_pq('.fav-thumb a').attr('href'))
						authUID = authUIDInfo('.info ul li a').attr('href').split('/')[-2]
						# print 'authUID:',authUID
						parms = (item_pq('.fav-thumb a').attr('href'),item_pq('.fav-thumb a img').attr('src'),item_pq('.fav-thumb a').attr('title'),item_pq('.fav-main .abstract').text(),authUID)
						sql = "INSERT INTO album (url,cover,name,des,authUID)VALUES(%s,%s,%s,%s,%s)"
						result = dataconn.write(sql,parms,True)
						if result == 1:
							print "OK",authUID
						else:
							print "wrong",authUID
				except:
					print 'Not Found.',authUID

def getAllAlbumLikes():
	sendurl = ""
	url = "http://www.douban.com/people/playwithcat/likes"
	for i in xrange(35,104):
		sendurl = url + "?start=" + str(i*15) 
		print 'url:',sendurl
		getAlbumLike(sendurl)

if __name__ == "__main__":
	getAllAlbumLikes()
