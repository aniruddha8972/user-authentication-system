from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
# import otp

def verify_page():
    root2.destroy()
    import verification


# def clear():
#     email.delete(0,END)
#     User.delete(0,END)
#     Pass1.delete(0,END)
#     Pass2.delete(0,END)

# def save_mail():
#     addr = email.get()
#     return addr


def connectdatabase():
    if email.get() =='' or User.get() == '' or Pass1.get() == '' or Pass2.get() == '':
        messagebox.showerror('Error','all fields are required')
    elif Pass1.get() != Pass2.get():
        messagebox.showerror('Error','paswords are unmatched')
    elif chv.get() == 0:
        messagebox.showerror('Error','please accept all the terms & conditions')
    else:
        try:
            con =  mysql.connector.connect(host = 'localhost',user = 'root',passwd ='Giri12345@')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','database connection is not available')
            return
        
        
        
        qurey = 'use login'
        mycursor.execute(qurey)
        
        
        
        query = 'SELECT* FROM user_details WHERE user_id = %s'
        val = (User.get(),)
        mycursor.execute(query,val)
        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','ueername already exists')
        else:
            query = 'INSERT INTO USER_DETAILS(EMAIL,USER_ID,PASSWORD) VALUES(%s,%s,%s)'
            val1= (email.get(),User.get(),Pass1.get())
            mycursor.execute(query, val1)
            con.commit()
            verify_page()
            con.close()
            messagebox.showinfo('success','account created successfully')
            # clear()
        
root2=  Tk()
root2.geometry('790x512')
root2.resizable(0,0)
root2.title('signup Page')


def on_enter(event):
    if email.get() == 'email':
        email.delete(0,END)


def on_enter2(event):
    if User.get() == 'user id':
        User.delete(0,END)


def on_enter3(event):
    if Pass1.get() == 'password':
        Pass1.delete(0,END)


def on_enter4(event):
    if Pass2.get() == 'password':
        Pass2.delete(0,END)
        
        
def login_window():
    root2.destroy()
    import login
    
        


bgImage = ImageTk.PhotoImage(file="bg.jpg")

bgLabel = Label(root2,image=bgImage)
bgLabel.place(x=0,y=0)

heading = Label(root2,text="Hey first time here!!",font=('Courier New',16,'bold'),bg ='white',fg ="firebrick1")
heading.place(x=465,y=50)

heading2 = Label(root2,text="Enter email adress",font=('Courier New',10,'bold'),bg ='white',fg ="blue2")
heading2.place(x=500,y=100)

email = Entry(root2, width = 25,font=('Courier New',10),bd =0,fg ="firebrick1")
email.place(x=500,y=130)
email.insert(0,'email')
email.bind('<FocusIn>',on_enter)
Frame(root2,width=200,height=1,bg = "firebrick1").place(x=500,y=150)


heading3 = Label(root2,text="Enter username",font=('Courier New',10,'bold'),bg ='white',fg ="blue2")
heading3.place(x=500,y=160)

User = Entry(root2, width = 25,font=('Courier New',10),bd =0,fg ="firebrick1")
User.place(x=500,y=190)
User.insert(0,'user id')
User.bind('<FocusIn>',on_enter2)
Frame(root2,width=200,height=1,bg = "firebrick1").place(x=500,y=210)


heading4 = Label(root2,text="Enter password",font=('Courier New',10,'bold'),bg ='white',fg ="blue2")
heading4.place(x=500,y=220)

Pass1 = Entry(root2, width = 25,font=('Courier New',10),bd =0,fg ="firebrick1")
Pass1.place(x=500,y=250)
Pass1.insert(0,'password')
Pass1.bind('<FocusIn>',on_enter3)
Frame(root2,width=200,height=1,bg = "firebrick1").place(x=500,y=270)


heading5 = Label(root2,text="Confirm password",font=('Courier New',10,'bold'),bg ='white',fg ="blue2")
heading5.place(x=500,y=280)

Pass2 = Entry(root2, width = 25,font=('Courier New',10),bd =0,fg ="firebrick1")
Pass2.place(x=500,y=320)
Pass2.insert(0,'password')
Pass2.bind('<FocusIn>',on_enter4)
Frame(root2,width=200,height=1,bg = "firebrick1").place(x=500,y=340)

# if Pass1 != Pass2:
#     heading6 = Label(root2,text="password unmatched",font=('Courier New',10,'bold'),bg ='white',fg ="red")
#     heading5.place(x=500,y=290)
chv = IntVar()
check = Checkbutton(root2,text = "i agreed all the terms & conditions",bd = 0,bg = 'white',fg = 'blue2',activebackground='white',cursor='hand2',variable=chv)
check.place(x = 500,y =350)



signup = Button(root2,text = "sign up",font=('Courier New',12),bg = 'red',fg = 'white',activebackground='white',cursor='hand2',command = connectdatabase)
signup.place(x = 560,y =380)

heading6 = Label(root2,text="already have an account!!--",font=('Courier New',10,'bold'),bg ='white',fg ="red")
heading6.place(x=500,y=420)

click = Button(root2,text = "Login here",bd = 0,bg = 'white',fg = 'blue2',activebackground='white',cursor='hand2',command= login_window)
click.place(x = 570,y =440)

root2.mainloop()
