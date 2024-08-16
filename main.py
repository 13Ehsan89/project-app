import os
from tkinter import *

screen=Tk()

screen.title("online shop")
screen.geometry("%dx%d+%d+%d" % (1440,900,-10,0))
screen.iconbitmap("img/SabtMahsol.ico")
screen.resizable(False,False)

def SabtMoshtari(e):
    os.system(f"python msgs/msgSabtenam.py")

def SabtMahsol(e):
    os.system(f"python msgs/msgMahsol.py")

def SabtFaktor(e):
    os.system(f"python msgs/msgFaktor.py")

"""def SabtMahsol1(e):
    os.system(f"python msgs/msgMahsol.py")"""


def exit_window():
    screen.destroy()




#image
bgimage1=PhotoImage(file="img/bbg1.png")
lblBG=Label(screen,text="*",image=bgimage1,width=1440,height=900).place(x=0,y=0)

bgimage2=PhotoImage(file="img/shop1.png")
lblBG1=Label(screen,text="*",image=bgimage2,width=209,height=113).pack(side=TOP,fill=X)

bgimage3=PhotoImage(file="img/pngcart.png")
lblBG1=Label(screen,text="*",image=bgimage3,width=250,height=125).pack(side=TOP,fill=X)



#Labels
lblsabt1=Label(screen,text="Kosar online store",font="Arial 25").pack(fill=BOTH,side=TOP)
lblsabt2=Label(screen,text="",font="Arial 25").pack(fill=BOTH,side=TOP)
lblsabt3=Label(screen,text="W E L C O M E",bg="#1c99ff",font="Arial 25",height=2).pack(fill=BOTH,side=TOP)

#Buttons
btnMoshtari=Button(screen,text="Sabt Moshtari")
btnMoshtari.configure(bg="#8cb6ff",fg="black",font="Arial 15")
btnMoshtari.bind("<Button-1>",SabtMoshtari)
btnMoshtari.place(x=655,y=440)

btnMahsol=Button(screen,text="Sabt Mahsol Va Faktor")
btnMahsol.configure(bg="#8cb6ff",font="Arial 15")
btnMahsol.bind("<Button-1>",SabtMahsol)
btnMahsol.place(x=612.5,y=530)

'''btnFaktor=Button(screen,text="Sabt Faktor",font="Arial 15",bg="#8cb6ff").place(x=662,y=360)
btnFaktor=Button(screen,text="Sabt Faktor")
btnFaktor.configure(bg="#8cb6ff",font="Arial 15")
btnFaktor.bind("<Button-1>",SabtFaktor)
btnFaktor.place(x=662,y=360)'''

closebtn=Button(screen,text="E x i t",bg="#761aed",font="Arial 18",command=exit_window)
closebtn.place(x=30,y=800)

screen.mainloop()