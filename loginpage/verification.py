import os
import math
import random
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
import smtplib
root3=  Tk()
root3.geometry('790x512')
root3.resizable(0,0)
root3.title('signup Page')


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
def verify_otp(OTP,a):
    if OTP == a:
        return 1
    else:
       return 0
        


def signup_page():
    root3.destroy()
    import signup


def login_page():
    root3.destroy()
    import login
    
    
    
def connect():
    try:
        con =  mysql.connector.connect(host = 'localhost',user = 'root',passwd ='Giri12345@')
        mycursor=con.cursor()
    except:
        messagebox.showerror('Error','database connection is not available')
        return
    qurey = 'use login'
    mycursor.execute(qurey)
        
        
        
    query = 'SELECT email from user_details order by id desc limit 0,1'
    mycursor.execute(query)
    row = mycursor.fetchone()
    # print(row)
    
    x = gen_otp(row[0])
    return x
    # if y== 1:
    #     messagebox.showinfo('success','otp verified successfully')
    #     login_page()
    # else:
    #     messagebox.showerror('error','otp verification failed')
    #     signup_page()





def on_enter2(event):
    if User.get() == 'enter otp':
        User.delete(0,END)


def verification():
    if  User.get() =='' or User.get() == 'enter otp':
        messagebox.showerror('error','please enter otp')
    else:
        
        z = verify_otp(y,User.get())
        if z == 1:
            messagebox.showinfo('success','otp verified successfully')
            login_page()
        else:
            messagebox.showerror('error','otp verification failed')
            signup_page()
        # if  otp.verify_otp(row,verinum) == 1:
        #     login_page()
        # else:
        #     messagebox.showerror('error', 'account not created')
        #     signup_page()
            
            
bgImage = ImageTk.PhotoImage(file="bg.jpg")

bgLabel = Label(root3,image=bgImage)
bgLabel.place(x=0,y=0)


heading = Label(root3,text="verify your account here",font=('Courier New',15,'bold'),bg ='white',fg ="firebrick1")
heading.place(x=454,y=50)


heading = Label(root3,text="enter the otp send to your mobile no",font=('Courier New',10,'bold'),bg ='white',fg ="blue2")
heading.place(x=454,y=150)

User = Entry(root3, width = 25,font=('Courier New',10),bd =2,fg ="firebrick1")
User.place(x=500,y=190)
User.insert(0,'enter otp')
User.bind('<FocusIn>',on_enter2)
# Frame(root3,width=200,height=1,bg = "firebrick1").place(x=500,y=210)


verify = Button(root3,text = "verify",font=('Courier New',12),bg = 'red',fg = 'white',activebackground='white',cursor='hand2',command=verification)
verify.place(x = 560,y =220)



resend = Button(root3,text = "resend otp",font=('Courier New',10),bg ='white',fg = 'blue2',bd = 0,activebackground='white',cursor='hand2')
resend.place(x = 555,y =250)


y = connect()

root3.mainloop()