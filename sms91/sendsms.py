import json
import requests
import  random
import json

class SMSClient:

	def initialize(self, key, sender,lenn=4):
		# if lenn is None or lenn <4:
		# 	self.length = 4
		# else:
		# 	self.length = lenn;
			
		self.otp = "Your otp is {{otp}}. Please do not share it with anybody"
		self.headers = {'Content-type': 'application/json', 'authkey':key}
		self.payload = {"route": "4","country": "91","sender": "SOCKET",}
		if len(sender) == 6 and type(sender) == str:
			self.payload["sender"]=sender
		# self.key = key
		self.url = "https://api.msg91.com/api/v2/sendsms"

	def changeOtp(self,data):
		if "{{otp}}" in data:
			self.otp = data
		else:
			raise ValueError("add {{otp}} in the string") 

	def sendMessgae(self,data,phno):
		self.payload["sms"] = [{"message":data,"to":phno}]
		self.sendRequest()

	def sendOtp(self,phno):
		rand = random.randrange(10**(self.length-1), 10**self.length)
		data = self.otp.replace("{{otp}}",str(rand))
		self.payload["sms"] = [{"message":data,"to":phno}]

	def sendRequest(self):
		r = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
		print(r.content)