from CTkTable import CTkTable
from customtkinter import CTkButton,CTk,CTkImage,CTkEntry,CENTER,CTkLabel,CTkFrame,StringVar,CTkCheckBox,DISABLED,CTkTabview,CTkScrollableFrame,CTkComboBox,set_default_color_theme,set_appearance_mode
from PIL import Image
import mysql.connector as msconn

def main():
    main = CTk()
    main.title("Mavrik Hotel Booking")
    main.minsize(height=520,width=1040)
    main.attributes('-topmost', 1)
    main.overrideredirect(True)

    main_pic = CTkImage(Image.open('images/logo.png'),size = (520,520))
    main_label = CTkLabel(main,text = '', image = main_pic)
    main_label._image = main_pic
    main_label.place(x=0,y=0)

    details = CTkFrame(main,height=520,width=520)
    details.place(x=520)
    CTkLabel(details,text='Mavrik Hotel', font=('Berlin Sans FB',50)).place(relx=0.5, rely=0.35, anchor=CENTER)
    CTkLabel(details,text='Management Sytem', font=('Berlin Sans FB',50)).place(relx=0.5, rely=0.45, anchor=CENTER)
    CTkLabel(details,text='Made By:', font=('Dubai',25)).place(relx=0.5, rely=0.55, anchor=CENTER)
    CTkLabel(details,text='Samyog 12A', font=('Dubai',25)).place(relx=0.5, rely=0.65, anchor=CENTER)

    main.after(3000,lambda:call_mainapp(main))
    main.resizable(False,False)
    main.mainloop()

