from tkinter import *
def redmi_not_7_pro():
    import tkinter
    from PIL import ImageTk, Image
    #import QR_Code 
    b=Tk()
    b.title("Redmi Not 9 Pro")
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
        print("======================================================================================\n")
        print("Xiaomi Redmi Note 9 Pro 128GB + 6GB RAM, 6.67 FHD+ DotDisplay, 64MP AI Quad Camera, Qualcomm Snapdragon 720G")
        print("LTE Factory Unlocked Smartphone - International Version (Tropical Green)")
        print("\nXiaomi Rougemi Note 9 Smartphone - 4 GB + 128 GB, Verde (Forest Green)\n")
        print("Price : $217.50")
        print("Available at a lower price from other sellers that may not offer free Prime shipping.")
        print("Model Name	Xiaomi Redmi Note 9")
        print("Wireless Carrier : Unlocked")
        print("Brand : Xiaomi")
        print("Form Factor : Smartphone")
        print("Memory Storage Capacity : 128 GB")
        print("Operating System  : Android 9.0")
        print("Color : Forest Green")
        print("Cellular Technology : 4G")
        print("SIM card slot count : Dual SIM")
        print("Model Year : 2020")
        print("\n================\n")
        print("About this item\n")
        print("1.) FDD-LTE: B1/3/7/8/20/28/38/40 - Supports dual SIM VoLTE HD calling > (ensure to check compatibility with your carrier before purchase")
        print("2.) 6.53 ”FHD + DotDisplay 2340x1080 FHD+ - Corning Gorilla Glass 5 front and TÜV Rheinland low blue light certification - Splash-proof nano coating")
        print("3.) 128GB + 4GB RAM - MTK Helio G85 High-performance octa-core processor - 5020mAh Ultra high capacity battery - 2.4G Wi-Fi / 5G Wi-Fi")
        print("4.) Rear Main Camera: 48MP AI quad camera, 8MP ultra wide-angle camera, 2MP Macro camera, 2MP depth camera - Front Camera: 13MP in-display")
        print("5.) Factory Unlocked cellphones are compatible with most of the GSM carriers ( Like T-Mobile or AT&T ) but please be aware that are not compatible")
        print("with CDMA carriers (Like Sprint or Verizon Wireless for example) - FCC ID: 2AFZZJ15SS")
    def buy_now():
        qr()
    image1 = Image.open('redmi9pro1.jpg').resize((500,600))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.place(x=50,y=5)
    #lab=Label(a,text="Mobiles",font=("Arial",15,"bold"),fg="white",bg="blue").place(x=70,y=365)
    btn=Button(b,text="Buy now",bd=5,bg="yellow",font=("Arial",12,"bold"),command=buy_now).place(x=135,y=612)
    btn=Button(b,text="Details",bd=5,bg="yellow",font=("Arial",12,"bold"),command=details).place(x=400,y=612)
    b.mainloop()
redmi_not_7_pro()