#-*- coding: UTF-8 -*-
from douban_client import DoubanClient

from codes import Settings

class ManagerDoubanAPIS : 
	'''
		this is a class for managering something control about Douban
	'''
	def __init__(self):
		self.API_KEY = Settings.API_KEY
		self.API_SECRET = Settings.API_SECRET
		self.REDIRECT_URI = Settings.REDIRECT_URI

		self.SCOPE = Settings.SCOPE

		self.client = DoubanClient(self.API_KEY, self.API_SECRET, self.REDIRECT_URI, self.SCOPE)

		self.authorize_url = self.client.authorize_url
	
	def getUserCurrent(self,code):
		self.client.auth_with_code(code)
		return self.client.user.me

	def getUserToken(self):
		return self.client.client.token