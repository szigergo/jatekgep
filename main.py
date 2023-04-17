from tkinter import *
from random import choice
import random
from random import choice, random
import time
import os
from PIL import Image, ImageTk

import winsound
import pygame as pg
pg.mixer.init()
os.system('cls')
lehetosegek = "🍒", "🍉", "🔔", "🍇", "💰", "🍀"
lnyer = "🍒🍒🍒", "🔔🔔🔔", "🍉🍉🍉", "🍇🍇🍇", "💰💰💰"
eredmeny = 'Üdv!'
indulj = True

def play_sound_porgeteseleje():
    BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\porgeteseleje.wav"))
    BULLET_HIT_SOUND.play()
    
def play_sound_porgetesvege():
    BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\porgetesvege.wav"))
    BULLET_HIT_SOUND.play()

def play_sound_indulas():
    BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\indulas.wav"))
    BULLET_HIT_SOUND.play()

nyeresilehetoseg = 0.17
paswd = ""

def t2():
        global cseresznye, harang, szolo, dinye, penz, levonas, tsillag, nyeresilehetoseg
        nyeresilehetoseg = 0.17
        cseresznye = 2
        harang = 4
        szolo = 10
        dinye = 14
        penz = 20
        levonas = 2
        tsillag = 200


t2()

def exit():
    root.destroy()
    pt.destroy()
    tet.destroy()
    win.destroy()
    db.destroy()
    os.system('cls')
with open('Assets\Documentacion\ellenorzes.txt', 'r') as forrrasfajl:
    
    ell = forrrasfajl.readline()

    if ell == 'Eredeti szoftver!':
        print()

getfut4 = True
def tetelek():
    global cseresznye, harang, szolo, dinye, penz, levonas, tsillag, tet, getfut4
    if getfut4 == True:
        tet = Tk()
        tet.geometry('250x150+506+0')
    def t2():
        BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\ptetvalasztas.wav"))
        BULLET_HIT_SOUND.play()
        global cseresznye, harang, szolo, dinye, penz, levonas, tsillag, nyeresilehetoseg
        nyeresilehetoseg = 0.17
        cseresznye = 2
        harang = 4
        szolo = 10
        dinye = 14
        penz = 20
        tsillag = 200
        levonas = 2
        pt.destroy()

        megnyitas()

    def t5():
        BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\ptetvalasztas.wav"))
        BULLET_HIT_SOUND.play()
        global cseresznye, harang, szolo, dinye, penz, levonas, tsillag, nyeresilehetoseg
        nyeresilehetoseg = 0.16
        cseresznye = 5
        harang = 10
        szolo = 25
        dinye = 35
        penz = 50
        levonas = 5
        tsillag = 500
        pt.destroy()
        
        megnyitas()

    def t10():
        BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\ptetvalasztas.wav"))
        BULLET_HIT_SOUND.play()
        global cseresznye, harang, szolo, dinye, penz, levonas, tsillag, nyeresilehetoseg
        nyeresilehetoseg = 0.15
        cseresznye = 10
        harang = 20
        szolo =50
        dinye = 70
        penz = 100
        levonas = 10
        tsillag = 1000
        pt.destroy()
        megnyitas()
    if getfut4 == True:
        getfut4 = False
        
        tet2 = Button(tet, text="Tét 2", command=t2)
        tet2.pack()
        tet5 = Button(tet, text="Tét 5", command=t5)
        tet5.pack()
        tet10 = Button(tet, text="Tét 10", command=t10)
        tet10.pack()
        et = Button(tet, text="Kilépés", command=exit)
        et.pack()
    def megnyitas():
        pontozas()


nyv_eredmeny = ""
getfut5 = True
def nyertel():
    global nyv, labelnyv, cslabel

    nyv = Tk()
    nyv.geometry("756x150+0+151")
    font = ("Helvetica", 45)
    labelnyv = Label(nyv, text=nyv_eredmeny, font=font)
    labelnyv.pack()
    font = ("Helvetica", 30)
    cslabel = Label(nyv, text='', font=font)
    cslabel.pack()













