from CTkTable import CTkTable
from customtkinter import CTkButton,CTk,CTkProgressBar,CTkImage,CTkEntry,CTkLabel,CTkFrame,StringVar,CTkCheckBox,CTkTabview,CTkScrollableFrame,CTkComboBox,CENTER,DISABLED,set_default_color_theme,set_appearance_mode
from PIL import Image
from datetime import datetime as dt
import mysql.connector as msconn

def main():
    main = CTk()
    main.title("Mavrik Hotel Booking")
    main.minsize(height=520,width=1040)
    main.attributes('-topmost', 1)
    main.overrideredirect(True)

    main_pic = CTkImage(Image.open('assets/logo.png'),size = (520,520))
    main_label = CTkLabel(main,text = '', image = main_pic)
    main_label._image = main_pic
    main_label.place(x=0,y=0)

    details = CTkFrame(main,height=520,width=520)
    details.place(x=520)
    CTkLabel(details,text='Mavrik Hotel', font=('HP Simplified',50)).place(relx=0.5, rely=0.35, anchor=CENTER)
    CTkLabel(details,text='Management Sytem', font=('HP Simplified',50)).place(relx=0.5, rely=0.45, anchor=CENTER)
    CTkLabel(details,text='Made By:', font=('Dubai',25)).place(relx=0.5, rely=0.55, anchor=CENTER)
    CTkLabel(details,text='Samyog 12A', font=('Dubai',25)).place(relx=0.5, rely=0.65, anchor=CENTER)

    main.after(3000,lambda:call_mainapp(main))
    main.resizable(False,False)
    main.mainloop()

