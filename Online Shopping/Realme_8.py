from tkinter import *
def realme():
    import tkinter
    from PIL import ImageTk, Image
    #import QR_Code 
    b=Tk()
    b.title("Realme 8 Pro")
    b.minsize(410,655)
    b.maxsize(410,655)
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
        print("\nRealme 8 Pro 128GB 8GB RAM RMX3081 (Global) 6.4 108MP Factory Unlocked (Black/Negro Infinito)")
        print("Price : $349.99")
        print("\nModel Name : Realme 8 Pro")
        print("Wireless Carrier : Unlocked for All Carriers")
        print("Brand : Realme")
        print("Form Factor : Smartphone")
        print("Memory Storage Capacity : 128 GB")
        print("Cellular Technology : 4G")
        print("Operating System : Android 10.0")
        print("Color : Black/Negro Infinito")
        print("SIM card slot count : Single SIM")
        print("Display Size  : 6.4 inches LCD")
        print("Package Dimensions : 6.85 x 3.62 x 2.44 inches; 6.21 Ounces")
        print("Manufacturer : Realme Chongqing Mobile Telecommunications Corp., Ltd.\n")
        print("\nAbout this item\n")
        print("1.) Will NOT work on Verizon/BOOST/CRICKET or any CDMA Carrier. 4G VoLTE Worldwide Unlocked Dual Nano sim")
        print("2.) Dual Nano Sim LTE Bands: FDD: 1/2/3/4/5/7/8/20/28 TDD: 38/40/41 3G h+: 1/2/4/5/8 GSM Quad Band")
        print("3.) 108MP Quad Camera + 32Mp Selfie Camera Octa-core CPU, 8nm, up to 2.3GHz")
        print("4.) 6.4 LCD Super Amoled 180Hz Touch Sampling Rate")
        print("5.) Fast charging 50W, 50% in 17 min, 100% in 65 min (advertised)")
    def buy_now():
            qr()
    image1 = Image.open('realme8jpg.jpg').resize((300,600))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.place(x=50,y=5)
    #lab=Label(a,text="Mobiles",font=("Arial",15,"bold"),fg="white",bg="blue").place(x=70,y=365)
    btn=Button(b,text="Buy now",bd=5,bg="yellow",font=("Arial",12,"bold"),command=buy_now).place(x=100,y=612)
    btn=Button(b,text="Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=details).place(x=230,y=612)
    b.mainloop()
realme()