def duplazas():
    
    global score, db
    db = Tk()
    db.geometry("756x150+0+302")
    scoresave = 0
    scoresave = score
    choicecomp = "1", "2"
    
    def generald():
        global eredmeny
        eredmeny = ''.join(
            choice(choicecomp) for i in range(1)
        )
        

    def piros():
        global bonuspont, score
        generald()
        userchoice = "2"
        if eredmeny == userchoice:
            bonuspont * 2
        else:
            bonuspont = 0
           
            db.destroy()
            button16.config(state= NORMAL)
            score == scoresave

    def fekete():
        global bonuspont, score
        generald()
        userchoice = "1"
        if eredmeny == userchoice:
            bonuspont * 2

        else:
            bonuspont = 0
            
            db.destroy()
            button16.config(state= NORMAL)
            score == scoresave
    
    def feliras():
        global score
        global bonuspont
        score += bonuspont
        
        bonuspont = 0
        db.destroy()
        button16.config(state= NORMAL)
        score_label.config(font=font)
        root.after(lambda: score_label.config(text=eredmeny))
        
        

    dbb1 = Button(db, text="Fekete", command=fekete)
    dbb1.pack()
    dbb2 = Button(db, text ="Piros", command=piros)
    dbb2.pack()
    dbb3 = Button(db, text="Felírás", command=feliras)
    dbb3.pack()
    db.mainloop()




indulj = True
def pontozas():
    global pt, indulj
    pt = Tk()
    pt.title("Cseresznyés játék")
    pt.geometry('250x150+0+0')
    ptl = Label(pt, text=f"🍒🍒🍒 = {cseresznye}\n🔔🔔🔔  = {harang}\n🍇🍇🍇 = {szolo}\n🍉🍉🍉 = {dinye}\n💰💰💰 = {penz}\n🍀🍀🍀 = {tsillag}", font=200)
    ptl.pack()
        
    if indulj == True:
    
        tetelek()
        nyertel()
        
        indulj = False

    pt.mainloop()
    

def aktivacio():
    global aktiva, ell
    def valami():
        global aktiva, kap
        aktiva = inp.get()
        if aktiva == "5O1R3-VQ0Q1-F5ZEE-MBVSC":
            with open('Assets\Documentacion\ellenorzes.txt', 'w') as forrrasfajl:
                print("Eredeti szoftver!", file=forrrasfajl)
                akt.destroy()
        elif aktiva == 'freetrial':
            print
            akt.destroy()

    akt = Tk()
    akt.configure(bg='white')
    akt.title("Cseresznyés játék")
    akt.geometry('250x150')
    inp = Entry(akt)
    inp.pack()

    
    button1 = Button(akt, text="Aktiválás", command=valami)
    button1.pack()
    
    
    akt.mainloop()

with open('Assets\Documentacion\ellenorzes.txt', 'r') as forrrasfajl:
    ell = forrrasfajl.readline()
    def akarmi():
        if aktiva == 'freetrial':
            print()
        else:
            exit()

    if ell == "freetrial":
        aktivacio()
        akarmi()

scorem = "0"

root = Tk()
root.configure(bg='white')
root.title("Cseresznyés játék")
root.geometry('256x156+250+0')

image1 = Image.open("Assets\Images\image .png")

newpic1 = ImageTk.PhotoImage(image1)
label1 = Label(root, image=newpic1)
label1.image = newpic1
label1.place(x=0, y=0)

score_labelpont = Label(text=f"Score: {scorem}", font=150)
score_labelpont.place(x=8, y=8)

score_label = Label(text="Üdv!", font=150)
bevitel = ""
getfut1 = True
def exit():
    root.destroy()
    pt.destroy()
    tet.destroy()
    nyv.destroy()
    win.destroy()
    db.destroy()
    os.system('cls')
gtefut2 = True
def get():
    global paswd, nyeresilehetoseg, getfut1, getfut2
    
    print(paswd)
    paswd = input('Írd be a jelszót: ')
    os.system('cls')
    if paswd == 'valamin':
        os.system('cls')
        print('Üdvözöllek Felhasználó!\nAz alábbi dolgokhoz van jogod a programban:\nAz eredmény előre megtekintése.')
        getfut1 == "code"
        getfut2 = False
        root.after(5000, lambda: os.system('cls'))
        nyv.destroy()
    
    elif paswd == 'rootpwd':
        os.system('cls')
        getfut2 = False
        print('Üdvözöllek Ferfo1!\nAz alábbi dolgokhoz van jogod a programban:\nAz eredmény előre megtekintése.\nNyerési esély beállítása.')
        getfut1 = "code"
        root.after(5000, lambda: os.system('cls'))
        nyeresl()
        nyv.destroy()
    elif paswd == "freeoff":
        with open('Assets\Documentacion\ellenorzes.txt', 'w') as forrrasfajl:
            print("Eredeti szoftver!", file=forrrasfajl)
    else: 
        getfut1 = False
            

