#-*- coding: UTF-8 -*-
from flask import Flask
from flask import render_template,request,session

import feedparser
import MySQLdb
from douban_client import DoubanClient

from doubanAPIS.manager_doubanAPI import ManagerDoubanAPIS
import Settings
import db

doubanUser = ManagerDoubanAPIS()

dataObect = db.DB() 

def DoubanAuth():
	return doubanUser.authorize_url

def DoumaoAuth():
	session["code"] = ""
	# try:
	if "code" in request.args and request.args["code"]:
		session["code"] = request.args["code"]
	if session["code"]:
		user = doubanUser.getUserCurrent(session["code"])
		user_token = doubanUser.getUserToken()

		parmse = (user['name'],user['avatar'],user['loc_id'],user['loc_name'],user['alt'],user['id'],user['uid'],user_token)
		sql = "INSERT INTO user (name,avatar,locationID,location,url,doubanID,doubanUID,token)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
		dataObect.write(sql,parmse,True)

		if dataObect.write(sql,parmse) == 1:
			result = "success!"
		else:
			result = "Error!"

		result = user_token
	else:
		result = "Welecome to Doumao"
	return result
	# except Exception,e:
	# 	return e
