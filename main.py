import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import openpyxl 
import pandas as pd
import pygame

root = tk.Tk()
bg=ImageTk.PhotoImage(file='timetravel.png')
bg_image=Label(root,image=bg).place(x=0,y=0, relwidth=1,relheight=1)
root.state('zoomed')
root.geometry('935x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



root.mainloop()