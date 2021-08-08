from tkinter import *
def nokia():
    import tkinter
    from PIL import ImageTk, Image
    #import QR_Code 
    b=Tk()
    b.title("Nokia 3.4")
    b.minsize(520,655)
    b.maxsize(520,655)
    def qr():
        b.minsize(500,600)
        b.maxsize(500,600)
        image1 = Image.open('qrcode.jpg')
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.pack()
        b.mainloop()
    def details():
        print("==========================================================================")
        print("\nNokia 3.4 | Android 10 | Unlocked Smartphone | 2-Day Battery | US Version | 3/64GB | 6.39-Inch Screen | Triple Camera | Charcoal\n")
        print("Price : $169.00 + $83.80 Shipping & Import Fees Deposit to India Details")
        print("\nModel Name : 3.4")
        print("Wireless Carrier : Unlocked for All Carriers")
        print("Brand : Nokia")
        print("Form Factor : Smartphone")
        print("Memory Storage Capacity : 64 GB")
        print("Cellular Technology : 4G")
        print("Operating System : 10.0")
        print("Color : Charcoal")
        print("SIM card slot count : Single SIM")
        print("\nAbout this item\n")
        print("1.) Get up to 70% better performance compared to previous generations, thanks to the newest Qualcomm Snapdragon 460 mobile platform.")
        print("2.) Enjoy all your favorite entertainment in 6.39-inch immersive HD+ with punch hole display for maximized screen real estate.")
        print("3.) Charge less and get up to two days on a single charge with the Adaptive Battery. Capture the perfect shot with triple camera AI")
        print("imaging, Portrait mode, Night mode and the ultra-wide lens.")
        print("4.) Take in a truly timeless design that's built to last, with a durable 3D Nano-textured rear cover and stunning finish in living colors.")
        print("5.) Works with all GSM carriers, including AT&T, T-Mobile, Cricket, Tracfone, Simple Mobile, Mint, and Ultra Mobile.")
        print("Includes the Nokia 3.4 smartphone, Quick start guide, charger, Type-C USB cable, and SIM tray tool.")
    def buy_now():
            qr()
    image1 = Image.open('nokia_3.4.jpg').resize((400,600))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.place(x=50,y=5)
    #lab=Label(a,text="Mobiles",font=("Arial",15,"bold"),fg="white",bg="blue").place(x=70,y=365)
    btn=Button(b,text="Buy now",bd=5,bg="yellow",font=("Arial",12,"bold"),command=buy_now).place(x=100,y=612)
    btn=Button(b,text="Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=details).place(x=300,y=612)
    b.mainloop()
nokia()
