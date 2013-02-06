#-*- coding: UTF-8 -*-
import urllib

url = 'http://img3.douban.com/view/photo/albumicon/public/p1805142917.jpg'
comicName = url.split('/')[-1]

image=urllib.URLopener()
image.retrieve(url,comicName) 