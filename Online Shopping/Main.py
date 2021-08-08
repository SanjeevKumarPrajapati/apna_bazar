from tkinter import *
import webbrowser as wb
from PIL import ImageTk, Image
from pyautogui import click
from pyautogui import press
from keyboard import write
from time import sleep
import pyautogui
import os
import pyttsx3
import speech_recognition as sr
import tkinter
a=Tk()
alex=pyttsx3.init()
a.minsize(1370,700)
a.maxsize(1370,700)
a.title("अपना Bazar")
def f1():
    os.system("python Computer.py")
def f2():
    os.system("python Gaming.py")
def f3():
    os.system("python Cloths.py")
def f4():
    os.system("python Jewellery.py")
def redme():
    os.system("python redmi_not_7_pro.py")
def samsang_s20():
    os.system("python Samsang_Galaxy_s20.py")
def tcl_20():
    os.system("python TCL_20_pro.py")
def realme_7():
    os.system("python Realme.py")
def realme_8():
    os.system("python Realme_8.py")
def oppo():
    os.system("python Oppo_reno.py")
def nokia():
    os.system("python Nokia.py")
def oukitel():
    os.system("python Oukitel.py")
def asus():
    os.system("python Asus.py")
def iphone():
    os.system("python Iphone.py")
def fb():
    wb.open("https://www.facebook.com/baake.singh.1")
def insta():
    wb.open("https://www.instagram.com/sanjeev_kumar.10/")
def likedin():
    wb.open("https://www.linkedin.com/in/sanjeev-kumar-prajapati-bb50431b3/")
