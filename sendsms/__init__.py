from sendsms import sendsms


otpobj = sendsms('313526A2RuWoJ94TkI5e20af18P1','selvam',6)
otpobj.sendMessgae('vanakkam da maplaa',["9659872073","8428720872"])
otpobj.printt()
otpobj.sendOtp(["9659872073","8428720872"])
otpobj.printt()
otpobj.changeOtp("tahmbi unga otp inthanga {{otp}}")
otpobj.sendOtp(["1111","234"])
otpobj.printt()


