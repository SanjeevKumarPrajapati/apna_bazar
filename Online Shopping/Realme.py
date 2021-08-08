from tkinter import *
def realme():
    import tkinter
    from PIL import ImageTk, Image
    #import QR_Code 
    b=Tk()
    b.title("Realme 7(128)")
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
        print("\nRealme 7 (128GB, 8GB) 6.5 90Hz Display, 30W Fast Charge, MediaTek")
        print("Helio G95, GSM Unlocked Global 4G LTE International Model (Mist Blue)")
        print("Price : $258.76")
        print("\nModel Name : Realme 7")
        print("Wireless Carrier : Unlocked for All Carriers")
        print("Brand : Realme")
        print("Form Factor : Smartphone")
        print("Memory Storage Capacity : 128 GB")
        print("Cellular Technology : 4G,2G")
        print("Operating System : Android 10.0")
        print("Color : Marine Blue")
        print("SIM card slot count : Single SIM")
        print("Display Size  : 6.5 inches AMOLED")
        print("Package Dimensions : 7.17 x 3.66 x 2.52 inches; 1.08 Pounds")
        print("Manufacturer : Realme\n")
        print("\nAbout this item\n")
        print("Realme 7 128GB is a mid-range smartphone, offering an impressive spec sheet.")
        print("The device flaunts an amazing camera setup backed up by a 5000mAh battery compatible")
        print("with 30W Super Dart charging technology, facilitating long photography sessions. Further, considering")
        print("the price range of the device its massive 128GB internal storage backed up by 8GB RAM, makes it a buyers' delight.")
    def buy_now():
            qr()
    image1 = Image.open('realme_7.jpg').resize((400,600))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.place(x=50,y=5)
    #lab=Label(a,text="Mobiles",font=("Arial",15,"bold"),fg="white",bg="blue").place(x=70,y=365)
    btn=Button(b,text="Buy now",bd=5,bg="yellow",font=("Arial",12,"bold"),command=buy_now).place(x=100,y=612)
    btn=Button(b,text="Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=details).place(x=300,y=612)
    b.mainloop()
realme()
