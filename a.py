from sms91.sendsms import SMSClient

cli = SMSClient()

cli.initialize("313526AEfebhQ85e7a1260P1","SELVAM",6)
cli.sendMessgae("hi",["9659872073"]) 

print("hi")