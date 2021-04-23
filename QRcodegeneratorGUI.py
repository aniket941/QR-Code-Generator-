from tkinter import *
import os
import pyqrcode

window = Tk()
window.title("QR Code Generator")
window.geometry('600x600')
window.config(bg='powderblue')

def generate():
    if len(Subject.get())!=0 :
        global qr,photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showinfo("Please Enter some Subject")
    try:
        showcode()
    except:
        pass

def showcode():
    imageLabel.config(image = photo)
    subLabel.config(text="QR of " + Subject.get())

def save():
    dir = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get())!=0:
            qr.png(os.path.join(dir,name.get()+".png"),scale=8)
        else:
            messagebox.showinfo("Please enter a File Name")
    except:
        messagebox.showinfo("Generate the QR code first!")

Sub = Label(window,text="Enter subject" )
Sub.place(x = 20 ,y = 20)

FName = Label(window,text="Enter FileName")
FName.place( x = 20, y = 70)

Subject = StringVar()
SubEntry = Entry(window,textvariable = Subject)
SubEntry.place(x = 120, y = 20)

name = StringVar()
nameEntry = Entry(window,textvariable = name)
nameEntry.place(x = 120, y = 70)

button = Button(window,text = "Generate",width=15,command = generate)
button.place(x = 270, y = 20)

imageLabel = Label(window)
imageLabel.place(x = 220, y = 140)

subLabel = Label(window,text="")
subLabel.place(x = 300, y = 500)

saveB = Button(window,text="Save as PNG",width=15,command = save)
saveB.place(x = 270, y = 70)

#making this resposnsive
Rows = 3
Columns = 3

for row in range(Rows+1):
    window.grid_rowconfigure(row,weight=1)

for col in range(Columns+1):
    window.grid_columnconfigure(col,weight=1)

 
window.mainloop()
