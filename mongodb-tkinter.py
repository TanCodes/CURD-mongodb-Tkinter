#curd mongodb with tkinter

from tkinter import *
import tkinter.messagebox as MessageBox
import pymongo

###########database connection###############

client = pymongo.MongoClient(
            "mongodb+srv://demo:demo@cluster0.kll4c.mongodb.net/demoname?retryWrites=true&w=majority")
mydb = client['demoname']
mydbcol = mydb["democollection"]

######### window ############
root = Tk()
root.title("TanCodes")
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
w = 700
h= 500
x = int(ws/2-w/2)
y = int(hs/2-h/2)
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)


#--------------------function

#SHOW DATA
def show_data():
    x = mydbcol.find({},{'_id':0})
    for doc in x:
        print(doc)
        list1.insert(END,doc)
    client.close()

#CLEAR DATA
def clear_data():
    list1.delete(0, END)

#ADD DATA
def add_data():
    name = e1.get()
    mail = e2.get()
    error = '@gmail.com'
    if name == "" or mail == "":
        MessageBox.showerror("erro","All Fields required ")
    elif error not in mail:
        MessageBox.showerror("error", "invalid email")
    else:
        mydict = {"name": name,
                "mail": mail
                }

        x = mydbcol.insert_one(mydict)
        client.close()
        MessageBox.showinfo("good", 'Thank you')
        e1.delete(0, "end")
        e2.delete(0, "end")

#DELETE DATA
def del_data():
    mail = e2.get()
    error = '@gmail.com'
    if  mail == "":
        MessageBox.showerror("erro", "All Fields required ")
    elif error not  in mail:
        MessageBox.showerror("error","invalid email")
    else:
        mydbcol.delete_one({"mail": mail})
        client.close()
        MessageBox.showinfo("good", 'Thank you')
        e1.delete(0, "end")
        e2.delete(0, "end")
        list1.delete(0,"end")

####################################### new windwo for update #######################################################################

def update_data():
    import tkinter.messagebox as MessageBox
    import pymongo

    ###########data###############

    client = pymongo.MongoClient(
        "mongodb+srv://demo:demo@cluster0.kll4c.mongodb.net/demoname?retryWrites=true&w=majority")
    mydb = client['demoname']
    mydbcol = mydb["democollection"]

    #####################
    root = Tk()
    root.title("TanCodes")
    root.geometry("700x300")
    def final_update():
        currentemail = e1u.get()
        changeemail = e2u.get()
        error = '@gmail.com'
        if currentemail == "" or changeemail == "":
            MessageBox.showerror("erro", "All Fields required ")
        elif error not in currentemail or error not in changeemail:
            MessageBox.showerror("error", "invalid email")
        else:
            mydbcol.update_one(
                {"mail": currentemail},
                 {
                     "$set": {
                         "mail" : changeemail
                             }
                 }
            )
            # print("change email:" ,currentemail,"\n" "new email",changeemail)
            MessageBox.showinfo("good", 'updated successflly')
            e1u.delete(0, "end")
            e2u.delete(0, "end")



    email1u = Label(root, text="Enter email which u want to change with: ", font=("arial"))
    email1u.place(x=10, y=70)
    changeemail = Label(root, text="Enter new  email ", font=("arial"))
    changeemail.place(x=10, y=100)

    e1u = Entry(root, textvariable="s", width="30")
    e1u.place(x=350, y=70)

    e2u = Entry(root, textvariable="t", width="30")
    e2u.place(x=350, y=100)

    s = StringVar()
    t = StringVar()

    bu = Button(root, text="Update", fg = "white" ,bg="black",cursor="hand2", command=lambda: final_update())
    bu.place(x=300, y=130, width=70)

    root.configure(background="light blue")
    root.resizable(0, 0)
    root.mainloop()

####################################### END OF UPDATE FUNCTION######################################################################

######## NAME AND EMAIL #####################

titlelable = Label(root, text ="MongoDb CURD operations with Tkinter", font=("Helvetica",17, "bold"), fg="white", bg="black")
titlelable.place(x=130,y=2)

name = Label(root,text="Enter name: ",bg="papaya whip",font=("arial"))
name.place(x=10,y=50)

email1 = Label(root,text="Enter email: ",bg="papaya whip",font=("arial"))
email1.place(x=10,y=85)

###################### STRING ##################################

s = StringVar()
t = StringVar()

#################### ENTRY ####################################

e1 = Entry(root,textvariable="s")
e1.place(x=130,y=50,width=200, height=25)
e2 = Entry(root,textvariable="t")
e2.place(x=130,y=85,width=200, height=25)

####################### LIST ###############################

list1 = Listbox(root, font=("arial",15))
list1.place(x=10,y=170,height=200, width=670)


######################## BUTTON #############################

b1 = Button(root,text="Add",bg="yellow",cursor="hand2",command = lambda :add_data())
b1.place(x=100,y=130,width=70)

b2 = Button(root,text="Delete",bg="red",cursor="hand2",command = lambda :del_data())
b2.place(x=200,y=130,width=70)

notelab = Label(root,text="*After adding or deleting data first click clear shown data & then click the Show data ", bg="lightblue",font=("arial",9, "bold"))
notelab.place(x=10,y=380)

updatelab = Label(root,text="CLICK UPDATE BUTTON TO TAKE YOU TO THE NEW WINDOW TO UPDATE CURRENT MAIL WITH NEW EMAIL", font=("arial",10))
updatelab.place(x=10,y=420)

b3 = Button(root,text="Update",bg="steel blue",borderwidth=5,relief="ridge",cursor="hand2",command = lambda :update_data())
b3.place(x=300,y=450,width=70)

b4 = Button(root,text="Show data",bg="green",cursor="hand2",command = lambda :show_data())
b4.place(x=400,y=130,width=70)

b5 = Button(root,text="clear shown data",bg="grey",cursor="hand2",command = lambda :clear_data())
b5.place(x=500,y=130,width=100)

##################### END ###################################
root.configure(background="light blue")
root.resizable(0,0)
root.mainloop()