my_menu=Menu(a)
a.config(menu=my_menu)
file_menu=Menu(my_menu)
stock=Menu(my_menu)
cmp=Menu(my_menu)
gmm=Menu(my_menu)
clt=Menu(my_menu)
jw=Menu(my_menu)
con=Menu(my_menu)
my_menu.add_cascade(label="Available item ==>",menu=stock)
my_menu.add_cascade(label="Mobiles",menu=file_menu)
file_menu.add_separator()
file_menu.add_cascade(label="Redmi Not 9 Pro",command=redme)
file_menu.add_separator()
file_menu.add_cascade(label="Samsang Galaxy s20",command=samsang_s20)
file_menu.add_separator()
file_menu.add_cascade(label="TCL 20 Pro",command=tcl_20)
file_menu.add_separator()
file_menu.add_cascade(label="Realme 7(128)",command=realme_7)
file_menu.add_separator()
file_menu.add_cascade(label="Realme 8 Pro",command=realme_8)
file_menu.add_separator()
file_menu.add_cascade(label="Oppo Reno 5 Pro",command=oppo)
file_menu.add_separator()
file_menu.add_cascade(label="Nokia 3.4",command=nokia)
file_menu.add_separator()
file_menu.add_cascade(label="OUKITEL C20",command=oukitel)
file_menu.add_separator()
file_menu.add_cascade(label="Asus Zenfone 7 Pro",command=asus)
file_menu.add_separator()
file_menu.add_cascade(label="Apple iphone 11 Pro max",command=iphone)
my_menu.add_cascade(label="Computers",menu=cmp)
cmp.add_separator()
cmp.add_cascade(label="HP 14s Core i3",command=f1)
cmp.add_separator()
cmp.add_cascade(label="DELL Vostro Core i3",command=f1)
cmp.add_separator()
cmp.add_cascade(label="HP 15s Ryzen 3 ",command=f1)
cmp.add_separator()
cmp.add_cascade(label="ASUS VivoBook 15",command=f1)
cmp.add_separator()
cmp.add_cascade(label="Lenovo Core i5 9th Gen",command=f1)
cmp.add_separator()
cmp.add_cascade(label="MSI GF63 Thin Hexa",command=f1)
cmp.add_separator()
cmp.add_cascade(label="APPLE MacBook Air M1",command=f1)
cmp.add_separator()
cmp.add_cascade(label="Acer Aspire 7",command=f1)
cmp.add_separator()
cmp.add_cascade(label="Lenovo Ideapad Slim",command=f1)
cmp.add_separator()
cmp.add_cascade(label="Nokia PureBook X14",command=f1)
cmp.add_separator()
cmp.add_cascade(label="ASUS ROG Strix",command=f1)
cmp.add_separator()
cmp.add_cascade(label="HP Pavilion Gaming",command=f1)
cmp.add_separator()
cmp.add_cascade(label="MSI Modern 14",command=f1)
cmp.add_separator()
cmp.add_cascade(label="ASUS TUF Gaming",command=f1)
cmp.add_separator()
cmp.add_cascade(label="Acer Nitro Ryzen",command=f1)
my_menu.add_cascade(label="Games",menu=gmm)
gmm.add_separator()
gmm.add_cascade(label="AMKETTE Evo",command=f2)
gmm.add_separator()
gmm.add_cascade(label="AMUSING AK16 Best",command=f2)
gmm.add_separator()
gmm.add_cascade(label="VIBOTON TINJI ",command=f2)
gmm.add_separator()
gmm.add_cascade(label="Redgear Pro Series",command=f2)
gmm.add_separator()
gmm.add_cascade(label="HP K500F Wired USB",command=f2)
gmm.add_separator()
gmm.add_cascade(label="FKU E9 Game Controller",command=f2)
gmm.add_separator()
gmm.add_cascade(label="PrintMall STOP THINK",command=f2)
gmm.add_separator()
gmm.add_cascade(label="PrintMall Marvel",command=f2)
gmm.add_separator()
gmm.add_cascade(label="Logitech G923 RACING",command=f2)
gmm.add_separator()
gmm.add_cascade(label="Clapcart India",command=f2)
gmm.add_separator()
gmm.add_cascade(label="GO SHOPS Mobile",command=f2)
gmm.add_separator()
gmm.add_cascade(label="RETRACK King 2 Metal",command=f2)
gmm.add_separator()
gmm.add_cascade(label="The Printpack Mouse",command=f2)
gmm.add_separator()
gmm.add_cascade(label="AMKETTE EvoFox",command=f2)
gmm.add_separator()
gmm.add_cascade(label="QUANTUM 2 Way",command=f2)
my_menu.add_cascade(label="Cloths",menu=clt)
clt.add_separator()
clt.add_cascade(label="Color Block Men",command=f3)
clt.add_separator()
clt.add_cascade(label="Striped Men Hooded",command=f3)
clt.add_separator()
clt.add_cascade(label="Color Block Men",command=f3)
clt.add_separator()
clt.add_cascade(label="Printed Bhagalpuri",command=f3)
clt.add_separator()
clt.add_cascade(label="Printed, Embellished",command=f3)
clt.add_separator()
clt.add_cascade(label="TRIPR Men Vest",command=f3)
clt.add_separator()
clt.add_cascade(label="Solid Men Mandarin",command=f3)
clt.add_separator()
clt.add_cascade(label="Polka Print Daily",command=f3)
clt.add_separator()
clt.add_cascade(label="Full Sleeve Solid Men",command=f3)
clt.add_separator()
clt.add_cascade(label="Color Block Men Round",command=f3)
my_menu.add_cascade(label="Jewellery",menu=jw)
jw.add_separator()
jw.add_cascade(label="Alloy Gold-plated",command=f4)
jw.add_separator()
jw.add_cascade(label="Alloy Gold-plated2",command=f4)
jw.add_separator()
jw.add_cascade(label="Alloy Copper Jewel",command=f4)
jw.add_separator()
jw.add_cascade(label="Copper Gold-plated",command=f4)
jw.add_separator()
jw.add_cascade(label="Copper Gold-plated2",command=f4)
jw.add_separator()
jw.add_cascade(label="Alloy Gold-plated3",command=f4)
jw.add_separator()
jw.add_cascade(label="Zinc Gold-plated",command=f4)
jw.add_separator()
jw.add_cascade(label="Alloy Gold-plated4",command=f4)
jw.add_separator()
jw.add_cascade(label="Brass Gold-plated",command=f4)
jw.add_separator()
jw.add_cascade(label="Brass Gold-plated2",command=f4)
my_menu.add_cascade(label="Contact Info",menu=con)
con.add_separator()
con.add_cascade(label="LikedIn",command=likedin)
con.add_separator()
con.add_cascade(label="Facbook",command=fb)
con.add_separator()
con.add_cascade(label="Instagram",command=insta)
con.add_separator()
con.add_cascade(label="G-Mail : sp6406919@gmail.com")
def say(text):
        alex.say(text)
        alex.runAndWait()
def search():
    x=var.get()
    if("mobile" in x or "phone" in x):
        os.system("python Mobiles_collections.py")
    elif("computer" in x or "laptop" in x):
        os.system("python Computer.py")
    elif("game" in x):
        os.system("python Gaming.py")
    elif("cloths" in x or "t-shirt" in x or "shirt" in x or "saari" in x or "sari" in x or "jeans" in x):
        os.system("python Cloths.py")
    elif("jewellery" in x or "jewell" in x):
        os.system("python Jewellery.py")
    else:
        say("We don't have this item so sorry for that")
