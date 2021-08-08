from tkinter import *
def samsang():
    import tkinter
    from PIL import ImageTk, Image
    #import QR_Code 
    b=Tk()
    b.title("Samsang Galaxy S20")
    b.minsize(580,655)
    b.maxsize(580,655)
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
        print("\nSamsung Galaxy S20 5G (128GB, 12GB) 6.2  120Hz AMOLED, Snapdragon 865, Canada 5G Only/Global")
        print("4G LTE (GSM + CDMA) Unlocked(AT&T, Verizon, T-Mobile, Metro) International Model SM-G981W (Cloud Blue)\n")
        print("Price : $649.99")
        print("\nModel Name : Galaxy S20 5G")
        print("Wireless Carrier : Unlocked for All Carriers")
        print("Brand : SAMSUNG")
        print("Memory Storage Capacity : 128 GB")
        print("Operating System : Android 10.0")
        print("Color : Cloud Blue")
        print("SIM card slot count : Single SIM")
        print("Display Size  : 6.2 inches AMOLED")
        print("Manufacturer : Samsung")
        print("Other camera features : Front\n")
        print("\nAbout this item\n")
        print("1.) 2G: GSM 850/900/1800/1900, 3G: HSDPA 850/900/1700(AWS)/1900/2100, 4G LTE:")
        print("1/2/3/4/5/7/8/12/13/18/19/20/25/29/30/38/39/40/41/46/66/71, 5G: n5/41/66/71 - SINGLE SIM")
        print("2.) 6.2 Quad HD+ Dynamic AMOLED 2X, Infinity-O Display, 1200 nits (peak), HDR10+, 1440 x 3200 Pixels")
        print("3.) 128GB ROM, 12GB RAM, Qualcomm SM8250 Snapdragon 865 5G (7nm+), Octa-core, Adreno 650, 4500mAh Battery")
        print("4.) Rear Camera: 64MP, f/2.0 + 12MP, f/1.8 + 12,MP, f/2.2, Front Camera: 10MP, f/2.2")
        print("5.) International Model - NO US Warranty. Canada 5G. Global 4G LTE. Compatible with Most GSM and CDMA Carriers like T-Mobile,")
        print("AT&T, MetroPCS, etc. Will Also work with CDMA Carriers Such as Verizon, Sprint.")
    def buy_now():
            qr()
    image1 = Image.open('samsang.jpg').resize((500,600))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.place(x=50,y=5)
    #lab=Label(a,text="Mobiles",font=("Arial",15,"bold"),fg="white",bg="blue").place(x=70,y=365)
    btn=Button(b,text="Buy now",bd=5,bg="yellow",font=("Arial",12,"bold"),command=buy_now).place(x=145,y=612)
    btn=Button(b,text="Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=details).place(x=400,y=612)
    b.mainloop()
samsang()