button1 = Button(text="", command=get, border=0)
button1.pack(padx=9, pady=7)
font = ("Helvetica", 45)

def loading_animation():
    
    
    button16.config(state= DISABLED)
    play_sound_porgeteseleje()
    global paswd, getfut1
    font = ("Helvetica", 45)
    if paswd == "valamin":
        print
        button16.config(state= NORMAL)
        score_label.config(font=font)
        root.after(1, lambda: score_label.config(text=eredmeny))
    elif paswd == "rootpwd":
        score_label.config(font=font)
        root.after(1, lambda: score_label.config(text=eredmeny))
        button16.config(state= NORMAL)
    else:
        button16.config(state= DISABLED)
        score_label.config(text="💰💰💰", font=font)

        root.after(0, lambda: score_label.config(text="🍒💰💰"))
        root.after(500, lambda: score_label.config(text="💰🍒💰"))
        root.after(1000, lambda: score_label.config(text="💰💰🍒"))

        root.after(1500, lambda: score_label.config(text="🍒💰💰"))
        root.after(2000, lambda: score_label.config(text="💰🍒💰"))
        root.after(2500, lambda: score_label.config(text="💰💰🍒"))

        root.after(3000, lambda: score_label.config(text=eredmeny))

        root.after(3000, lambda: play_sound_porgetesvege())
        if getfut1 == True:
            root.after(3000, lambda: button16.config(state= NORMAL))
            getfut1 = False
        elif getfut1 == "code":
            button16.config(state=NORMAL)


    font = ("Helvetica", 45)


   
root.after(1, lambda: loading_animation())



def nyeresl():
    global win, entry
    win= Tk()
    win.configure(bg='white')
    win.title("Cseresznyés játék")
    win.geometry('250x170+756+0')
    button1 = Button(win, text="25", command=egy)
    button1.pack()
    button2 = Button(win, text="50", command=ketto)
    button2.pack()
    button3 = Button(win, text="100", command=harom)
    button3.pack()
    button3 = Button(win, text="Jogosultság kikapcsolása.", command=koff)
    button3.pack()
    button4 = Button(win, text="Loading bekapcsolása", command=loadoff)
    button4.pack()
    entry = Entry(win)
    entry.pack()
    button5 = Button(win, text="Beírt egyenleg jóváírása.", command=entryny)
    button5.pack()
    win.mainloop()

def entryny():
    global score
    bevittosszeg = entry.get()
    azossz = int(bevittosszeg)
    score += azossz

def loadoff():
    global paswd, getfut1
    paswd = "eznemajelszo"
    getfut1 = False


def egy():
    global nyeresilehetoseg
    nyeresilehetoseg = 0.25
    
def ketto():
    global nyeresilehetoseg
    nyeresilehetoseg = 0.5
    

def harom():
    global nyeresilehetoseg
    nyeresilehetoseg = 1
    

def koff():
    global paswd, getfut1
    paswd = ''
    win.destroy()
    getfut1 = False
getfut = 3


def csillagzas():
    global cs
    root.after(3000, lambda:cslabel.configure(text='⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐'))
    root.after(3500, lambda:cslabel.configure(text=''))
    root.after(4000, lambda:cslabel.configure(text='⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐'))
    root.after(4500, lambda:cslabel.configure(text=''))
    root.after(5000, lambda:cslabel.configure(text='⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐'))
    root.after(5500, lambda:cslabel.configure(text=''))
    root.after(6000, lambda:cslabel.configure(text='⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐'))
    root.after(6500, lambda:cslabel.configure(text=''))
    root.after(7000, lambda:cslabel.configure(text='⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐'))
    root.after(7500, lambda:cslabel.configure(text=''))              

def futtats():
    global button16
    button16.config(state=NORMAL)

