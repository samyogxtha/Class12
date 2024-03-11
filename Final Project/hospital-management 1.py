from customtkinter import *    #importing all libraries as part of python itself(no longer need to call customtkinter)(wild card entry)
from PIL import Image
import mysql.connector as msconn
import re
    
set_appearance_mode('dark')#can be changed to light
deactivate_automatic_dpi_awareness()

#----------------------------------------------------↓↓↓↓↓password checking function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------
    
def password(passentry,repassentry):
    global passwrd_check, pass_error_label, paswrd
    
    paswrd = passentry.get()
    repas = repassentry.get()
    
    passwrd_check = False
    
    length_check = False
    nmbr_check = False
    upper_check = False
    
    spl = '`\~!@\#$%^&*()_-+={[:;\\\'\"<>,.?/]}'
    spl_check = False
    
    
    if len(paswrd) > 7:
        length_check = True
    
    for i in paswrd:
    
        if i.isdigit():
            nmbr_check = True
            continue
    
        else:
    
            if i in spl:
                spl_check = True
                continue
    
            else:
    
                if i.isupper():
                    upper_check = True
                    continue
    
                else:
                    continue
    
    if length_check == spl_check == nmbr_check == upper_check == True and paswrd == repas:
        passwrd_check = True
        pass_error_label.configure(text="Password accepted", font=('Dubai', 12), text_color='Green')        
    
    else:
        if length_check is False:
            pass_error_label.configure(text="Invalid password. Must have 8 or more characters", font=('Dubai', 12), text_color='Red')            
        elif upper_check is False:
            pass_error_label.configure(text="Invalid password. Must include an upper case letter", font=('Dubai', 12), text_color='Red')        
        elif nmbr_check is False:
            pass_error_label.configure(text="Invalid password. Must include a number", font=('Dubai', 12), text_color='Red')        
        elif spl_check is False:
            pass_error_label.configure(text="Invalid password. Must include a special character", font=('Dubai', 12), text_color='Red')           
        elif paswrd != repas:
            pass_error_label.configure(text="Passwords do not match", font=('Dubai', 12), text_color='Red')          
    
