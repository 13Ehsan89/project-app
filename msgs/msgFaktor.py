import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from msgMahsol import

screen=Tk()

screen.title("Sabt Faktor")
screen.geometry("%dx%d+%d+%d" % (1440,900,-10,0))
screen.iconbitmap("img/SabtMahsol.ico")
screen.resizable(False,False)

bgimage1=PhotoImage(file="img/bbg1.png")


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
    frmSearch.place(x=0,y=0)
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
        editbutton.place(x=100,y=700)
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

def CloseFaktor():
    frmSearch.place_forget()

def exit_window():
    screen.destroy()



frmSearch=Frame(screen,width=380,height=900,bg="#8324ff")
frmSearch.place(x=0,y=0)
frmSearch.place_forget()
lblBG=Label(frmSearch,text="*",image=bgimage1,width=1440,height=900).place(x=0,y=0)

lbl1=Label(screen,text=":  Name Moshtari",font="Areal 26").place(x=800,y=150)
lbl2=Label(screen,text=":  Name Kala",font="Areal 26").place(x=800,y=250)
lbl3=Label(screen,text=":  Gheymat",font="Areal 26").place(x=800,y=350)
lbl4=Label(screen,text=":  Tarikh",font="Areal 26").place(x=800,y=450)

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


entmahsol=Label(screen,text="Sabt Faktor",font="Arial 20").place(x=650,y=30)

Name=StringVar()
Family=StringVar()
Phone_Number=StringVar()
Adress=StringVar()

txt1=Entry(screen,textvariable=Name,font="Arial 18")
txt1.place(x=500,y=160)
txt2=Entry(screen,textvariable=Family,font="Arial 18").place(x=500,y=260)
txt3=Entry(screen,textvariable=Phone_Number,font="Arial 18").place(x=500,y=360)
txt4=Entry(screen,textvariable=Adress,font="Arial 18").place(x=500,y=460)

regbutton=Button(screen,text="Sabt Faktor",bg="#761aed",command=OnClickRegister,font="Arial 18").place(x=600,y=600)

btndelete=(Button(frmSearch,text="Delete",bg="red",fg="white",command=OnClickDelte)).place(x=100,y=650)
lbldelete=Label(frmSearch,text=": Delete",font="Arial 16").place(x=150,y=650)



tbl=ttk.Treeview(frmSearch,columns=("c1","c2","c3","c4"),show="headings",height=26)

tbl.column("# 4",anchor=S,width=90)
tbl.heading("# 4",text="Name Moshtari")

tbl.column("# 3",anchor=S,width=85)
tbl.heading("# 3",text="Name Kala")

tbl.column("# 2",anchor=S,width=60)
tbl.heading("# 2",text="Gheymat")

tbl.column("# 1",anchor=S,width=60)
tbl.heading("# 1",text="Tarikh")

tbl.bind("<Button-1>",GetSelction)


tbl.place(x=20,y=80)

lblSearch=Label(frmSearch,text=": Search place").place(x=140,y=10)
txtSearch=Entry(frmSearch)
txtSearch.place(x=10,y=10)

btnSearch=Button(frmSearch,text="Search",command=OnClickSearch).place(x=80,y=40)

editbutton=Button(frmSearch,text="Edit",bg="#b7ff00",fg="black",command=OnClickEdit)
editbutton.pack_forget()
editdelete=Label(frmSearch,text=": Edit",font="Arial 14").place(x=150,y=700)

closeSearch=Button(frmSearch,text="close",command=CloseFaktor).place(x=300,y=10)

closebtn=Button(screen,text="E x i t",bg="#761aed",font="Arial 18",command=exit_window)
closebtn.place(x=30,y=800)

tavajohlbl=Label(screen,text="Tavajoh : Gheymat Ha Be Reyal Ast",font="Arial 14").place(x=495,y=320)

screen.mainloop()