def speak():
    a=take()
    if("mobile" in a or "phone" in a):
        os.system("python Mobiles_collections.py")
    elif("computer" in a or "laptop" in a):
        os.system("python Computer.py")
    elif("game" in a):
        os.system("python Gaming.py")
    elif("cloths" in a or "t-shirt" in a or "shirt" in a or "saari" in a or "sari" in a or "jeans" in a):
        os.system("python Cloths.py")
    elif("jewellery" in a or "jewell" in a):
        os.system("python Jewellery.py")
    else:
        say("We don't have this item so sorry for that")
def take():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("    listening.....")
                r.pause_threshold=1
                audio=r.listen(source,timeout=1,phrase_time_limit=5)
            try:
                print("    Recognizing......")
                recog=r.recognize_google(audio,language='en-in')
                print(f"    You said : - {a}\n")
            except:
                    say("    Say that again please....")
                    return "none"
            return recog
def mobile_click_me():
    os.system("python Mobiles_collections.py")
def computer():
    os.system("python Computer.py")
def game():
    os.system("python Gaming.py")
def cloths():
    os.system("python Cloths.py")
def jewellery():
    os.system("python Jewellery.py")
lb=Label(a,text="अ",font=("Arial",50,"bold"),fg="blue").place(x=500,y=-10)
lb=Label(a,text="प",font=("Arial",50,"bold"),fg="red").place(x=550,y=-10)
lb=Label(a,text="ना",font=("Arial",50,"bold"),fg="green").place(x=600,y=-10)

lb=Label(a,text="B",font=("Arial",50,"bold"),fg="blue").place(x=680,y=-10)
lb1=Label(a,text="a",font=("Arial",50,"bold"),fg="red").place(x=730,y=-10)
lb1=Label(a,text="z",font=("Arial",50,"bold"),fg="orange").place(x=775,y=-10)
lb1=Label(a,text="a",font=("Arial",50,"bold"),fg="blue").place(x=815,y=-10)
lb1=Label(a,text="r",font=("Arial",50,"bold"),fg="green").place(x=860,y=-10)
var=StringVar()
et=Entry(a,fg="green",font=("Arial",20),borderwidth = 7,textvariable=var).place(x=500,y=80)
btn=Button(a,text="Search",bd=5,bg="orange",font=("Arial",14,"bold"),command=search).place(x=830,y=80)
bt1=Button(a,text="Speak",bd=5,bg="green",font=("Arial",14,"bold"),command=speak).place(x=940,y=80)
lab=Label(a,text="You are on अपना Bazar. You can also shop on  अपना Bazar India for millions of products with fast local delivery.",font=("Arial",15,"bold")).place(x=140,y=130)

image1 = Image.open('head1.jpg').resize((100,100))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=20, y=15)

image1 = Image.open('head2.jpg').resize((100,100))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=180, y=15)

image1 = Image.open('head3.jpg').resize((100,100))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=350, y=15)

image1 = Image.open('head4.jpg').resize((100,100))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=1070, y=15)

image1 = Image.open('head5.jpg').resize((100,100))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=1230, y=15)

image1 = Image.open('Full.jpg').resize((1360,540))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=160)

image1 = Image.open('amazonbasics.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=10, y=390)
lab=Label(a,text="Mobiles",font=("Arial",15,"bold"),fg="white",bg="blue").place(x=70,y=355)
btn=Button(a,text="Click here",bd=5,bg="yellow",font=("Arial",12,"bold"),command=mobile_click_me).place(x=60,y=646)


image1 = Image.open('computer_accessories.jpg').resize((220,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=280, y=390)
lab=Label(a,text="Computers",font=("Arial",15,"bold"),fg="white",bg="blue").place(x=337,y=355)
btn=Button(a,text="Click here",bd=5,bg="yellow",font=("Arial",12,"bold"),command=computer).place(x=340,y=646)

image1 = Image.open('gaming_accessories.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=565, y=390)
lab=Label(a,text="Gaming Accessories",font=("Arial",15,"bold"),fg="white",bg="blue").place(x=566,y=355)
btn=Button(a,text="Click here",bd=5,bg="yellow",font=("Arial",12,"bold"),command=game).place(x=615,y=646)

image1 = Image.open('dress.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=840, y=390)
lab=Label(a,text="Cloths",font=("Arial",15,"bold"),fg="white",bg="blue").place(x=905,y=355)
btn=Button(a,text="Click here",bd=5,bg="yellow",font=("Arial",12,"bold"),command=cloths).place(x=895,y=646)

image1 = Image.open('jewellery.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=1120, y=390)
lab=Label(a,text="Jewellery",font=("Arial",15,"bold"),fg="white",bg="blue").place(x=1170,y=355)
btn=Button(a,text="Click here",bd=5,bg="yellow",font=("Arial",12,"bold"),command=jewellery).place(x=1180,y=646)
a.mainloop()








