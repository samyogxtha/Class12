import tkinter as tk
from tkinter import *
from customtkinter import *
from PIL import ImageTk,Image
import mysql.connector as msconn
import time

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'hotel')

cur = sqlcon.cursor()
cur.execute('select * from rooms')
room_data = cur.fetchall()


import customtkinter
from CTkTable import *

root = customtkinter.CTk()
root.minsize(height=720,width=1440)


room = CTkFrame(root,height=600,width=1400)
room.place(relx = 0.5,rely = 0.5, anchor=CENTER)


filters = CTkFrame(room,height=100,width=1420)
filters.pack()

fil = ['single','yes','yes','yes','yes']

def filter_all():
    cur.execute('select * from rooms where type = "%s" and availability = "%s" and wifi = "%s" and tv = "%s" and ac = "%s"'%(fil[0],fil[1],fil[2],fil[3],fil[4]))
    fil_data = cur.fetchall()
    table.configure(row=len(fil_data), column=7, values=fil_data)

def filter_clear():
    table.configure(row=64, column=7, values=room_data)

def tableclick(cell):
    column = cell['column']
    if column == 7:
        row = cell['row']
        roomno = table.get()[row][0]
        




def combobox_callback(choice):
    fil[0] = choice
combobox = customtkinter.CTkComboBox(filters,values=['All', 'Single','Double','Triple','Quad'],
                                     command=combobox_callback)
combobox.place(relx = 0.08,rely = 0.25, anchor=CENTER)
combobox.set('All')

check_var_avai = StringVar()
def checkbox_avai_event():
    fil[1] = check_var_avai.get()
checkbox_avai = CTkCheckBox(filters, text='Availability', command=checkbox_avai_event,
                                     variable=check_var_avai, onvalue='yes', offvalue='no')
checkbox_avai.place(relx = 0.22,rely = 0.25, anchor=CENTER)

check_var_wifi = StringVar()
def checkbox_wifi_event():
    fil[2] = check_var_wifi.get()
checkbox_wifi = CTkCheckBox(filters, text='WiFi', command=checkbox_wifi_event,
                                     variable=check_var_wifi, onvalue='yes', offvalue='no')
checkbox_wifi.place(relx = 0.36,rely = 0.25, anchor=CENTER)

check_var_tv = StringVar()
def checkbox_tv_event():
    fil[3] = check_var_tv.get()
checkbox_tv = CTkCheckBox(filters, text='TV', command=checkbox_tv_event,
                                     variable=check_var_tv, onvalue='yes', offvalue='no')
checkbox_tv.place(relx = 0.5,rely = 0.25, anchor=CENTER)

check_var_ac = StringVar()
def checkbox_event_ac():
    fil[4] = check_var_ac.get()
checkbox_ac = CTkCheckBox(filters, text='AC', command=checkbox_event_ac,
                                     variable=check_var_ac, onvalue='yes', offvalue='no')
checkbox_ac.place(relx = 0.635,rely = 0.25, anchor=CENTER)

button_filter = CTkButton(filters,text='Filter',command=lambda:filter_all())
button_filter.place(relx = 0.775,rely = 0.25, anchor=CENTER)

button_clear = CTkButton(filters,text='Clear Filters',command=lambda:filter_clear())
button_clear.place(relx = 0.915,rely = 0.25, anchor=CENTER)

button0 = CTkButton(filters,text='Sl.No.',state=DISABLED,width=250,corner_radius=0,text_color_disabled='white')
button0.place(relx = 0.08,rely = 0.75, anchor=CENTER)
button1 = CTkButton(filters,text='Availability',state=DISABLED,width=250,corner_radius=0,text_color_disabled='white')
button1.place(relx = 0.2,rely = 0.75, anchor=CENTER)
button2 = CTkButton(filters,text='Type',state=DISABLED,width=250,corner_radius=0,text_color_disabled='white')
button2.place(relx = 0.31,rely = 0.75, anchor=CENTER)
button3 = CTkButton(filters,text='WiFi',state=DISABLED,width=250,corner_radius=0,text_color_disabled='white')
button3.place(relx = 0.435,rely = 0.75, anchor=CENTER)
button4 = CTkButton(filters,text='TV',state=DISABLED,width=250,corner_radius=0,text_color_disabled='white')
button4.place(relx = 0.555,rely = 0.75, anchor=CENTER)
button5 = CTkButton(filters,text='AC',state=DISABLED,width=250,corner_radius=0,text_color_disabled='white')
button5.place(relx = 0.675,rely = 0.75, anchor=CENTER)
button6 = CTkButton(filters,text='Price',state=DISABLED,width=250,corner_radius=0,text_color_disabled='white')
button6.place(relx = 0.79,rely = 0.75, anchor=CENTER)
button7 = CTkButton(filters,text='Book',state=DISABLED,width=250,corner_radius=0,text_color_disabled='white')
button7.place(relx = 0.915,rely = 0.75, anchor=CENTER)

room_scrollframe = CTkScrollableFrame(room, width=1400, height=470)
room_scrollframe.pack()

table = CTkTable(room_scrollframe, row=64, column=8, hover_color= '#575757', values=room_data,command=tableclick)
table.pack(expand=False, fill='both', padx=20)


root.mainloop()


cur.close()
sqlcon.close()