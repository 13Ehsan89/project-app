import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

screen=Tk()


screen.title("Sabt Mahsol")
screen.geometry("%dx%d+%d+%d" % (1440,900,-10,0))
screen.iconbitmap("img/SabtMahsol.ico")
screen.resizable(False,False)


#Label
entMahsol=Label(screen,text="Protein",font="Areal 30").place(x=80,y=650)
entMahsol1=Label(screen,text="Drinks",font="Areal 30").place(x=350,y=650)
entMahsol2=Label(screen,text="Rise",font="Areal 30").place(x=600,y=650)
entMahsol3=Label(screen,text="Vegetables",font="Areal 30").place(x=900,y=650)
entMahsol4=Label(screen,text="Hobobat",font="Areal 30").place(x=1200,y=650)

Name=StringVar()
Brand=StringVar()
Gheymat=StringVar()
Tedad=StringVar()

#Entry
'''entMahsolname1=(Entry(screen,font="Areal 15",textvariable=Name))
entMahsolname1.place(x=100,y=220)

combotext=ttk.Combobox(screen,state="readonly",textvariable=Brand,justify="left",height=30,width=35)
valuescombo=["Irani","Khareji"]
combotext["value"]=valuescombo
combotext.place(x=100,y=280)

entMahsolname3=Entry(screen,font="Areal 15",textvariable=Gheymat).place(x=100,y=340)
entMahsolname4=Entry(screen,font="Areal 15",textvariable=Tedad).place(x=100,y=400)'''

bgimage=PhotoImage(file="img/stake.png")
lblBG=Label(screen,text="*",image=bgimage).place(x=80,y=700)

bgimage1=PhotoImage(file="img/drink.png")
lblBG1=Label(screen,text="*",image=bgimage1).place(x=350,y=700)

bgimage2=PhotoImage(file="img/rise.png")
lblBG2=Label(screen,text="*",image=bgimage2).place(x=600,y=700)

bgimage3=PhotoImage(file="img/vegetables.png")
lblBG3=Label(screen,text="*",image=bgimage3).place(x=900,y=700)

bgimage4=PhotoImage(file="img/hobobat.png")
lblBG4=Label(screen,text="*",image=bgimage4).place(x=1200,y=700)

'''regbutton=Button(screen,text="S a b t",command=OnClickRegister,font="Areal 15",bg="#22e36c").place(x=200,y=450)

tbl=ttk.Treeview(screen,columns=("c1","c2","c3","c4"),show="headings",height=18)

tbl.column("# 4",anchor=S,width=70)
tbl.heading("# 4",text="name")

tbl.column("# 3",anchor=S,width=70)
tbl.heading("# 3",text="brand")

tbl.column("# 2",anchor=S,width=100)
tbl.heading("# 2",text="gheymat")

tbl.column("# 1",anchor=S,width=80)
tbl.heading("# 1",text="tedad")

tbl.bind("<Button-1>",GetSelction)


tbl.place(x=500,y=300)'''

def SabtFaktor(e):
    os.system(f"python msgs/msgFaktor.py")

UserAll=[]

def Register(User):
    if int(User["age"])>=1000:
        if Exist(User):
            messagebox.showerror("Error","Gheymat Kam Ast")
            return False
        else:
            UserAll.append(User)
            messagebox.showinfo("Done", "Ba Moafaghiat Sabt Shod")
            return True



    else:
        messagebox.showerror("eror","Gheymat Kam Ast")
        return False
def OnClickRegister():
    name = Name.get()
    family = Family.get()
    age = Phone_Number.get()
    address = Adress.get()
    us = {"name": name, "family": family, "age": age, "address": address}
    result=Register(us)
    if result==True:
        ListName=[Name,Family,Phone_Number,Adress]
        insertData(ListName)
        clear(ListName)
        txt1.focus_set()


def clear(listvar):
    for item in listvar:
        item.set("")

def insertData(value):
    tbl.insert('', "end", text="1", values=[value[3].get(), value[2].get(), value[1].get(), value[0].get()])

def GetSelction(e):
    selction_row=tbl.selection()

    if selction_row!= ():
        editbutton.place(x=405,y=450)
        ListName=[Name,Family,Phone_Number,Adress]
        clear(ListName)
        Name.set(tbl.item(selction_row)["values"][3])
        Family.set(tbl.item(selction_row)["values"][2])
        Phone_Number.set(tbl.item(selction_row)["values"][1])
        Adress.set(tbl.item(selction_row)["values"][0])

def OnClickSearch():
    query=txtSearch.get()
    result=Search(query)
    CleenTable()
    Load(result)


def Search(value):
    Listsec=[]
    for item in UserAll:
        if item["name"]==value or item["family"]==value or item["Phone_Number"]==value or item["address"]==value:
            Listsec.append(item)
    return Listsec

def Load(value):
    for item in value:
        tbl.insert('', "end", text="1", values=[item["address"], item["Phone_Number"], item["family"], item["name"]])

def CleenTable():
    for item in tbl.get_children():
        sel=(str(item),)
        tbl.delete(sel)

def Exist(Value):
    for item in UserAll:
        if Value["name"]==item["name"] and Value["family"]==item["family"] and Value["Phone_Number"]==item["Phone_Number"] and Value["address"]==item["address"]:
            return True
    return False

def OnClickDelte():
    result=messagebox.askquestion("Warning","Are you sure you want to delete the data?")
    if result=="yes":
        Delete()

def Delete():
    select_row=tbl.selection()
    print(select_row)
    if select_row!=():
        Selectitem=tbl.item(select_row)["values"]
        print(Selectitem)
        dic={'name':Selectitem[3],'family':Selectitem[2], 'age':Selectitem[1],'address':Selectitem[0]}
        tbl.delete(select_row)
        print(UserAll)
        UserAll.remove(dic)

