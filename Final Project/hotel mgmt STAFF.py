from tkinter import *
from tkinter import ttk
from customtkinter import *
import datetime
from PIL import ImageTk,Image
import os
from tkinter import messagebox
import mysql.connector as msconn #pip install mysql-connector-python

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'hotel') 


root = CTk()
root.geometry('1080x500')
root.minsize(width=1080,height=550)
root.maxsize(width=1080,height=550)
root.title("Hotel Management")
 


sqlcon.close()
mainloop()