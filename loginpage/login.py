from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
root = Tk()
root.geometry('790x512')
root.resizable(0,0)
root.title('Login Page')

def signup_page():
    root.destroy()
    import signup


def login_user():
    if User.get() =='' or Pass.get() == '':
        messagebox.showerror('Error','all fields are required')
    else:
        try:
            con=  mysql.connector.connect(host = 'localhost',user = 'root',passwd ='Giri12345@')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','database connection is not available')
            return
        
        qurey = 'use login'
        mycursor.execute(qurey)
        
        query = 'SELECT* FROM user_details WHERE user_id = %s and password = %s'
        val = (User.get(),Pass.get())
        mycursor.execute(query,val)
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error','wrong username or password')
        else:
            messagebox.showinfo('login','login successful')

def on_enter(event):
    if User.get() == 'enter username':
        User.delete(0,END)
def on_enter1(event):
    if Pass.get() == 'enter password':
        Pass.delete(0,END)
        
        
        
def hide():
    openeye.config(file = 'closeye.png')
    Pass.config(show = '*')
    eye.config(command= show)

def show():
    openeye.config(file = 'openeye.png')
    Pass.config(show = '')
    eye.config(command = hide)

bgImage = ImageTk.PhotoImage(file="bg.jpg")

bgLabel = Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

heading = Label(root,text="Hii User",font=('Courier New',16,'bold'),bg ='white',fg ="firebrick1")
heading.place(x=550,y=50)




heading2 = Label(root,text="USERNAME",font=('Courier New',10,'bold'),bg ='white',fg ="blue2")
heading2.place(x=500,y=100)
User = Entry(root, width = 25,font=('Courier New',10),bd =0,fg ="firebrick1")
User.place(x=500,y=130)
User.insert(0,'enter username')
User.bind('<FocusIn>',on_enter)
Frame(root,width=200,height=1,bg = "firebrick1").place(x=500,y=150)



heading3 = Label(root,text="PASSWORD",font=('Courier New',10,'bold'),bg ='white',fg ="blue2")
heading3.place(x=500,y=170)
Pass = Entry(root, width = 25,font=('Courier New',10),bd =0,fg ="firebrick1")
Pass.place(x=500,y=200)
Pass.insert(0,'enter password')
Pass.bind('<FocusIn>',on_enter1)
Frame(root,width=200,height=1,bg = "firebrick1").place(x=500,y=220)


openeye = PhotoImage(file='openeye.png')
closeeye = PhotoImage(file='closeye.png')
eye = Button(root,image=openeye,bd = 0,bg = 'white',activebackground='white',cursor='hand2',command=hide)
eye.place(x=680,y = 194)


forgetpass = Button(root,text = "forgot password?",bd = 0,bg = 'white',fg = 'blue2',activebackground='white',cursor='hand2')
forgetpass.place(x = 610,y =226)



Login = Button(root,text = "login",font=('Courier New',12),bg = 'red',fg = 'white',activebackground='white',cursor='hand2',command= login_user)
Login.place(x = 566,y =270)

heading4 = Label(root,text="Or login usig------------",font=('Courier New',10,'bold'),bg ='white',fg ="red")
heading4.place(x=500,y=310)



gpng = PhotoImage(file="google.png")
google= Button(root,image=gpng,bd = 0,bg = 'white',activebackground='white',cursor='hand2')
google.place(x = 550,y =340)

fpng =PhotoImage(file="facebook.png")
facebook= Button(root,image=fpng,bd = 0,bg = 'white',activebackground='white',cursor='hand2')
facebook.place(x = 590,y =340)

tpng =PhotoImage(file="twitter.png")
twitter= Button(root,image=tpng,bd = 0,bg = 'white',activebackground='white',cursor='hand2')
twitter.place(x = 630,y =340)



heading5 = Label(root,text="Don't have an account!!--",font=('Courier New',10,'bold'),bg ='white',fg ="red")
heading5.place(x=500,y=380)

click = Button(root,text = "sign up now",bd = 0,bg = 'white',fg = 'blue2',activebackground='white',cursor='hand2',command = signup_page)
click.place(x = 570,y =400)

heading6 = Label(root,text="need help??",font=('Courier New',10,'bold'),bg ='white',fg ="red")
heading6.place(x=500,y=430)

click = Button(root,text = "girianiruddha4@gmail.com",bd = 0,bg = 'white',fg = 'blue2',activebackground='white',cursor='hand2')
click.place(x = 600,y =450)



root.mainloop()