#----------------------------------------------------↓↓↓↓↓signup button function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------
    
    
def signup_button():
    global pass_error_label,username, user_error_label, mob_error_label, EID_error_label, passwrd_check,user_name, emirates_id, det_check
    
    
    username = userentry.get()
    signup_cur = sqlcon.cursor()
    
    signup_cur.execute(f'select * from login where username = "{username}"')
    user_exist = signup_cur.fetchall()
    
    if user_exist == []:
    
        user_check = False
        mob_check = False
    
        space_check = False
        length_check = False
        nmbr_check = False
        upper_check = False
    
        spl = '`\~!@\#$%^&*()_-+={[:;\\\'\"<>,.?/]}'
        spl_check = False
    
    
        if len(username) > 7:
            length_check = True
    
        for i in username:
    
            if i.isdigit():
                nmbr_check = True
                continue
    
            else:
    
                if i in spl:
                    spl_check = True
                    continue
    
                else:
    
                    if i.isupper():
                        upper_check = True
                        continue
    
                    else:
                        continue
    
        if ' ' in username:
            space_check = False
    
        else:
            space_check = True
    
        if length_check == spl_check == nmbr_check == upper_check == space_check == True:
            user_check = True
    
        else:
    
            if length_check is False:
                user_error_label.configure(text="Invalid username. Must have 8 or more characters", font=('Dubai', 12), text_color='Red')    
            elif upper_check is False:
                user_error_label.configure(text="Invalid username. Must include an upper case letter", font=('Dubai', 12), text_color='Red')    
            elif nmbr_check is False:
                user_error_label.configure(text="Invalid username. Must include a number", font=('Dubai', 12), text_color='Red')        
            elif spl_check is False:
                user_error_label.configure(text="Invalid username. Must include a special character", font=('Dubai', 12), text_color='Red')    
            elif ' ' in username:
                user_error_label.configure(text="Username cannot contain spaces", font=('Dubai', 12), text_color='Red')    
        
        if user_check is True:
            user_error_label.configure(text="Username accepted.", font=('Dubai', 12), text_color='Green')    
        
        password(passentry,repassentry)
    
        mob_no = phone_entry.get()
        length_check = False
        nmbr_check = False
    
        if len(str(mob_no)) != 10:
            mob_error_label.configure(text="Phone number not valid, Please recheck", font=('Dubai', 12), text_color='Red')
    
        else:
            length_check = True
            for i in mob_no:
                if i.isdigit() == False:
                    mob_error_label.configure(text="Phone number can only contain numbers", font=('Dubai', 12), text_color='Red')
                else:
                    mob_error_label.configure(text="Phone number accepted", font=('Dubai', 12), text_color='Green')
                    nmbr_check = True
    
        if length_check == nmbr_check is True:mob_check = True

        emirates_id = EID_entry.get()
        pattern = re.compile(r'^\d{3}-?\d{4}-?\d{7}-?\d$')
    
        EID_check = False
        signup_cur.execute(f'select * from login where Emirates_ID = "{emirates_id}"')
        EID_exists = signup_cur.fetchall()
    
        if pattern.match(emirates_id) and emirates_id[0:3] == '784':
            if EID_exists == []:
                EID_error_label.configure(text="Emirates ID accepted", font=('Dubai', 12), text_color='Green')
                EID_check = True    
            else:
                EID_error_label.configure(text="Emirates ID already registered", font=('Dubai', 12), text_color='Red')

        else:
            EID_error_label.configure(text="Emirates ID Invalid", font=('Dubai', 12), text_color='Red')
        if passwrd_check == user_check == mob_check == EID_check is True:
            signup_cur.execute(f"insert into login values('{emirates_id}','{username}','{paswrd}','{mob_no}')")
            sqlcon.commit()
            signup_cur.close()
            user_name = username
            log.destroy()
            detailspage()
    
    else:
        user_error_label.configure(text="Sorry, This username is already in use.", font=('Dubai', 12), text_color='Red')

  
#----------------------------------------------------↓↓↓↓↓login button function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------
    
def login_button():
    global user_error_label, pass_error_label,username
    
    username = userentry.get()
    paswrd = passentry.get()   
    
    log_cur = sqlcon.cursor()
    log_cur.execute(f'select * from login where username = "{username}"')
    user_pass = log_cur.fetchall()
    
    if user_pass != []:
    
        if user_pass[0][1] == paswrd:
            user_error_label.destroy()
            pass_error_label.destroy()
            enter_label=CTkLabel(master=logframe, text="Welcome", font=('Dubai', 12), text_color='Lime')
            enter_label.place(x=45,y=137)
            log.after(1000,log.destroy())
            home_page()
    
        else:
            pass_error_label.configure(text="Incorrect password", font=('Dubai', 12), text_color='Red')
    
    else:
        user_error_label.configure(text="Account does not exist", font=('Dubai', 12), text_color='Red')
    
#----------------------------------------------------↓↓↓↓↓change password function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------
    
def chngpass():
    global mobentry, passentry, repassentry, mob_error_label, frgtframe, user_error_label, pass_error_label
    
    mob = mobentry.get()
    if mob.isdigit():
        if len(mob)==10:
            mobcur = sqlcon.cursor()
            mobcur.execute(f'select * from login where phone_number = {mob}')
            acc = mobcur.fetchall()
            if acc == []:
                mob_error_label.configure(text="Mobile number not registered", font=('Dubai', 12), text_color='Red')
            else:
                mob_error_label.configure(text="Mobile number accepted", font=('Dubai', 12), text_color='Green')    
                username = userentry.get()
                if acc[0][0] == username:
                    user_error_label.configure(text="Username accepted", font=('Dubai', 12), text_color='Green')
                    password(passentry,repassentry)
                    if passwrd_check is True:
                        mobcur.execute(f'update login set password = "{paswrd}" where phone_number = "{mob}"')
                        sqlcon.commit()
                        mobcur.close()
                        detailspage()
                else:
                    user_error_label.configure(text="Username not registered with this number", font=('Dubai', 12), text_color='Red')
    else:
        mob_error_label.configure(text="Mobile number not valid", font=('Dubai', 12), text_color='Green')
    
