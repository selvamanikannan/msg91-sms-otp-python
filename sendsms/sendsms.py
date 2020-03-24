import json
import requests
import  random
import json

class sendsms:
	def __init__(self, key, sender,lenn):
		if self.lenn is None or <4:
			self.length = 4
		else:
			self.length = lenn;
			
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

	def sendOtp(self,phno):
		rand = random.randrange(10**(self.length-1), 10**self.length)
		data = self.otp.replace("{{otp}}",str(rand))
		self.payload["sms"] = [{"message":data,"to":phno}]

	def printt(self):
		r = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
		print(r.content)
		print(self.payload)
		print(self.headers)


if __name__ == '__main__':
	otpobj = sendsms('313526A2RuWoJ94TkI5e20af18P1','selvam',6)
	otpobj.sendMessgae('vanakkam da maplaa',["9659872073","8428720872"])
	otpobj.printt()
	otpobj.sendOtp(["9659872073","8428720872"])
	otpobj.printt()
	otpobj.changeOtp("tahmbi unga otp inthanga {{otp}}")
	otpobj.sendOtp(["1111","234"])
	otpobj.printt()