def mainapp():
    root = CTk()
    root.title("Mavrik Hotel Booking")
    root.minsize(height=720,width=1440)

    #------------------FUNCTION-FOR-LOGGING-OUT------------------
    def logout():
        def logged_out():
            progressbar.stop()
            CTkLabel(logout_,height=200,text='Logged Out Successfully!',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
            tabview.set("About")
            root.after(2000,lambda:frame_logout.destroy())

        loggedin[0] = False
        login_details.clear()
        button_login.configure(text='Log In',image=None ,command=lambda:loggin())

        frame_logout = CTkFrame(root,height=720,width=1440)
        frame_logout.place(relx = 0.5,rely = 0.5,anchor = CENTER)

        bottompic2 = CTkImage(Image.open('assets/loginbg.png'),size = (1440,720))
        bpic2 = CTkLabel(frame_logout,text = '', image = bottompic2)
        bpic2._image = bottompic2
        bpic2.place(relx=0.5,rely=0.5,anchor = CENTER)

        logout_ = CTkFrame(frame_logout,height=620,width=540,corner_radius=20)
        logout_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        progressbar = CTkProgressBar(logout_,height=50,mode="indeterminate")
        progressbar.place(relx = 0.5,rely = 0.5, anchor=CENTER)
        CTkLabel(logout_,text='Logging Out...',font=('HP Simplified',20,'bold')).place(relx=0.5,rely=0.6,anchor = CENTER)
        progressbar.start()

        root.after(3000,lambda:logged_out())

    #------------------FUNCTION-FOR-LOGGING-AND-SIGNING-IN------------------
    def loggin():
        cur0 = sqlcon.cursor()

        cur0.execute('select email from customers')
        edata = cur0.fetchall()
        emails = []
        for i in edata:
            emails.append(i[0])

        def save_signin():
            def logged_in(progress):
                progress.stop()
                cur0.close()
                sqlcon.commit()
                CTkLabel(signin_,height=620,width=540,corner_radius=20,text='Signed In Successfully!',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
                update_logbutton()
                root.after(2000,lambda:frame_login.destroy())

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
                if len(passw)<8:
                    misc.configure(text='The Password must have atleast 8 Characters.',width = 500)

            name = entry_name.get()
            if name == '':
                misc.configure(text='Enter Name.!',width = 500)
            
            if misc._text == '':
                cur0.execute('insert into customers(name,email,pass) values("%s","%s","%s")'%(name,email,passw))
                sqlcon.commit()
                cur0.execute('select * from customers where email = "%s"'%(email))
                data = cur0.fetchall()[0]
                loggedin[0] = True
                login_details.clear()
                login_details.insert(0,list(data))

                signin_ = CTkFrame(frame_login,height=620,width=540,corner_radius=20)
                signin_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

                progressbar = CTkProgressBar(signin_,height=50,mode="indeterminate")
                progressbar.place(relx = 0.5,rely = 0.5, anchor=CENTER)
                CTkLabel(signin_,text='Signing In...',font=('HP Simplified',20,'bold')).place(relx=0.5,rely=0.6,anchor = CENTER)
                progressbar.start()

                root.after(3000,lambda:logged_in(progressbar))

        def save_login():
            def logged_in(progress):
                progress.stop()
                cur0.close()
                CTkLabel(logoin_,height=200,corner_radius=20,text='Logged In Successfully!',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
                update_logbutton()
                root.after(2000,lambda:frame_login.destroy())

            lmisc = CTkLabel(login,text='',text_color='red',width=500)
            lmisc.place(relx = 0.5,y = 444,anchor = CENTER)

            password = []
            email = enter_email.get()
            if email == '':
                lmisc.configure(text='Enter Email.!',width = 500)
            else:
                cur0.execute('select pass from customers where email = "%s"'%(email,))
                password.insert(0,cur0.fetchall())
                if password[0] == []:
                    lmisc.configure(text='Incorrect Email or Password',width = 500)

            passw = enter_passw.get()
            if passw == '':
                lmisc.configure(text='Enter Password.!',width = 500)
            elif password[0] == []:
                lmisc.configure(text='Incorrect Email or Password',width = 500)
            else:
                if passw == password[0][0][0]:
                    cur0.execute('select * from customers where email = "%s"'%(email))
                    data = cur0.fetchall()[0]
                    loggedin[0] = True
                    login_details.clear()
                    login_details.insert(0,list(data))

                    logoin_ = CTkFrame(frame_login,height=620,width=540,corner_radius=20)
                    logoin_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

                    progressbar = CTkProgressBar(logoin_,height=50,mode="indeterminate")
                    progressbar.place(relx = 0.5,rely = 0.5, anchor=CENTER)
                    CTkLabel(logoin_,text='Logging In...',font=('HP Simplified',20,'bold')).place(relx=0.5,rely=0.6,anchor = CENTER)
                    progressbar.start()

                    root.after(3000,lambda:logged_in(progressbar))
                else:
                    lmisc.configure(text='Incorrect Email or Password',width = 500)

        main_pic = CTkImage(Image.open('assets/logo.png'),size = (200,200))
        bottompic1 = CTkImage(Image.open('assets/loginbg.png'),size = (1440,720))

        frame_login = CTkFrame(root,height=720,width=1440)
        frame_login.place(relx = 0.5,rely = 0.5, anchor=CENTER)
        
        bpic1 = CTkLabel(frame_login,text = '', image = bottompic1)
        bpic1._image = bottompic1
        bpic1.place(relx=0.5,rely=0.5,anchor = CENTER)
        
        #signup page
        signup = CTkFrame(frame_login,height=620,width=540,corner_radius=20)
        signup.place(relx = 0.5,rely = 0.5, anchor=CENTER)
        login_pic = CTkLabel(signup,text = '', image = main_pic)
        login_pic._image = main_pic
        login_pic.place(relx=0.5,rely=0.21,anchor = CENTER)
        
        CTkButton(signup,text='←',height=50,width=50,corner_radius=30,fg_color='transparent', hover_color='#333333', command=lambda:frame_login.destroy()).place(x=1,y=1)
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
        login = CTkFrame(frame_login,height=620,width=540,corner_radius=20)
        login.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        signin_pic = CTkLabel(login,text = '', image = main_pic)
        signin_pic._image = main_pic
        signin_pic.place(relx=0.5,rely=0.21,anchor = CENTER)
        
        CTkButton(login,text='←',height=50,width=50,corner_radius=30,fg_color='transparent', hover_color='#333333', command=lambda:frame_login.destroy()).place(x=1,y=1)
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

    def update_logbutton():
        #profile_pic = CTkImage(Image.open('assets/profile.png'),size = (58,58))
        button_login.configure(text='Log Out',command=lambda:logout())#text='',image=profile_pic
        #button_login._image = profile_pic

    #main app
    cur = sqlcon.cursor()

    frame = CTkFrame(root,height=720,width=1440,corner_radius=15)
    frame.place(relx = 0.5,rely = 0.5, anchor=CENTER)

    #------------------TOP-BANNER------------------
    banner_pic = CTkImage(Image.open('assets/banner2.png'),size = (1440,120))
    topbanner = CTkLabel(frame,text = '', image = banner_pic)
    topbanner._image = banner_pic
    topbanner.place(relx=0.5,rely=0.086,anchor = CENTER)

    button_login = CTkButton(frame,width=70,height=70,text='Log In',command=lambda:loggin())
    button_login.place(relx=0.97,rely=0.065,anchor=CENTER)
    
    #------------------CREATE-TABS------------------
    tabview = CTkTabview(frame,width=1440,height=630)
    tabview.place(relx=0.5,rely=0.56,anchor=CENTER)

    #------------------ABOUT-TAB------------------
    about = tabview.add("About")
    
    pic = CTkFrame(about,height=630,width=1440,corner_radius=15)
    pic.place(relx = 0.5,rely = 0.5, anchor=CENTER)

    image_files = ['assets/image0.jpg','assets/image1.jpg', 'assets/image2.jpg', 'assets/image3.jpg','assets/image4.jpg','assets/image5.jpg']
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

    #------------------CONTACS-TAB------------------
    contact = tabview.add("Contact")

    fr_mgr = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_mgr.place(relx = 0.25,rely = 0.25, anchor=CENTER)

    mgr_pic = CTkImage(Image.open('assets/mgr.jpg'),size = (275,275))
    mgr = CTkLabel(fr_mgr,text = '', image = mgr_pic)
    mgr._image = mgr_pic
    mgr.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_mgr,text="Manager",font=('HP Simplified',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_mgr,text="Mr. Gru",font=('HP Simplified',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_mgr,text="Extention : 117",font=('HP Simplified',27)).place(x=290,y=150)
    CTkLabel(fr_mgr,text="Mail : manager@mavrik.com",font=('HP Simplified',27)).place(x=290,y=185)

    fr_rec = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_rec.place(relx = 0.75,rely = 0.25, anchor=CENTER)

    rec_pic = CTkImage(Image.open('assets/rec.jpg'),size = (275,275))
    rec = CTkLabel(fr_rec,text = '', image = rec_pic)
    rec._image = rec_pic
    rec.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_rec,text="Customer Service",font=('HP Simplified',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_rec,text="Mr. Sam",font=('HP Simplified',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_rec,text="Extention : 225",font=('HP Simplified',27)).place(x=290,y=150)
    CTkLabel(fr_rec,text="Mail : customerservice@mavrik.com",font=('HP Simplified',27)).place(x=290,y=185)
    
    fr_serv = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_serv.place(relx = 0.25,rely = 0.75, anchor=CENTER)

    serv_pic = CTkImage(Image.open('assets/serv.jpg'),size = (275,275))
    serv = CTkLabel(fr_serv,text = '', image = serv_pic)
    serv._image = serv_pic
    serv.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_serv,text="Room Service",font=('HP Simplified',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_serv,text="Ms. Anya",font=('HP Simplified',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_serv,text="Extention : 147",font=('HP Simplified',27)).place(x=290,y=150)
    CTkLabel(fr_serv,text="Mail : roomservice@mavrik.com",font=('HP Simplified',27)).place(x=290,y=185)

    fr_cook = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_cook.place(relx = 0.75,rely = 0.75, anchor=CENTER)

    cook_pic = CTkImage(Image.open('assets/cook.jpg'),size = (275,275))
    cook = CTkLabel(fr_cook,text = '', image = cook_pic)
    cook._image = cook_pic
    cook.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_cook,text="Restaurant",font=('HP Simplified',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_cook,text="Mr. Kim",font=('HP Simplified',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_cook,text="Extention : 125",font=('HP Simplified',27)).place(x=290,y=150)
    CTkLabel(fr_cook,text="Mail : dining@mavrik.com",font=('HP Simplified',27)).place(x=290,y=185)

    #------------------PRICING-TAB------------------
    pricing = tabview.add("Rooms & Pricings")

    def price_book(type):
        cur2 = sqlcon.cursor()
        cur2.execute('select * from rooms where type = "%s"'%(type))
        fil_data = cur2.fetchall()
        table.configure(row=len(fil_data), column=7, values=fil_data)
        cur2.close()
        tabview.set('Book a Room')

    fr_single = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_single.place(relx = 0.25,rely = 0.25, anchor=CENTER)

    single_pic = CTkImage(Image.open('assets/single.jpg'),size = (275,275))
    single = CTkLabel(fr_single,text = '', image = single_pic)
    single._image = single_pic
    single.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_single,text="Single Room",font=('HP Simplified',47,'bold')).place(x=290,y=45)
    CTkLabel(fr_single,text="Basic    $200",font=('HP Simplified',27)).place(x=300,y=100)
    CTkLabel(fr_single,text="WiFi       +$50",font=('HP Simplified',27)).place(x=300,y=130)
    CTkLabel(fr_single,text="TV          +$50",font=('HP Simplified',27)).place(x=300,y=160)
    CTkLabel(fr_single,text="AC          +$50",font=('HP Simplified',27)).place(x=300,y=185)
    CTkButton(fr_single,text='Book',height=50,width=80, command=lambda:price_book('Single')).place(relx=0.92,rely=0.85,anchor=CENTER)

    fr_double = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_double.place(relx = 0.75,rely = 0.25, anchor=CENTER)

    double_pic = CTkImage(Image.open('assets/double.jpg'),size = (275,275))
    double = CTkLabel(fr_double,text = '', image = double_pic)
    double._image = double_pic
    double.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_double,text="Double Room",font=('HP Simplified',47,'bold')).place(x=290,y=45)
    CTkLabel(fr_double,text="Basic    $250",font=('HP Simplified',27)).place(x=300,y=100)
    CTkLabel(fr_double,text="WiFi       +$50",font=('HP Simplified',27)).place(x=300,y=130)
    CTkLabel(fr_double,text="TV          +$50",font=('HP Simplified',27)).place(x=300,y=160)
    CTkLabel(fr_double,text="AC          +$50",font=('HP Simplified',27)).place(x=300,y=185)
    CTkButton(fr_double,text='Book',height=50,width=80, command=lambda:price_book('Double')).place(relx=0.92,rely=0.85,anchor=CENTER)
    
    fr_triple = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_triple.place(relx = 0.25,rely = 0.75, anchor=CENTER)

    triple_pic = CTkImage(Image.open('assets/triple.jpg'),size = (275,275))
    triple = CTkLabel(fr_triple,text = '', image = triple_pic)
    triple._image = triple_pic
    triple.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_triple,text="Triple Room",font=('HP Simplified',47,'bold')).place(x=290,y=45)
    CTkLabel(fr_triple,text="Basic    $300",font=('HP Simplified',27)).place(x=300,y=100)
    CTkLabel(fr_triple,text="WiFi       +$50",font=('HP Simplified',27)).place(x=300,y=130)
    CTkLabel(fr_triple,text="TV          +$50",font=('HP Simplified',27)).place(x=300,y=160)
    CTkLabel(fr_triple,text="AC          +$50",font=('HP Simplified',27)).place(x=300,y=185)
    CTkButton(fr_triple,text='Book',height=50,width=80, command=lambda:price_book('Triple')).place(relx=0.92,rely=0.85,anchor=CENTER)

    fr_quad = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_quad.place(relx = 0.75,rely = 0.75, anchor=CENTER)

    quad_pic = CTkImage(Image.open('assets/quad.jpg'),size = (275,275))
    quad = CTkLabel(fr_quad,text = '', image = quad_pic)
    quad._image = quad_pic
    quad.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_quad,text="Quad Room",font=('HP Simplified',47,'bold')).place(x=290,y=45)
    CTkLabel(fr_quad,text="Basic    $350",font=('HP Simplified',27)).place(x=300,y=100)
    CTkLabel(fr_quad,text="WiFi       +$50",font=('HP Simplified',27)).place(x=300,y=130)
    CTkLabel(fr_quad,text="TV          +$50",font=('HP Simplified',27)).place(x=300,y=160)
    CTkLabel(fr_quad,text="AC          +$50",font=('HP Simplified',27)).place(x=300,y=185)
    CTkButton(fr_quad,text='Book',height=50,width=80, command=lambda:price_book('Quad')).place(relx=0.92,rely=0.85,anchor=CENTER)

    #------------------BOOKING-TAB------------------
    book = tabview.add("Book a Room")
    
    cur.execute('select * from rooms')
    room_data = cur.fetchall()

    #------------------ENTER-CUSTOMER-DETAILS------------------
    def show_details():
        def check_entrys():
            if checkin_date.get() == '' or checkout_date.get() == '':
                miscs.configure(width=500,text='*Please fill all the Information*')
            elif address.get() == '' and login_details[0][2] is None:
                miscs.configure(width=500,text='*Please fill all the Information*')
            elif mobile.get() == '' and login_details[0][3] is None:
                miscs.configure(width=500,text='*Please fill all the Information*')
            else:
                proceed()

        def proceed():
            #------------------PRINT-RECIPT------------------
            def print_recipt():
                def closeall():
                    tabview.set('About')
                    details.destroy()
                    rec.destroy()

                sqlcon.commit()
                cur = sqlcon.cursor()
                cur.execute(f'select * from customers where cust_id = {login_details[0][0]}')
                login_details.clear()
                login_details.append(cur.fetchall()[0])

                #-------------------ADD-RECIPT-PDF------------------
                from PyPDF2 import PdfWriter, PdfReader
                import io
                from reportlab.pdfgen import canvas
                from reportlab.lib.pagesizes import letter

                packet = io.BytesIO()
                can = canvas.Canvas(packet, pagesize=letter)
                can.drawString(70, 700, f'Booking Id: {booking_details[0][0]}' )
                can.drawString(350, 700, f'Customer Id: {login_details[0][0]}' )
                can.drawString(70, 670, f'Customer Name: {login_details[0][1]}') 
                can.drawString(350, 670, f'Checkin Date: {booking_details[0][3]}' )
                can.drawString(70, 640, f'No of days staying: {booking_details[0][5]}')
                can.drawString(350, 640, f'Checkout Date: {booking_details[0][4]}' )
                can.drawString(70, 610, f'Room No: {booking_details[0][2]}')
                can.drawString(350, 610, f'WiFi: {room_details[0][3]}' )
                can.drawString(70, 580, f'Type: {room_details[0][2]}')
                can.drawString(350, 580, f'TV: {room_details[0][4]}' )
                can.drawString(70, 550, f'Price: {room_details[0][6]}$')
                can.drawString(350, 550,  f'AC: {room_details[0][5]}')
                can.drawString(200, 15,  'Please show this at the Reception.')
                can.save()

                packet.seek(0)

                new_pdf = PdfReader(packet)

                existing_pdf = PdfReader(open('assets/rec.pdf', 'rb'))
                output = PdfWriter()

                page = existing_pdf.pages[0]
                page.merge_page(new_pdf.pages[0])
                output.add_page(page)

                output_stream = open(f'{booking_details[0][0]} Recipt.pdf', 'wb')
                output.write(output_stream)
                output_stream.close() 

                CTkLabel(rec_,text='Please show the recipt at the Reception',font=('HP Simplified',25),height=200,corner_radius=30).place(relx=0.5,rely=0.45,anchor = CENTER)
                CTkLabel(rec_,text='Thank You.!',font=('HP Simplified',20,'bold')).place(relx=0.5,rely=0.59,anchor = CENTER)
                CTkButton(rec_,text='Done',height=50,width=100, command=lambda:closeall()).place(relx=0.5,rely=0.75,anchor=CENTER)

            def recload_stop():
                progressbar.stop()
                try:
                    cur = sqlcon.cursor()
                    if login_details[0][2] is None:
                        cur.execute('update customers set address = "%s",mobile = "%s" where cust_id = %s'%(address.get(),mobile.get(),login_details[0][0]))
                    dif = (dt.strptime(checkout_date.get(), "%Y-%m-%d") - dt.strptime(checkin_date.get(), "%Y-%m-%d")).days
                    cur.execute(f'update rooms set availability = "no" where room_no = {room_details[0][0]}')
                    cur.execute('insert into bookings(cust_id,room_no,checkin_date,checkout_date,no_stay,price) values(%s,%s,"%s","%s",%s,%s)'%(login_details[0][0],room_details[0][0],checkin_date.get(),checkout_date.get(),dif,room_details[0][6]))
                    CTkLabel(rec_,height=200,text='Room Booked Successfully!',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
                    cur.execute('select * from bookings order by booking_id desc limit 1')
                    det = cur.fetchall()[0]
                    booking_details.clear()
                    booking_details.append(det)
                    root.after(2000,lambda:print_recipt())
                    cur.close()
                except:
                    CTkLabel(rec_,height=200,text='Booking Failed', width=200,font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
                    miscs.configure(width=500,text='*Please fill Correct the Information*')
                    root.after(2000,lambda:rec.destroy())

            rec = CTkFrame(book,height=590,width=1422,corner_radius=30)
            rec.place(relx = 0.5,rely = 0.5, anchor=CENTER)

            recp = CTkImage(Image.open('assets/loginbg.png'),size = (1440,720))
            recpic = CTkLabel(rec,text = '', image = recp)
            recpic._image = recp
            recpic.place(relx=0.5,rely=0.5,anchor = CENTER)

            rec_ = CTkFrame(rec,height=520,width=540,corner_radius=30)
            rec_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

            progressbar = CTkProgressBar(rec_,height=50,mode="indeterminate")
            progressbar.place(relx = 0.5,rely = 0.5, anchor=CENTER)
            CTkLabel(rec_,text='Booking...',font=('HP Simplified',20,'bold')).place(relx=0.5,rely=0.6,anchor = CENTER)
            progressbar.start()

            root.after(3000,lambda:recload_stop())

        details = CTkFrame(book,height=590,width=1422,corner_radius=30)
        details.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        CTkButton(details,text='←',height=50,width=50,corner_radius=30,fg_color='transparent', hover_color='#333333', command=lambda:details.destroy()).place(x=1,y=1)

        CTkLabel(details,text="Checkin Date (yyyy-mm-dd)*",font=('HP Simplified',17)).place(relx = 0.15,rely = 0.2, anchor=CENTER)
        checkin_date = CTkEntry(details,placeholder_text = 'Checkin Date*',height=45,width=300)
        checkin_date.place(relx = 0.15,rely = 0.3, anchor=CENTER)

        CTkLabel(details,text="Checkout Date (yyyy-mm-dd)*",font=('HP Simplified',17)).place(relx = 0.45,rely = 0.2, anchor=CENTER)
        checkout_date = CTkEntry(details,placeholder_text = 'Checkout Date*',height=45,width=300)
        checkout_date.place(relx = 0.45,rely = 0.3, anchor=CENTER)

        CTkLabel(details,text="Name*",font=('HP Simplified',17)).place(relx = 0.15,rely = 0.4, anchor=CENTER)
        name = CTkEntry(details, placeholder_text = login_details[0][1], height=45,width=300)
        name.place(relx = 0.15,rely = 0.5, anchor=CENTER)
        name.configure(state=DISABLED)

        CTkLabel(details,text="Address*",font=('HP Simplified',17)).place(relx = 0.45,rely = 0.4, anchor=CENTER)
        address = CTkEntry(details,placeholder_text = login_details[0][2],height=45,width=300)
        address.place(relx = 0.45,rely = 0.5, anchor=CENTER)

        if login_details[0][2] == None:
            address.configure(placeholder_text = 'Enter your Address')
        else:
            address.configure(state=DISABLED)

        CTkLabel(details,text="Phone Number*",font=('HP Simplified',17)).place(relx = 0.15,rely = 0.6, anchor=CENTER)
        mobile = CTkEntry(details,placeholder_text = login_details[0][3],height=45,width=300)
        mobile.place(relx = 0.15,rely = 0.7, anchor=CENTER)

        if login_details[0][3] == None:
            mobile.configure(placeholder_text = 'Enter Phone Number')
        else:
            mobile.configure(state=DISABLED)

        CTkLabel(details,text="Email*",font=('HP Simplified',17)).place(relx = 0.45,rely = 0.6, anchor=CENTER)
        email = CTkEntry(details, placeholder_text = login_details[0][5], height=45, width=300)
        email.place(relx = 0.45,rely = 0.7, anchor=CENTER)
        email.configure(state=DISABLED)

        miscs = CTkLabel(details,text='', text_color='red')
        miscs.place(relx = 0.35,rely = 0.85, anchor=CENTER)

        fr = CTkFrame(details,height=560,width=540,corner_radius=30)
        fr.place(relx=0.8,rely=0.5,anchor=CENTER)
        CTkLabel(fr,font=('HP Simplified',30),text='Room Details').place(relx=0.5,rely=0.15,anchor=CENTER)
        CTkLabel(fr,font=('HP Simplified',15),text='Room No: %s'%(room_details[0][0])).place(relx=0.5,rely=0.25,anchor=CENTER)
        CTkLabel(fr,font=('HP Simplified',15),text='Room Type: %s'%(room_details[0][2])).place(relx=0.5,rely=0.35,anchor=CENTER)
        CTkLabel(fr,font=('HP Simplified',15),text='WiFi :%s'%(room_details[0][3])).place(relx=0.5,rely=0.45,anchor=CENTER)
        CTkLabel(fr,font=('HP Simplified',15),text='TV : %s'%(room_details[0][4])).place(relx=0.5,rely=0.55,anchor=CENTER)
        CTkLabel(fr,font=('HP Simplified',15),text='AC : %s'%(room_details[0][5])).place(relx=0.5,rely=0.65,anchor=CENTER)
        CTkLabel(fr,font=('HP Simplified',15),text='Price : %s$'%(room_details[0][6])).place(relx=0.5,rely=0.75,anchor=CENTER)
        
        CTkButton(fr,text='Proceed',height=50,width=100, command=lambda:check_entrys()).place(relx=0.5,rely=0.85,anchor=CENTER)

    #------------------FILTERS-FOR-ROOMS------------------
    filters = CTkFrame(book,height=100,width=1420)
    filters.pack()

    fil = ['All','yes','yes','yes','yes']

    def filter_all():
        cur2 = sqlcon.cursor()
        
        if fil[0] == 'All':
            cur2.execute('select * from rooms where availability = "%s" and wifi = "%s" and tv = "%s" and ac = "%s"'%(fil[1],fil[2],fil[3],fil[4]))
            fil_data = cur2.fetchall()
        else:
            cur2.execute('select * from rooms where type = "%s" and availability = "%s" and wifi = "%s" and tv = "%s" and ac = "%s"'%(fil[0],fil[1],fil[2],fil[3],fil[4]))
            fil_data = cur2.fetchall()
    
        table.configure(row=len(fil_data), column=7, values=fil_data)
        cur2.close()

    def filter_clear():
        table.configure(row=64, column=7, values=room_data)
    
    def showsignin():
        def reqdestroy(req):
            req.destroy()
        req = CTkFrame(root, width=1440, height=720)
        req.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        bottompic2 = CTkImage(Image.open('assets/loginbg.png'),size = (1440,720))
        bpic2 = CTkLabel(req,text = '', image = bottompic2)
        bpic2._image = bottompic2
        bpic2.place(relx=0.5,rely=0.5,anchor = CENTER)

        signupreq = CTkFrame(req,height=620,width=540,corner_radius=20)
        signupreq.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        CTkLabel(signupreq,corner_radius=20,text='Please Log In',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)

        root.after(2000,lambda:reqdestroy(req))

    def tableclick(cell):
        column = cell['column']
        if column == 7:
            row = cell['row']
            room_details.clear()
            room_details.insert(0,table.get()[row])
            if loggedin[0] is True:
                show_details()
            else:
                showsignin()
            
    def combobox_callback(choice):
        fil[0] = choice
    combobox = CTkComboBox(filters, font=('HP Simplified',13),values=['All', 'Single','Double','Triple','Quad'],
                                        command=combobox_callback)
    combobox.place(relx = 0.08,rely = 0.25, anchor=CENTER)
    combobox.set('All')

    check_var_avai = StringVar()
    def checkbox_avai_event():
        fil[1] = check_var_avai.get()
    checkbox_avai = CTkCheckBox(filters, font=('HP Simplified',13), text='Availability', command=checkbox_avai_event,
                                        variable=check_var_avai, onvalue='yes', offvalue='no')
    checkbox_avai.place(relx = 0.22,rely = 0.25, anchor=CENTER)
    checkbox_avai.select()
    
    check_var_wifi = StringVar()
    def checkbox_wifi_event():
        fil[2] = check_var_wifi.get()
    checkbox_wifi = CTkCheckBox(filters, font=('HP Simplified',13), text='WiFi', command=checkbox_wifi_event,
                                        variable=check_var_wifi, onvalue='yes', offvalue='no')
    checkbox_wifi.place(relx = 0.36,rely = 0.25, anchor=CENTER)
    checkbox_wifi.select()

    check_var_tv = StringVar()
    def checkbox_tv_event():
        fil[3] = check_var_tv.get()
    checkbox_tv = CTkCheckBox(filters, font=('HP Simplified',13), text='TV', command=checkbox_tv_event,
                                        variable=check_var_tv, onvalue='yes', offvalue='no')
    checkbox_tv.place(relx = 0.5,rely = 0.25, anchor=CENTER)
    checkbox_tv.select()

    check_var_ac = StringVar()
    def checkbox_event_ac():
        fil[4] = check_var_ac.get()
    checkbox_ac = CTkCheckBox(filters, font=('HP Simplified',13), text='AC', command=checkbox_event_ac,
                                        variable=check_var_ac, onvalue='yes', offvalue='no')
    checkbox_ac.place(relx = 0.635,rely = 0.25, anchor=CENTER)
    checkbox_ac.select()

    button_filter = CTkButton(filters, font=('HP Simplified',13),text='Filter',command=lambda:filter_all())
    button_filter.place(relx = 0.775,rely = 0.25, anchor=CENTER)

    button_clear = CTkButton(filters, font=('HP Simplified',13),text='Clear Filters',command=lambda:filter_clear())
    button_clear.place(relx = 0.915,rely = 0.25, anchor=CENTER)

    CTkLabel(filters,text='Sl.No.', font=('HP Simplified',13),width=250,corner_radius=0, fg_color = "#2FA572").place(relx = 0.08,rely = 0.75, anchor=CENTER)
    CTkLabel(filters,text='Availability', font=('HP Simplified',13),width=250,corner_radius=0, fg_color = "#2FA572").place(relx = 0.2,rely = 0.75, anchor=CENTER)
    CTkLabel(filters,text='Type', font=('HP Simplified',13),width=250,corner_radius=0, fg_color = "#2FA572").place(relx = 0.31,rely = 0.75, anchor=CENTER)
    CTkLabel(filters,text='WiFi', font=('HP Simplified',13),width=250,corner_radius=0, fg_color = "#2FA572").place(relx = 0.435,rely = 0.75, anchor=CENTER)
    CTkLabel(filters,text='TV', font=('HP Simplified',13),width=250,corner_radius=0, fg_color = "#2FA572").place(relx = 0.555,rely = 0.75, anchor=CENTER)
    CTkLabel(filters,text='AC', font=('HP Simplified',13),width=250,corner_radius=0, fg_color = "#2FA572").place(relx = 0.675,rely = 0.75, anchor=CENTER)
    CTkLabel(filters,text='Price', font=('HP Simplified',13),width=250,corner_radius=0, fg_color = "#2FA572").place(relx = 0.79,rely = 0.75, anchor=CENTER)
    CTkLabel(filters,text='Book', font=('HP Simplified',13),width=250,corner_radius=0, fg_color = "#2FA572").place(relx = 0.915,rely = 0.75, anchor=CENTER)

    room_scrollframe = CTkScrollableFrame(book, width=1400, height=470)
    room_scrollframe.pack()

    table = CTkTable(room_scrollframe, font=('HP Simplified',13),height=40, row=len(room_data), column=8, hover_color= '#575757', values=room_data,command=tableclick)
    table.pack(expand=False, fill='both', padx=20)

    tabview.set("About")
    cur.close()
    root.mainloop()

def call_mainapp(main):
	main.destroy()
	mainapp()

if __name__ == '__main__':
    set_appearance_mode('system')
    set_default_color_theme('green')

    loggedin = [False]
    login_details = []
    room_details = []
    booking_details = []
    
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'hotel')
    #main()
    mainapp()
    sqlcon.close()