#----------------------------------------------------↓↓↓↓↓login / signup window creation↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------
    
def login_win():
    global log , logbg, logframe,  pass_error_label, user_error_label, mob_error_label, mobentry, passentry, repassentry, switchlog, switchsignup, switchfrgt
    
    #----------------------------------------------------↓↓↓↓↓forgot password frame↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------
    
    def switchfrgt():
        global userentry, passentry, repassentry, logframe, frgtframe, mobentry, pass_error_label, user_error_label, mob_error_label
    
        frgtframe = CTkFrame(master=logbg, width=320, height=360, corner_radius=15)
        frgtframe.place(relx=0.5,rely=0.5,anchor=CENTER)
    
        frgtlabel=CTkLabel(master=frgtframe, text="Change your password", font=('Dubai', 20))
        frgtlabel.place(x=50,y=45)
    
        mobentry=CTkEntry (master=frgtframe, width=220, placeholder_text="Mobile number")
        mobentry.place(x=50, y=100)
    
        userentry=CTkEntry (master=frgtframe, width=220, placeholder_text="Username")
        userentry.place(x=50, y=150)
    
        passentry=CTkEntry (master=frgtframe, width=220, placeholder_text="New password",show='*')
        passentry.place(x=50, y=200)
    
        repassentry=CTkEntry (master=frgtframe, width=220, placeholder_text="Repeat password",show='*')
        repassentry.place(x=50, y=230)
    
        user_error_label=CTkLabel(master=frgtframe, text="")
        user_error_label.place(x=45,y=135)
    
        pass_error_label=CTkLabel(master=frgtframe, text="")
        pass_error_label.place(x=45,y=192)
    
        mob_error_label=CTkLabel(master=frgtframe, text="")
        mob_error_label.place(x=45,y=230)
    
        chngbutton=CTkButton(master=frgtframe, width=220, text='Change password', corner_radius=6, command=lambda:chngpass())
        chngbutton.place(x=50,y=280)
    
        switchbutton=CTkButton(master=frgtframe, width=100, text="← back to login page", corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:switchlog())
        switchbutton.place(x=50,y=320)
    
        log.bind('<Return>',lambda event:chngpass())
    
    
    #----------------------------------------------------↓↓↓↓↓login frame↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------
    
    def switchlog():
        global userentry, passentry, logframe, pass_error_label, user_error_label
    
        log.title('LOGIN')
    
        logframe = CTkFrame(master=logbg, width=320, height=360, corner_radius=15)
        logframe.place(relx=0.5,rely=0.5,anchor=CENTER)
    
        loglabel=CTkLabel(master=logframe, text="Log into your Account", font=('Dubai', 20))
        loglabel.place(x=50,y=45)
    
        userentry=CTkEntry (master=logframe, width=220, placeholder_text="Username")
        userentry.place(x=50, y=110)
    
        passentry=CTkEntry (master=logframe, width=220, placeholder_text="Password",show='*')
        passentry.place(x=50, y=165)
    
        frgtpasbutton=CTkButton (master=logframe, text="Forgot password?", width=100, height=20, corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:switchfrgt())
        frgtpasbutton.place(x=165,y=195)
    
        pass_error_label=CTkLabel(master=logframe, text="")
        pass_error_label.place(x=45,y=192)
    
        user_error_label=CTkLabel(master=logframe, text="")
        user_error_label.place(x=45,y=135)
    
        logbutton=CTkButton(master=logframe, width=220, text='Login', corner_radius=6, command=lambda:login_button())
        logbutton.place(x=50,y=240)

        switchbutton=CTkButton(master=logframe, width=220, text="Don't have an account? sign up.", corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:switchsignup())
        switchbutton.place(x=50,y=320)
    
        log.bind('<Return>',lambda event:login_button())
    
    #----------------------------------------------------↓↓↓↓↓signup frame↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------
    
    def switchsignup():
        global repassentry, passentry, userentry, signframe,EID_entry, EID_error_label, pass_error_label, user_error_label, phone_entry, mob_error_label
    
        log.title('SIGNUP')
    
        signframe = CTkFrame(master=logbg, width=320, height=450, corner_radius=15)
        signframe.place(relx=0.5,rely=0.5,anchor=CENTER)
    
        signlabel=CTkLabel(master=signframe, text="Create new account", font=('Dubai', 20))
        signlabel.place(x=50,y=20)
    
        userentry=CTkEntry (master=signframe, width=220, placeholder_text="Username")
        userentry.place(x=50, y=70)
    
        passentry=CTkEntry (master=signframe, width=220, placeholder_text="Password",show='*')
        passentry.place(x=50, y=130)
    
        repassentry=CTkEntry (master=signframe, width=220, placeholder_text="Repeat Password",show='*')
        repassentry.place(x=50, y=165)
    
        phone_entry=CTkEntry (master=signframe, width=220, placeholder_text="Phone Number")
        phone_entry.place(x=50, y=225)
    
        EID_entry=CTkEntry (master=signframe, width=220, placeholder_text="Emirates ID")
        EID_entry.place(x=50, y=285)
    
        user_error_label=CTkLabel(master=signframe, text="", height=1)
        user_error_label.place(x=45,y=105)
    
        pass_error_label=CTkLabel(master=signframe, text="", height=1)
        pass_error_label.place(x=45,y=200)
    
        mob_error_label=CTkLabel(master=signframe, text="", height=1)
        mob_error_label.place(x=45,y=260)
    
        EID_error_label=CTkLabel(master=signframe, text="", height=1)
        EID_error_label.place(x=45,y=320)
    
        testlabel=CTkLabel(master=signframe, text="", height=1)
        testlabel.place(x=45,y=400)
    
        signbutton=CTkButton(master=signframe, width=220, text='Sign up', corner_radius=6, command=lambda:signup_button())
        signbutton.place(x=50,y=350)
    
        def del_frame():
            signframe.destroy()
            switchlog()
    
        switchbutton=CTkButton(master=signframe, width=220, text="Already have an account? Login.", corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:del_frame())
        switchbutton.place(x=50,y=410)
    
        log.bind('<Return>',lambda event:signup_button())
    
    
    #--------------------------------------------------↓↓↓↓↓creating the login window↓↓↓↓↓-------------------------------------------------------
    
    log = CTk()
    log.geometry('640x675')
    log.title('LOGIN')
    
    logimg = CTkImage(Image.open('pxfuel.jpg'),size=(1920,1080))
    logbg = CTkLabel(master=log, image=logimg)
    logbg.place(relx = 0.5,rely = 0.5,anchor = CENTER)

    switchlog()  
    log.mainloop()