def signup():
    sign = CTk()
    sign.title("Mavrik Hotel Booking")
    sign.minsize(height=720,width=1440)

    cur = sqlcon.cursor()

    cur.execute('select cust_email from credentials')
    edata = cur.fetchall()
    emails = []
    for i in edata:
        emails.append(i[0])

    def save_signin():
        misc = CTkLabel(signup,text='',text_color='red',width=500)
        misc.place(relx = 0.5,y = 444,anchor = CENTER)

        at = dot = up = no = spl = False
        
        email = entry_email.get()
        if email == '':
            misc.configure(text='Enter Email.!',width = 500)
        elif email in emails:
            misc.configure(text='Email already registered',width = 500)
        else:
            if '@' in email:
                at = True
            if '.' in email:
                dot = True
            if at is False or dot is False:
                misc.configure(text='Enter Correct Email Id.',width = 500)

        passw = entry_passw.get()
        if passw == '':
            misc.configure(text='Enter Password.!',width = 500)
        else:
            schar = '!@#$%^&*()_+|-=\\\'./'
            for i in passw:
                if i.isupper():
                    up = True
                    break
            for i in passw:
                if i.isdigit():
                    no = True
                    break
            for i in passw:
                if i in schar:
                    spl = True
                    break
            if spl == False:
                misc.configure(text='Your Password must have atleast one Special character.',width = 500)
            if no == False:
                misc.configure(text='Your Password must have atleast one Number.',width = 500)
            if up == False:
                misc.configure(text='Your Password must have atleast one Upper case character.',width = 500)
            if len(passw)<=8:
                misc.configure(text='The Password must have atleast 8 Characters.',width = 500)

        name = entry_name.get()
        if name == '':
            misc.configure(text='Enter Name.!',width = 500)
        
        if misc._text == '':
            cur.execute('insert into credentials(cust_name,cust_email,cust_pass) values("%s","%s","%s")'%(name,email,passw))
            sqlcon.commit()
            cur.execute('select cust_id from credentials where cust_email = "%s"'%(email))
            custid = cur.fetchall()[0]
            cur.close()
            loggedin[0] = True
            login_details.insert(0,email)
            login_details.insert(0,name)
            login_details.insert(0,custid)
            call_mainapp(sign)

    def save_login():
        lmisc = CTkLabel(login,text='',text_color='red',width=500)
        lmisc.place(relx = 0.5,y = 444,anchor = CENTER)

        password = ''
        email = enter_email.get()
        if email == '':
            lmisc.configure(text='Enter Email.!',width = 500)
        else:
            cur.execute('select cust_pass from credentials where cust_email = "%s"'%(email,))
            password = cur.fetchall()
            if password == []:
                lmisc.configure(text='Incorrect Email or Password',width = 500)

        passw = enter_passw.get()
        if passw == '':
            lmisc.configure(text='Enter Password.!',width = 500)
        else:
            if passw == password[0][0]:
                cur.execute('select * from credentials where cust_email = "%s"'%(email))
                data = cur.fetchall()[0]
                cur.close()
                loggedin[0] = True
                login_details.insert(0,email)
                login_details.insert(0,data[1])
                login_details.insert(0,data[0])
                call_mainapp(sign)  
            else:
                lmisc.configure(text='Incorrect Email or Password',width = 500)

    main_pic = CTkImage(Image.open('images/logo.png'),size = (200,200))
    bottompic1 = CTkImage(Image.open('images/loginbg.png'),size = (1440,720))

    frame = CTkFrame(sign,height=720,width=1440)
    frame.place(relx = 0.5,rely = 0.5, anchor=CENTER)
    
    bpic1 = CTkLabel(frame,text = '', image = bottompic1)
    bpic1._image = bottompic1
    bpic1.place(relx=0.5,rely=0.5,anchor = CENTER)
    
    #signup page
    signup = CTkFrame(frame,height=620,width=540,corner_radius=20)
    signup.place(relx = 0.5,rely = 0.5, anchor=CENTER)
    login_pic = CTkLabel(signup,text = '', image = main_pic)
    login_pic._image = main_pic
    login_pic.place(relx=0.5,rely=0.21,anchor = CENTER)
    

    entry_name = CTkEntry(signup,placeholder_text = 'Name',height=45,width=300)
    entry_name.place(relx = 0.5,y = 290, anchor=CENTER)
    entry_email = CTkEntry(signup,placeholder_text = 'Email',height=45,width=300)
    entry_email.place(relx = 0.5,y = 349,anchor = CENTER)
    entry_passw = CTkEntry(signup,placeholder_text = 'Password',height=45,width=300)
    entry_passw.place(relx = 0.5,y = 409,anchor = CENTER)
    CTkLabel(signup,text='Already have an account?',).place(relx = 0.37,y = 470,anchor = CENTER)
    login_ = CTkLabel(signup,text='Log In', text_color='#44f1a6')
    login_.place(relx = 0.73,y = 470,anchor = CENTER)
    login_.bind("<Button-1>", lambda x:login.tkraise())
    button_signup = CTkButton(signup,text = 'Sign Up',width=300,height=45,command = lambda: save_signin())
    button_signup.place(relx=0.5,y=518,anchor = CENTER)

    #login page
    login = CTkFrame(frame,height=620,width=540,corner_radius=20)
    login.place(relx = 0.5,rely = 0.5, anchor=CENTER)

    signin_pic = CTkLabel(login,text = '', image = main_pic)
    signin_pic._image = main_pic
    signin_pic.place(relx=0.5,rely=0.21,anchor = CENTER)
    
    enter_email = CTkEntry(login,placeholder_text = 'Email',height=45,width=300)
    enter_email.place(relx = 0.5,y = 332,anchor = CENTER)
    enter_passw = CTkEntry(login,placeholder_text = 'Password',height=45,width=300)
    enter_passw.place(relx = 0.5,y = 409,anchor = CENTER)
    CTkLabel(login,text='Don\'t have an account?',).place(relx = 0.35,y = 470,anchor = CENTER)
    signup_ = CTkLabel(login,text='Sign Up', text_color='#44f1a6')
    signup_.place(relx = 0.728,y = 470,anchor = CENTER)
    signup_.bind("<Button-1>", lambda x:signup.tkraise())
    button_login = CTkButton(login,text = 'Log In',width=300,height=45,command=lambda: save_login())
    button_login.place(relx=0.5,y=518,anchor = CENTER)

    sign.mainloop()

def logout(root):
    root.destroy()
    loggedin[0] = False
    login_details.clear()
    mainapp()
    
def call_signup(main):
	main.destroy()
	signup()