def OnClickEdit():
    select_row = tbl.selection()
    Selectitem=tbl.item(select_row)["values"]
    dic = {'name': Selectitem[3], 'family': Selectitem[2], 'age': str(Selectitem[1]), 'address': Selectitem[0]}
    indexUs=UserAll.index(dic)
    print(indexUs)
    UserAll[indexUs]={'name': Name.get(),'family': Family.get(), 'age': str(Phone_Number.get()),'address': Adress.get() }
    if select_row!=():
        tbl.item(select_row,values=[Adress.get(),Phone_Number.get(),Family.get(),str(Name.get())])
        editbutton.place_forget()
        ListName = [Name, Family, Phone_Number, Adress]
        clear(ListName)

def exit_window():
    screen.destroy()


lbl1=Label(screen,text=":  Name").place(x=700,y=40)
lbl2=Label(screen,text=":  Brand").place(x=700,y=80)
lbl3=Label(screen,text=":  Gheymat").place(x=700,y=120)
lbl4=Label(screen,text=":  Tedad").place(x=700,y=160)

#alamat ha
'''
lbl6=Label(screen,text="*",font="Arial 50").place(x=1380,y=0)
lbl7=Label(screen,text="*",font="Arial 50").place(x=1380,y=40)
lbl8=Label(screen,text="*",font="Arial 50").place(x=1380,y=80)
lbl9=Label(screen,text="*",font="Arial 50").place(x=1380,y=120)
lbl10=Label(screen,text="*",font="Arial 50").place(x=1340,y=120)
lbl11=Label(screen,text="*",font="Arial 50").place(x=1300,y=120)
lbl12=Label(screen,text="*",font="Arial 50").place(x=1260,y=120)
lbl13=Label(screen,text="*",font="Arial 50").place(x=1220,y=120)
lbl14=Label(screen,text="*",font="Arial 50").place(x=1180,y=120)
lbl15=Label(screen,text="*",font="Arial 50").place(x=1140,y=120)
lbl16=Label(screen,text="*",font="Arial 50").place(x=1100,y=120)
lbl17=Label(screen,text="*",font="Arial 50").place(x=1060,y=0)
lbl18=Label(screen,text="*",font="Arial 50").place(x=1060,y=40)
lbl19=Label(screen,text="*",font="Arial 50").place(x=1060,y=80)
lbl20=Label(screen,text="*",font="Arial 50").place(x=1060,y=120)
lbl21=Label(screen,text="*",font="Arial 50").place(x=1100,y=0)
lbl22=Label(screen,text="*",font="Arial 50").place(x=1140,y=0)
lbl23=Label(screen,text="*",font="Arial 50").place(x=1180,y=0)
lbl24=Label(screen,text="*",font="Arial 50").place(x=1220,y=0)
lbl25=Label(screen,text="*",font="Arial 50").place(x=1260,y=0)
lbl26=Label(screen,text="*",font="Arial 50").place(x=1300,y=0)
lbl27=Label(screen,text="*",font="Arial 50").place(x=1340,y=0)

btngym=Button(screen,text="Kosar Shop",font="Arial 20")
btngym.configure(state=DISABLED)
btngym.place(x=1150,y=60)'''

#btnFaktor=Button(screen,text="Sabt Faktor",font="Arial 15",bg="#8cb6ff").place(x=662,y=200)
btnFaktor=Button(screen,text="Sabt Faktor")
btnFaktor.configure(bg="#761aed")
btnFaktor.bind("<Button-1>",SabtFaktor)
btnFaktor.place(x=662,y=200)

entmahsol=Label(screen,text="Sabt Mahsol",font="Arial 20").place(x=270,y=30)

Name=StringVar()
Family=StringVar()
Phone_Number=StringVar()
Adress=StringVar()

txt1=Entry(screen,textvariable=Name)
txt1.place(x=550,y=40)
txt2=Entry(screen,textvariable=Family).place(x=550,y=80)
txt3=Entry(screen,textvariable=Phone_Number).place(x=550,y=120)
txt4=Entry(screen,textvariable=Adress).place(x=550,y=160)

regbutton=Button(screen,text="S A B T",bg="#761aed",command=OnClickRegister).place(x=600,y=200)

btndelete=(Button(screen,text="Delete",bg="red",fg="white",command=OnClickDelte)).place(x=400,y=400)
lbldelete=Label(screen,text=": Delete",font="Arial 14").place(x=450,y=400)



tbl=ttk.Treeview(screen,columns=("c1","c2","c3","c4"),show="headings",height=14)

tbl.column("# 4",anchor=S,width=70)
tbl.heading("# 4",text="name")

tbl.column("# 3",anchor=S,width=70)
tbl.heading("# 3",text="brand")

tbl.column("# 2",anchor=S,width=100)
tbl.heading("# 2",text="gheymat")

tbl.column("# 1",anchor=S,width=80)
tbl.heading("# 1",text="tedad")

tbl.bind("<Button-1>",GetSelction)


tbl.place(x=200,y=80)

lblSearch=Label(screen,text=": Search place").place(x=140,y=10)
txtSearch=Entry(screen)
txtSearch.place(x=10,y=10)

btnSearch=Button(screen,text="Search",command=OnClickSearch).place(x=80,y=40)

editbutton=Button(screen,text="Edit",bg="#b7ff00",fg="black",command=OnClickEdit)
editbutton.pack_forget()
editdelete=Label(screen,text=": Edit",font="Arial 14").place(x=450,y=450)

closebtn=Button(screen,text="E x i t",bg="#761aed",font="Arial 18",command=exit_window)
closebtn.place(x=20,y=820)



screen.mainloop()