#--------------------------------------------------↓↓↓↓↓creating the details page↓↓↓↓↓-------------------------------------------------------
    
def det_check():
    global user, name_entry , address_entry, insurance_entry, allergy_entry, name_error_label,allergy_error_label,address_error_label,insurance_error_label
    
    name_check = False
    address_check = False
    insurance_check = False
    
    name = name_entry.get()
    if name == '':
        name_error_label.configure(text = 'Please enter a name', font=('Dubai', 12), text_color='Red', height=1)
    else:
        name_error_label.configure(text = 'Name accepted', font=('Dubai', 12), text_color='Green', height=1)
        name_check = True
    
    address = address_entry.get()
    if address == '':
        address_error_label.configure(text = 'Please enter an address', font=('Dubai', 12), text_color='Red', height=1)
    else:
        address_error_label.configure(text = 'Address accepted', font=('Dubai', 12), text_color='Red', height=1)
        address_check = True
    
    insurance = insurance_entry.get()
    if insurance == '':
        insurance_error_label.configure(text = 'Please enter an insurance', font=('Dubai', 12), text_color='Red', height=1)
    else:
        insurance_check = True
    
    allergy = allergy_entry.get()
    
    if name_check==address_check==insurance_check is True:
        det_cur = sqlcon.cursor()
        det_cur.execute(f'insert into details values("{emirates_id}","{user}","{name}","{address}","{insurance}","{allergy}")')
        sqlcon.commit()
        det_cur.close()
        detail_win.destroy()
        home_page()
    
    
