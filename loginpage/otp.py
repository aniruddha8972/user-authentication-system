import os
import math
import random
import smtplib
from tkinter import messagebox
def gen_otp(emailid):
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
    msg= otp   
    s = smtplib.SMTP('smtp.gmail.com', 587)    
    s.starttls()
    s.login("anig7367@gmail.com", "badm qoti ijpt raqq")
    s.sendmail('&&&&&&&&&&&',emailid,msg)
    return OTP

def verify_otp(x,a):
    if a == x:
        return 1
    else:
       return 0


a = gen_otp('girianiruddha4@gmail.com')
x = input("enter the otp")
print(verify_otp(x,a))