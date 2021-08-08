from tkinter import *
from PIL import ImageTk, Image
import tkinter
import os
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
a=Tk()
a.minsize(1370,700)
a.maxsize(1370,700)
a.title("Mobiles")
lab=Label(a,text="Redmi Not 9 Pro",font=("Arial",15,"bold")).place(x=40,y=2)
image1 = Image.open('redmi9pro1.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=10, y=30)
btn=Button(a,text="More Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=redme).place(x=55,y=290)

lab=Label(a,text="Samsang Galaxy s20",font=("Arial",15,"bold")).place(x=300,y=2)
image1 = Image.open('samsang.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=300, y=30)
btn=Button(a,text="More Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=samsang_s20).place(x=345,y=290)

lab=Label(a,text="TCL 20 Pro",font=("Arial",15,"bold")).place(x=630,y=2)
image1 = Image.open('tcl_20.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=580, y=30)
btn=Button(a,text="More Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=tcl_20).place(x=632,y=290)

lab=Label(a,text="Realme 7(128)",font=("Arial",15,"bold")).place(x=890,y=2)
image1 = Image.open('realme_7.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=850, y=30)
btn=Button(a,text="More Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=realme_7).place(x=893,y=290)

lab=Label(a,text="Realme 8 Pro",font=("Arial",15,"bold")).place(x=1165,y=2)
image1 = Image.open('realme8jpg.jpg').resize((150,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=1150, y=30)
btn=Button(a,text="More Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=realme_8).place(x=1170,y=290)


lab=Label(a,text="Oppo Reno 5 Pro",font=("Arial",15,"bold")).place(x=40,y=350)
image1 = Image.open('oppo.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=10, y=380)
btn=Button(a,text="More Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=oppo).place(x=55,y=640)

lab=Label(a,text="Nokia 3.4",font=("Arial",15,"bold")).place(x=345,y=350)
image1 = Image.open('nokia_3.4.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=300, y=380)
btn=Button(a,text="More Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=nokia).place(x=345,y=640)

lab=Label(a,text="OUKITEL C20",font=("Arial",15,"bold")).place(x=620,y=350)
image1 = Image.open('oukitel_c20.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=580, y=380)
btn=Button(a,text="More Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=oukitel).place(x=632,y=640)

lab=Label(a,text="Asus Zenfone 7 Pro",font=("Arial",15,"bold")).place(x=860,y=350)
image1 = Image.open('asus_zenfone.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=850, y=380)
btn=Button(a,text="More Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=asus).place(x=893,y=640)

lab=Label(a,text="Apple iphone 11 Pro max",font=("Arial",15,"bold")).place(x=1112,y=350)
image1 = Image.open('apple_iphone.jpg').resize((200,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=1130, y=380)
btn=Button(a,text="More Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=iphone).place(x=1176,y=640)

a.mainloop()