def detailspage():
    global detail_win,user, name_entry , address_entry, insurance_entry, allergy_entry, name_error_label,allergy_error_label,address_error_label,insurance_error_label
    detail_win = CTk()
    detail_win.minsize(height = 720,width = 1280)
    detail_win.title('Python Hospital')
    
    detimg = CTkImage(Image.open("home-bg.png"),size=(1920,1080))
    detbg = CTkLabel(master=detail_win, image=detimg)
    detbg.pack()
    
    user = user_name
    
    detailframe = CTkFrame(master=detail_win, width=650, height=750, corner_radius=15)
    detailframe.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    detail_label = CTkLabel(master=detailframe, text="Hello "+user+'!!,', font=('Dubai', 18), height = 1)
    detail_label.place(x=30,y=20)
    
    detail_label = CTkLabel(master=detailframe, text="Please enter the following details to make easier for you to book an appointment in the future!", font=('Dubai', 14), height = 0)
    detail_label.place(x=30,y=45)
    
    name_entry=CTkEntry (master=detailframe, width=400, placeholder_text="Full name")
    name_entry.place(x=125, y=100)
    
    name_error_label = CTkLabel(master=detailframe,text='', height = 0)
    name_error_label.place(x = 125,y = 150 )
    
    address_entry=CTkEntry (master=detailframe, width=400, placeholder_text="Address")
    address_entry.place(x=125, y=200)
    
    address_error_label = CTkLabel(master=detailframe,text='', height = 0)
    address_error_label.place(x = 125,y = 250 )
    
    insurance_entry=CTkEntry (master=detailframe, width=400, placeholder_text="Insurance")
    insurance_entry.place(x=125, y=300)
    
    insurance_error_label = CTkLabel(master=detailframe,text='', height = 0)
    insurance_error_label.place(x = 125,y = 350 )
    
    allergy_entry=CTkEntry (master=detailframe, width=400, placeholder_text="Allergies (if any)")
    allergy_entry.place(x=125, y=400)
    
    allergy_error_label = CTkLabel(master=detailframe,text='', height = 0)
    allergy_error_label.place(x = 125,y = 450 )
    
    switchbutton=CTkButton(master=detailframe, width=220, text="proceed ——>", corner_radius=6, compound='right', command=lambda:det_check())
    switchbutton.place(x=215,y=450)
    
    detail_win.mainloop()
       
#--------------------------------------------------↓↓↓↓↓creating the home page↓↓↓↓↓-------------------------------------------------------
    
