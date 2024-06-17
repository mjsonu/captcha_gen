import random
from io import BytesIO
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import string
from captcha.image import ImageCaptcha

#creating canvas
P= tk.Tk()
P.title("Captcha")
P.configure(background="#e0b9b8")

# adding backgroung
#photobg=PhotoImage(file='5.png')
#bg= Label(P, image=photobg)
#bg.place(x=0,y=0,relwidth=1,relheight=1)

    
#font styles
myFont = font.Font(family='Consolas', weight='bold', size=30)
myFonttxt = font.Font(family='Consolas', weight='bold', size=16)
myFont1 = font.Font(family='Consolas', weight='bold', size=50)
myFont2 = font.Font(family='Cooper Black',size=25)
myFont3= font.Font(family='Cooper Black', weight='bold', size=20)



# for the first time 
image = ImageCaptcha(width = 280, height = 90)
captcha_text =str(random.randint(100000,999999))
data = image.generate(captcha_text) 
image.write(captcha_text, 'CAPTCHA2.png')

user=0

def check():
    global user
    user=txtbox.get(1.0,"end-1c")
    if (captcha_text==user):
        print("text",user)
        messagebox.showinfo("ACCEPTED","ACCEPTED")
        txtbox.delete("1.0","end")
        P.destroy()
    else:
        print("text",user)
        messagebox.showerror("ERROR","WRONG CAPTCHA RETRY") #showerror to give error
        txtbox.delete("1.0","end")
        function()
        


def imagemaker():

    # Create an image instance of the given size
    image = ImageCaptcha(width = 280, height = 90)

    # Image captcha text
    global captcha_text
    captcha_text=str(random.randint(100000,999999))
    print(captcha_text)
 
    # generate the image of the given text
    data = image.generate(captcha_text) 
 
    # write the image on the given file and save it
    image.write(captcha_text, 'CAPTCHA2.png')
    

# label making

def function():
    imagemaker()
    global user
    user=txtbox.get(1.0, "end-1c")
    img=PhotoImage(file='CAPTCHA2.png')
    button3.config(image=img)
    button3.update()
    UpdateButton()



label1= Label(P,width=20,height=1,bg="#f53163",fg="#ffffff",borderwidth=5,relief="ridge",text="CAPTCHA GENERATOR")
label1['font'] = myFont1
label1.place(x=320,y=30)


# text box creation
txtbox= tk.Text(P,height = 2,width = 40,borderwidth=5,relief="solid")
txtbox['font'] = myFonttxt
txtbox.place(x=800,y=225)


# submit button
button1= Button(P,command=check,width=10,height=1,bg="#b6666f",fg="#fef2f2",borderwidth=3,relief="raised",text="SUBMIT")
button1['font'] = myFont2
button1.place(x=850,y=500)
    
# reset button
button2= Button(P,command=function,width=10,height=1,bg="#b6666f",fg="#fef2f2",borderwidth=3,relief="raised",text="RESET")
button2['font'] = myFont2
button2.place(x=200,y=500)

#for the first time
img=PhotoImage(file='CAPTCHA2.png')
button3 = Button(P, text="CAPTCHA:: ",  width=530, height=90, fg="white", bg="#f53163",image=img,compound=RIGHT,
                 relief="solid", borderwidth=7)
button3['font'] = myFont
button3.place(x=100,y=200)



P.geometry("1920x1080")
P.state('zoomed')
P.mainloop()
