from tkinter import *
import math

def leftClickButton(event):
    average = (float(textboxWeight.get())/math.pow(float(textboxHight.get())/100,2))
    if average > 30 :
       lableresult.configure(text = "อ้วนมาก")
    elif average > 25 :
        lableresult.configure(text ="อ้วน")
    elif average > 23 :
        lableresult.configure(text ="น้ำหนักเกิน")
    elif average > 18.6 :
        lableresult.configure(text = "ปกติ")
    elif average < 18.5 :
        lableresult.configure(text ="ผอมไป")

MainWindow = Tk()
lableHight = Label(MainWindow,text="high (cm.)")
lableHight.grid(row=0,column=0)
textboxHight = Entry(MainWindow)
textboxHight.grid(row=0,column=1)
lableWeight = Label(MainWindow,text="weight (Kg.)")
lableWeight.grid(row=1,column=0)
textboxWeight = Entry(MainWindow)
textboxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวณ")
calculateButton.bind("<Button-1>",leftClickButton)
calculateButton.grid(row=2,column=0)
lableresult = Label(MainWindow,text="ผลลัพธ์")
lableresult.grid(row=2,column=1)
MainWindow.mainloop()