def home_page():
    home_win = CTk()
    home_win.geometry("{0}x{1}+0+0".format(home_win.winfo_screenwidth(), home_win.winfo_screenheight()))
    #home_win.minsize(height = 720,width = 1280)
    home_win.title('Python Hospital')

    
    homeimg = CTkImage(Image.open("untitled.png"),size=(1920,1080))
    homebg = CTkLabel(master=home_win, image=homeimg)
    homebg.place(relx = 0.5,rely = 0.5,anchor = CENTER)
    
    tabs = CTkTabview(master=homebg, width=1080, height=800)
    tabs.place(relx = 0.5,rely = 0.5,anchor = CENTER)

    tab1 = tabs.add('about us')
    tab2 = tabs.add('book an appointment')
    tab3 = tabs.add('feedback')
    #tab4 = tabs.add('profile')
    tabs.set('about us')

    descframe = CTkFrame(master=tab1,height=500,width=360)
    descframe.place(relx=0.25,rely=0.5,anchor='center')

    details = '''                             PYTHON HOSPITAL\n
Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n 
Donec sed urna hendrerit,aliquam diam quis,vulputate erat.\n 
Orci varius natoque penatibus et magnis dis parturient\n
montes, nascetur ridiculus mus. Donec hendrerit lorem et\n
vestibulum interdum.Aliquam porta maximus sem.Sed viverra,\n
ante ut gravida pretium, augue sapien viverra lectus,non\n
cursus lectus nibh in dui. Cras mauris mi, congue non \n
orci et,blandit commodo,nisi.Suspendisse sed bibendum dui.\n
Quisque quis lectus eget nulla semper facilisis vitae \n
sit amet ante. Aliquam sit amet imperdiet risus, in \n
auctor nibh. Proin vitae nulla mi. Maecenas nisi mauris,\n
volutpat vitae tortor at, fermentum lobortis metus.\n
Praesent eget volutpat est, sit amet mattis mauris.\n
Nullacommodo lorem acurnadictum,sit amet aliqut porta.\n
Nam odio lectus,tristique at a,ultrices sit amet nisi.\n
Ut feugiat nunc nec eros ultrices aliquet.'''

    picframe = CTkFrame(master=tab1,height=500,width=360)
    picframe.place(relx=0.75,rely=0.5,anchor='center')

    hosimg = CTkImage(Image.open("darkhos.png"),size=(500,500))
    hosbg = CTkLabel(master=picframe,text='', image=hosimg)
    hosbg.place(relx=0.5,rely=0.5,anchor='center')

    desclabel = CTkLabel(master=descframe, text=details, font=('Dubai', 14), height = 0,justify = 'left')
    desclabel.place(x=15,y=0)

    feedlabel = CTkLabel(master=tab3, text='We value your feedback. \nPlease tell us what you think!!', font=('Dubai', 50), height = 0)
    feedlabel.pack()

    feedbox=CTkTextbox (master=tab3, width=700, height = 300, font=('Dubai', 20))
    feedbox.pack(pady=50)

    def feedback():
        feed = feedbox.get('0.0','end')
        feedcur = sqlcon.cursor()
        if len(feed)>1:
            try:feedcur.execute(f'insert into feedback values("{username}","{feed.strip()}")')
            except:feedcur.execute(f'insert into feedback values("{username}","{feed.strip()}")')
            sqlcon.commit()
            feedbox.delete('0.0','end')

    submitbut = CTkButton(master=tab3,text='submit!', font=('Dubai', 18),command=lambda:feedback())
    submitbut.pack(pady=15)

    frame_label = CTkLabel(master=tab2, text="choose specialization.", font=('Dubai', 20), height = 0)
    frame_label.pack(pady=10)


    catframe = CTkScrollableFrame(master=tab2,height=500,width=400,fg_color = '#333333')
    catframe.place(relx=0.5,rely=0.5,anchor='center')

    docicon=CTkImage(Image.open("docicon.jpg").resize((20,20), Image.Resampling.LANCZOS))
    button_dict = {}

    home_cur=sqlcon.cursor()
    home_cur.execute('select * from specialisations')

    spl = home_cur.fetchall()

    def spl_fn(spl_var):

        frame_label.configure(text='choose one of our amazing doctors')

        bgdocframe = CTkFrame(master=tab2,height=500,width=400)
        bgdocframe.place(relx=0.5,rely=0.5,anchor='center')
        docframe = CTkScrollableFrame(master=bgdocframe,height=500,width=400,bg_color='#333333')
        docframe.pack()
        def _back():
            frame_label.configure(text='choose specialization')
            bgdocframe.destroy()
            back_cat.destroy()

        back_cat = CTkButton(tab2,text = 'back',command = lambda:_back())
        back_cat.place(relx=0.1,rely=0.1)

        home_cur=sqlcon.cursor()
        home_cur.execute(f'select * from doctors where specialisation = "{spl_var[0]}"')

        def doctors(doc_var):
            frame_label.configure(text='what time would you like?')
            bgtimeframe = CTkFrame(master=tab2,height=500,width=400)
            bgtimeframe.place(relx=0.5,rely=0.5,anchor='center')
            timeframe = CTkScrollableFrame(master=bgtimeframe,height=500,width=400,bg_color='#333333')
            timeframe.place(relx=0.5,rely=0.5,anchor='center')

            def _back():
                frame_label.configure(text='choose one of our amazing doctors')
                bgtimeframe.destroy()
                back_cat.destroy()

            back_cat = CTkButton(tab2,text = 'back',command = lambda:_back())
            back_cat.place(relx=0.1,rely=0.1)

            
            home_cur.execute(f'select * from timings where doc_id = "{doc_var[0]}"')
            time=home_cur.fetchone()

            def doc_time(time_var):
                frame_label.configure(text='would you like to confirm your appointment?')
                apptframe = CTkFrame(master=tab2,height=480,width=425,fg_color = '#333333')
                apptframe.place(relx=0.5,rely=0.5,anchor='center')

                apptlabel = CTkLabel(master=apptframe, text=f"Appointment for {spl_var[0]} \n with Dr.{doc_var[1]} \nat {time_var}", font=('Dubai', 20), height = 0)
                apptlabel.pack(padx=100,pady=225)
                
                def accepted():
                    frame_label.configure(text='we look forward to meeting you.')
                    accframe = CTkFrame(master=tab2,height=580,width=425,fg_color = '#333333')
                    accframe.place(relx=0.5,rely=0.5,anchor='center')

                    acclabel = CTkLabel(master=accframe, text="Appointment confirmed !", font=('Dubai', 20), height = 0)
                    acclabel.pack(padx=100,pady=225)

                    def _back():
                        frame_label.configure(text='would you like to confirm your appointment?')
                        accframe.destroy()
                        back_cat.destroy()

                    back_cat = CTkButton(tab2,text = 'back',command = lambda:_back())
                    back_cat.place(relx=0.1,rely=0.1)
                
                def appt():
                    home_cur.execute(f'update timings set {time_var} = "n" where doc_id = "{doc_var[0]}"')
                    sqlcon.commit()
                    accepted()
                    
                appt_button = CTkButton(apptframe,text = 'confirm appointment',command = lambda:appt())
                appt_button.place(relx=0.63,rely=0.9)

                def _back():
                    frame_label.configure(text='what time would you like?')
                    apptframe.destroy()
                    back_cat.destroy()

                back_cat = CTkButton(tab2,text = 'back',command = lambda:_back())
                back_cat.place(relx=0.1,rely=0.1)


            for i in range(1,len(time)):
                if time[i] == 'y':
                    button_dict[i] = CTkButton(timeframe,image=docicon,width=380, text = str(5+i)+'AM',compound='left',anchor='w',command = lambda item =str(5+i)+'AM':doc_time(item))
                    button_dict[i].pack(pady=10)
                else:
                    button_dict[i] = CTkButton(timeframe,image=docicon,width=380, text = str(5+i)+'AM',compound='left',anchor='w',state = 'disabled',command = lambda item =str(5+i)+'AM':doc_time(item))
                    button_dict[i].pack(pady=10)

        doc = home_cur.fetchall()    

        docicon=CTkImage(Image.open("docicon.jpg").resize((20,20), Image.Resampling.LANCZOS))
        button_dict = {}
        for i in range(0,len(doc)):
            button_dict[i] = CTkButton(docframe,image=docicon,width=380, text = doc[i][1],compound='left',anchor='w',command=lambda item=doc[i]:doctors(item))
            button_dict[i].pack(pady=10)


    for i in range(0,len(spl)):
        button_dict[i] = CTkButton(catframe,image=docicon,width=380, text = spl[i],compound='left',anchor='w',command=lambda item=spl[i]:spl_fn(item))
        button_dict[i].pack(pady=10)
    
    #tabs.place(relheight = 0.6, relwidth = 0.6,relx=0.5,rely=0.5,anchor='center')
    
    home_win.mainloop() 

#----------------------------------------------------↓↓↓↓↓code activation↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------
    
if __name__ == '__main__':
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy',database='hospital')
    login_win()
    