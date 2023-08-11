import mysql.connector

con =  mysql.connector.connect(host = 'localhost',user = 'root',passwd ='Giri12345@')
mycursor=con.cursor()
qurey = 'use login'
mycursor.execute(qurey)
query = 'SELECT email from user_details order by id desc limit 0,1'
mycursor.execute(query)
row = mycursor.fetchone()
print(type(row[0]))
# from tkinter import *
# from tkinter import messagebox
# from PIL import ImageTk


# root3=  Tk()
# root3.geometry('790x512')
# root3.resizable(0,0)
# root3.title('signup Page')

# def on_enter2(event):
#     if User.get() == 'enter otp':
#         User.delete(0,END)

# bgImage = ImageTk.PhotoImage(file="bg.jpg")

# bgLabel = Label(root3,image=bgImage)
# bgLabel.place(x=0,y=0)


# heading = Label(root3,text="verify your account here",font=('Courier New',15,'bold'),bg ='white',fg ="firebrick1")
# heading.place(x=454,y=50)


# heading = Label(root3,text="enter the otp send to your mobile no",font=('Courier New',10,'bold'),bg ='white',fg ="blue2")
# heading.place(x=454,y=150)

# User = Entry(root3, width = 25,font=('Courier New',10),bd =2,fg ="firebrick1")
# User.place(x=500,y=190)
# User.insert(0,'enter otp')
# User.bind('<FocusIn>',on_enter2)
# # print(User.get())
# # Frame(root3,width=200,height=1,bg = "firebrick1").place(x=500,y=210)


# verify = Button(root3,text = "verify",font=('Courier New',12),bg = 'red',fg = 'white',activebackground='white',cursor='hand2')
# verify.place(x = 560,y =220)



# resend = Button(root3,text = "resend otp",font=('Courier New',10),bg ='white',fg = 'blue2',bd = 0,activebackground='white',cursor='hand2')
# resend.place(x = 555,y =250)




# root3.mainloop()