score = 100
getfut3 = True
getfut2 = True
def generalas():
    global paswd, getfut, score, score_labelpont, scorem, nyv_eredmeny, labelnyv, time, getfut3, button16, getfut1, bonuspont
    if getfut3 == True:
        play_sound_indulas()
        getfut3 = False
    getfut2 = True

    def futtats():
        root.after(3000, duplazas())

    loading_animation()
    time = 8500
    score -= levonas
    score = int(score)
    scorem = f"{score}        "
    score_labelpont.config(text=f"Score: {scorem}", font=150)


    if ell == "freetrial":
        getfut -= 1
    global eredmeny
    if getfut < 0:
        root.destroy()
        aktivacio()
    import random
    random_float = random.uniform(0,1)

    from random import choice, random
    if random_float <= nyeresilehetoseg:
        if random_float <= 0.01:
            eredmeny = "🍀🍀🍀"
        else:
            eredmeny = ''.join(
                choice(lnyer) for i in range(1)
            )
            
        
    else:
        eredmeny = ''.join(
            choice(lehetosegek) for i in range(3)
        )


    time = 8500
    if eredmeny == "🍒🍒🍒":
        
        root.after(250)
        
        bonuspont = cseresznye
        score = int(score)
        csillagzas()

        if getfut2 == True:
            nyv.after(3000, lambda:labelnyv.config(text="Gratulálok, nyertél!"))
            BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\pnyeres.wav"))
            nyv.after(3000, lambda: BULLET_HIT_SOUND.play())
            nyv.after(time, lambda:labelnyv.config(text=""))
            root.after(3000, lambda:futtats())
           

    

    elif eredmeny == "🍉🍉🍉":
        root.after(250)
        
        bonuspont = dinye
        score = int(score)

        csillagzas()
        if getfut2 == True:
            nyv.after(3000, lambda:labelnyv.config(text="Gratulálok, nyertél!"))
            BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\pnyeres.wav"))
            nyv.after(3000, lambda: BULLET_HIT_SOUND.play())
            nyv.after(time, lambda:labelnyv.config(text=""))
            root.after(0, lambda: button16.config(state= DISABLED))
            root.after(3000, lambda:futtats())
            
            
    

    elif eredmeny == "🔔🔔🔔":
        root.after(250)
        
        bonuspont = harang
        score = int(score)
        csillagzas()

        if getfut2 == True:
            nyv.after(3000, lambda:labelnyv.config(text="Gratulálok, nyertél!"))
            BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\pnyeres.wav"))
            nyv.after(3000, lambda: BULLET_HIT_SOUND.play())
            nyv.after(time, lambda:labelnyv.config(text=""))
            root.after(3000, lambda:futtats())
            

    

    elif eredmeny == "🍇🍇🍇":
        root.after(250)
        
        bonuspont = szolo
        score = int(score)
        csillagzas()

        if getfut2 == True:
            nyv.after(3000, lambda:labelnyv.config(text="Gratulálok, nyertél!"))
            BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\pnyeres.wav"))
            nyv.after(3000, lambda: BULLET_HIT_SOUND.play())
            nyv.after(time, lambda:labelnyv.config(text=""))
            root.after(3000, lambda:futtats())
           



    elif eredmeny == "💰💰💰":
        root.after(250)
        
        bonuspont = penz
        score = int(score)
        csillagzas()

        if getfut2 == True:
            nyv.after(3000, lambda:labelnyv.config(text="Gratulálok, nyertél!"))
            BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\pnyeres.wav"))
            nyv.after(3000, lambda: BULLET_HIT_SOUND.play())
            nyv.after(time, lambda:labelnyv.config(text=""))
            root.after(3000, lambda:futtats())

    
    elif eredmeny == "🍀🍀🍀":
        root.after(250)
        
        bonuspont = tsillag
        score = int(score)
        csillagzas()

        if getfut2 == True:
            nyv.after(3000, lambda:labelnyv.config(text="Gratulálok, nyertél!"))
            BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join("Assets\Sounds\pnyeres.wav"))
            nyv.after(3000, lambda: BULLET_HIT_SOUND.play())
            nyv.after(time, lambda:labelnyv.config(text=""))
            root.after(3000, lambda:futtats())
            
            

    else:

        time = 4000
        score = int(score)
        root.after(time, lambda: button16.config(state= NORMAL))
        if getfut2 == True:
            nyv.after(3000, lambda:labelnyv.config(text="Sajnálom, vesztettél!"))
            nyv.after(time, lambda:labelnyv.config(text=""))
            
            
            
 

    if score <= 0:
    
        exit()
    if score <= 10:
        scorem = f"{score}        "
    else:
        scorem = f"{score}        "

    





    

if paswd == 'valami':
    button1 = Button(text="25", command=egy)
    button1.pack()
    button2 = Button(text="50", command=ketto)
    button2.pack()
    button3 = Button(text="100", command=harom)
    button3.pack()
    
button16 = Button(text="Pörgetés", command=generalas)
button16.pack()

score_label = Label(root, text=eredmeny)
score_label.pack()

pontozas()



root.mainloop()






 
