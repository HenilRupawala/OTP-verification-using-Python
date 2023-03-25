import math
import random
import smtplib

digits = '0123456789'

OTP = ''

for i in range(6):
    OTP += digits[math.floor(random.random()*10)]

otp = f'''Subject: Please verify your device
{OTP} is you OTP'''
msg = otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('Your_Gmail_ID','App_Password') #Read the instruction from Readme.md for login and mail through your Gmail Account.
emailid = input('Enter Your Email: ')
s.sendmail('&&&&&&&&&&&&&',emailid,msg)
a = input('Enter Your OTP: ')

if a == OTP:
    print('OTP is successfully verified.')
else:
    print('OTP is either Invalid or Expired.')