def mainapp():
    root = CTk()
    root.title("Mavrik Hotel Booking")
    root.minsize(height=720,width=1440)
    
    cur = sqlcon.cursor()

    frame = CTkFrame(root,height=720,width=1440,corner_radius=15)
    frame.place(relx = 0.5,rely = 0.5, anchor=CENTER)

    banner_pic = CTkImage(Image.open('images/banner2.png'),size = (1440,120))
    topbanner = CTkLabel(frame,text = '', image = banner_pic)
    topbanner._image = banner_pic
    topbanner.place(relx=0.5,rely=0.086,anchor = CENTER)

    profile_pic = CTkImage(Image.open('images/profile.png'),size = (58,58))

    button_login = CTkButton(frame,width=70,height=70,text='',command=lambda:call_signup(root))
    button_login.place(relx=0.97,rely=0.065,anchor=CENTER)
    if loggedin[0] is True:
        button_login.configure(text='',image=profile_pic,command=lambda:logout(root))
    else:
        button_login.configure(text='Log In',image=None)
    
    #tabs
    tabview = CTkTabview(frame,width=1440,height=630)
    tabview.place(relx=0.5,rely=0.56,anchor=CENTER)

    #about tab
    about = tabview.add("About")
    
    pic = CTkFrame(about,height=630,width=1440,corner_radius=15)
    pic.place(relx = 0.5,rely = 0.5, anchor=CENTER)

    image_files = ['images/image0.jpg','images/image1.jpg', 'images/image2.jpg', 'images/image3.jpg','images/image4.jpg','images/image5.jpg']
    images = []

    def load_images():
        for file in image_files:
            image = CTkImage(Image.open(file),size=(1440,630))
            images.append(image)
        canvas.configure(image=images[0])

    canvas = CTkLabel(pic, text = '', width=1440, height=630)
    canvas.pack()

    def next_image(index):
        canvas.configure(image=images[index])
        index += 1
        if index >= len(images):
            index = 0
        root.after(5000, next_image, index)

    load_images()
    next_image(0)

    #rooms tab
    room = tabview.add("Our Rooms")
    
    cur.execute('select * from rooms')
    room_data = cur.fetchall()

    filters = CTkFrame(room,height=100,width=1420)
    filters.pack()

    fil = ['All','no','no','no','no']

    def filter_all():
        cur2 = sqlcon.cursor()
        if fil[0] == 'All':
            cur2.execute('select * from rooms where  availability = "%s" and wifi = "%s" and tv = "%s" and ac = "%s"'%(fil[1],fil[2],fil[3],fil[4]))
            fil_data = cur2.fetchall()
        else:
            cur2.execute('select * from rooms where type = "%s" and availability = "%s" and wifi = "%s" and tv = "%s" and ac = "%s"'%(fil[0],fil[1],fil[2],fil[3],fil[4]))
            fil_data = cur2.fetchall()
        table.configure(row=len(fil_data), column=7, values=fil_data)
        cur2.close()

    def filter_clear():
        table.configure(row=64, column=7, values=room_data)

    def tableclick(cell):
        column = cell['column']
        if column == 7:
            row = cell['row']
            roomno.insert(0,table.get()[row][0])
            tabview.set("Book a Room")
            
    def combobox_callback(choice):
        fil[0] = choice
    combobox = CTkComboBox(filters,values=['All', 'Single','Double','Triple','Quad'],
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

    #contacs tab
    contact = tabview.add("Contact")

    fr_mgr = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_mgr.place(relx = 0.25,rely = 0.25, anchor=CENTER)

    mgr_pic = CTkImage(Image.open('images/mgr.jpg'),size = (275,275))
    mgr = CTkLabel(fr_mgr,text = '', image = mgr_pic)
    mgr._image = mgr_pic
    mgr.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_mgr,text="Manager",font=('Berlin Sans FB',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_mgr,text="Mr. Gru",font=('Berlin Sans FB',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_mgr,text="Extention : 117",font=('Berlin Sans FB',27)).place(x=290,y=150)
    CTkLabel(fr_mgr,text="Mail : manager@mavrik.com",font=('Berlin Sans FB',27)).place(x=290,y=185)


    fr_rec = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_rec.place(relx = 0.75,rely = 0.25, anchor=CENTER)

    rec_pic = CTkImage(Image.open('images/rec.jpg'),size = (275,275))
    rec = CTkLabel(fr_rec,text = '', image = rec_pic)
    rec._image = rec_pic
    rec.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_rec,text="Customer Service",font=('Berlin Sans FB',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_rec,text="Mr. Sam",font=('Berlin Sans FB',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_rec,text="Extention : 225",font=('Berlin Sans FB',27)).place(x=290,y=150)
    CTkLabel(fr_rec,text="Mail : customerservice@mavrik.com",font=('Berlin Sans FB',27)).place(x=290,y=185)
    

    fr_serv = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_serv.place(relx = 0.25,rely = 0.75, anchor=CENTER)

    serv_pic = CTkImage(Image.open('images/serv.jpg'),size = (275,275))
    serv = CTkLabel(fr_serv,text = '', image = serv_pic)
    serv._image = serv_pic
    serv.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_serv,text="Room Service",font=('Berlin Sans FB',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_serv,text="Ms. Anya",font=('Berlin Sans FB',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_serv,text="Extention : 147",font=('Berlin Sans FB',27)).place(x=290,y=150)
    CTkLabel(fr_serv,text="Mail : roomservice@mavrik.com",font=('Berlin Sans FB',27)).place(x=290,y=185)


    fr_cook = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_cook.place(relx = 0.75,rely = 0.75, anchor=CENTER)

    cook_pic = CTkImage(Image.open('images/cook.jpg'),size = (275,275))
    cook = CTkLabel(fr_cook,text = '', image = cook_pic)
    cook._image = cook_pic
    cook.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_cook,text="Restaurant",font=('Berlin Sans FB',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_cook,text="Mr. Kim",font=('Berlin Sans FB',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_cook,text="Extention : 125",font=('Berlin Sans FB',27)).place(x=290,y=150)
    CTkLabel(fr_cook,text="Mail : dining@mavrik.com",font=('Berlin Sans FB',27)).place(x=290,y=185)

    #pricing tab
    pricing = tabview.add("Pricings")

    fr_single = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_single.place(relx = 0.25,rely = 0.25, anchor=CENTER)

    single_pic = CTkImage(Image.open('images/single.jpg'),size = (275,275))
    single = CTkLabel(fr_single,text = '', image = single_pic)
    single._image = single_pic
    single.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_single,text="Single Room",font=('Berlin Sans FB',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_single,text="Mr. Gru",font=('Berlin Sans FB',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_single,text="Extention : 117",font=('Berlin Sans FB',27)).place(x=290,y=150)
    CTkLabel(fr_single,text="Mail : manager@mavrik.com",font=('Berlin Sans FB',27)).place(x=290,y=185)


    fr_double = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_double.place(relx = 0.75,rely = 0.25, anchor=CENTER)

    double_pic = CTkImage(Image.open('images/double.jpg'),size = (275,275))
    double = CTkLabel(fr_double,text = '', image = double_pic)
    double._image = double_pic
    double.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_double,text="Customer Service",font=('Berlin Sans FB',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_double,text="Mr. Sam",font=('Berlin Sans FB',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_double,text="Extention : 225",font=('Berlin Sans FB',27)).place(x=290,y=150)
    CTkLabel(fr_double,text="Mail : customerservice@mavrik.com",font=('Berlin Sans FB',27)).place(x=290,y=185)
    

    fr_triple = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_triple.place(relx = 0.25,rely = 0.75, anchor=CENTER)

    triple_pic = CTkImage(Image.open('images/triple.jpg'),size = (275,275))
    triple = CTkLabel(fr_triple,text = '', image = triple_pic)
    triple._image = triple_pic
    triple.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_triple,text="Room Service",font=('Berlin Sans FB',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_triple,text="Ms. Anya",font=('Berlin Sans FB',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_triple,text="Extention : 147",font=('Berlin Sans FB',27)).place(x=290,y=150)
    CTkLabel(fr_triple,text="Mail : roomservice@mavrik.com",font=('Berlin Sans FB',27)).place(x=290,y=185)


    fr_quad = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_quad.place(relx = 0.75,rely = 0.75, anchor=CENTER)

    quad_pic = CTkImage(Image.open('images/quad.jpg'),size = (275,275))
    quad = CTkLabel(fr_quad,text = '', image = quad_pic)
    quad._image = quad_pic
    quad.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_quad,text="Restaurant",font=('Berlin Sans FB',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_quad,text="Mr. Kim",font=('Berlin Sans FB',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_quad,text="Extention : 125",font=('Berlin Sans FB',27)).place(x=290,y=150)
    CTkLabel(fr_quad,text="Mail : dining@mavrik.com",font=('Berlin Sans FB',27)).place(x=290,y=185)

    #booking tab
    book = tabview.add("Book a Room")
    books = CTkFrame(book,height=600,width=1440,corner_radius=15)
    books.place(relx = 0.5,rely = 0.58, anchor=CENTER)
    
    CTkLabel(books,text='book').place(relx = 0.5,rely = 0.5, anchor=CENTER)







    tabview.set("Book a Room")
    cur.close()
    root.mainloop()

def call_mainapp(sign):
	sign.destroy()
	mainapp()
    
if __name__ == '__main__':
    set_appearance_mode('system')
    set_default_color_theme('green')

    loggedin = [False]
    login_details = []
    roomno = []
    
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'hotel')
    #main()
    mainapp()
    sqlcon.close()