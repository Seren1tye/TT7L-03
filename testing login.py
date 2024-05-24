import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import itertools
import sys

class AnimatedGIF(tk.Label):
    def __init__(self, master, path, delay=100):
        self._master = master
        self._delay = delay

        im = Image.open(path)
        self._frames = []
        try:
            for i in itertools.count(1):
                self._frames.append(ImageTk.PhotoImage(im.copy().convert('RGBA')))
                im.seek(i)
        except EOFError:
            pass

        self._frame_index = 0
        self._num_frames = len(self._frames)

        super().__init__(master, image=self._frames[0])
        self._animate()

    def _animate(self):
        self._frame_index = (self._frame_index + 1) % self._num_frames
        self.config(image=self._frames[self._frame_index])
        self._master.after(self._delay, self._animate)
 
       
root = tk.Tk()
root.state('zoomed')
root.geometry('935x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)
gif_label = AnimatedGIF(root, "Undefined - Imgur.gif", 100)
gif_label.pack(expand=True, fill='both')

def signin():
    username=user.get()
    password=password.get()
    
    if username=='admin' and password=='1234' :
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')
        
        Label(screen,text='Hello Everyone!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)
        
        screen.mainloop()
        
    elif username!= 'admin' and password!= '1234':
        messagebox.showerror("Invalid" , "Invalid username and password" )

    elif password!='1234':
        messagebox.showerror("Invalid","Invalid password")
    
    elif username!='admin':
        messagebox.showerror("Invalid","Invalid username")
    
frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480, y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YahHei UI Light',23,'bold'))
heading.place(x=130, y=5)

#############################################################################################################

def on_enter(e):
    user.delete(0,'end')
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')

user = Entry(frame,width=25, fg='black',border=0, bg='white',highlightthickness=0, font=('Microsoft YahHei UI Light',11))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#############################################################################################################

def on_enter(e):
    password.delete(0,'end')
    
def on_leave(e):
    pw=password.get()
    if pw=='':
        password.insert(0, 'Password')

password = Entry(frame,width=25, fg='black',border=0, bg='white', highlightthickness=0,font=('Microsoft YahHei UI Light',11))
password.place(x=30, y=150)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##############################################################################################################

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0, command=signin).place(x=35,y=204)

Label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
Label.place(x=75,y=270)

signup= Button(frame,width=6,text='Sign up',border= 0,bg='white',cursor='hand2',fg='#57a1f8')
signup.place(x=215,y=270)


root.mainloop()

