from tkinter import*
import tkinter.messagebox
import backend

class Library:

    def __init__(self, root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="Cadet Blue")

        mtype=StringVar()
        idc=StringVar()
        title=StringVar()
        firstname=StringVar()
        lastname=StringVar()
        bookid=StringVar()
        booktitle=StringVar()
        bookauthor=StringVar()
        dateborrow=StringVar()
        datedue=StringVar()
        latefine=StringVar()
        dateoverdue=StringVar()

        #================================Functions===========================
        def iExit():
            iExit=tkinter.messagebox.askyesno("Library DBMS", "Do you really want to exit?")
            if (iExit>0):
                root.destroy()
                return

        def cleardata():
            self.txtmtype.delete(0, END)
            self.txtidc.delete(0, END)
            self.txttitle.delete(0, END)
            self.txtfirstname.delete(0, END)
            self.txtlastname.delete(0, END)
            self.txtbookid.delete(0, END)
            self.txtbooktitle.delete(0, END)
            self.txtbookauthor.delete(0, END)
            self.txtdateborrow.delete(0, END)
            self.txtdatedue.delete(0, END)
            self.txtlatefine.delete(0, END)
            self.txtdateoverdue.delete(0, END)

        def adddata():
            if (len(mtype.get())!=0):
                backend.adddatarec(mtype.get(), idc.get(), title.get(), firstname.get(), lastname.get(), bookid.get(), booktitle.get(), bookauthor.get(), dateborrow.get(), datedue.get(), latefine.get(), dateoverdue.get())

                booklist.delete(0, END)
                booklist.insert(END, (mtype.get(), idc.get(), title.get(), firstname.get(), lastname.get(), bookid.get(), booktitle.get(), bookauthor.get(), dateborrow.get(), datedue.get(), latefine.get(), dateoverdue.get()))

        def displaydata():
            booklist.delete(0, END)
            for row in backend.viewdata():
                booklist.insert(END, row)

        def selectedbook(event):
            global sb
            searchbook=booklist.curselection()[0]
            sb=booklist.get(searchbook)

            self.txtmtype.delete(0, END)
            self.txtmtype.insert(END, sb[1])
            self.txtidc.delete(0, END)
            self.txtidc.insert(END, sb[2])
            self.txttitle.delete(0, END)
            self.txttitle.insert(END, sb[3])
            self.txtfirstname.delete(0, END)
            self.txtfirstname.insert(END, sb[4])
            self.txtlastname.delete(0, END)
            self.txtlastname.insert(END, sb[5])
            self.txtbookid.delete(0, END)
            self.txtbookid.insert(END, sb[6])
            self.txtbooktitle.delete(0, END)
            self.txtbooktitle.insert(END, sb[7])
            self.txtbookauthor.delete(0, END)
            self.txtbookauthor.insert(END, sb[8])
            self.txtdateborrow.delete(0, END)
            self.txtdateborrow.insert(END, sb[9])
            self.txtdatedue.delete(0, END)
            self.txtdatedue.insert(END, sb[10])
            self.txtlatefine.delete(0, END)
            self.txtlatefine.insert(END, sb[11])
            self.txtdateoverdue.delete(0, END)
            self.txtdateoverdue.insert(END, sb[12])

        def deletedata():
            if (len(mtype.get())!=0):
                backend.deleterec(sb[0])
                cleardata()
                displaydata()

        def update():
            if (len(mtype.get())!=0):
                backend.dataupdate(sb[0], mtype.get(), idc.get(), title.get(), firstname.get(), lastname.get(), bookid.get(), booktitle,get(), bookauthor.get(), dateborrow.get(), datedue.get(), latefine.get(), dateoverdue.get())

        
        #==================================Frames===================================
        MainFrame=Frame(self.root)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame, bd=2, padx=40, pady=8, bg="Cadet Blue", relief=SUNKEN)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame, font=('arial', 46, 'bold'), text="Library Management System")
        self.lblTitle.grid(sticky=W)

        ButtonFrame=Frame(MainFrame, bd=2, width=1050, height=100, padx=20, pady=20, bg="Cadet Blue", relief=SUNKEN)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail=Frame(MainFrame, bd=0, width=1050, height=50, padx=20, relief=SUNKEN)
        FrameDetail.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame, bd=1, width=1000, height=400, padx=20, pady=20, relief=SUNKEN)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft=LabelFrame(DataFrame, bd=1, width=800, height=300, padx=20, relief=SUNKEN, font=('arial', 12, 'bold'), text="Library Membership Info:", bg="Cadet Blue")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight=LabelFrame(DataFrame, bd=1, width=450, height=300, padx=20, pady=3, relief=SUNKEN, font=('arial', 12, 'bold'), bg="Cadet Blue", text="Details:")
        DataFrameRight.pack(side=RIGHT)

        #===============================Label and Entry==================================
        self.lblmtype=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Member Type", padx=2, pady=2, bg="Cadet Blue")
        self.lblmtype.grid(row=0, column=0, sticky=W)
        self.txtmtype=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=mtype, width=20)
        self.txtmtype.grid(row=0, column=1)

        self.lblbookid=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Book ID:", padx=2, pady=2, bg="Cadet Blue")
        self.lblbookid.grid(row=0, column=2, sticky=W)
        self.txtbookid=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=bookid, width=20)
        self.txtbookid.grid(row=0, column=3)

        self.lblidc=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="PRN/ID No.:", padx=2, pady=2, bg="Cadet Blue")
        self.lblidc.grid(row=1, column=0, sticky=W)
        self.txtidc=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=idc, width=20)
        self.txtidc.grid(row=1, column=1)

        self.lblbooktitle=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Book Title:", padx=2, pady=2, bg="Cadet Blue")
        self.lblbooktitle.grid(row=1, column=2, sticky=W)
        self.txtbooktitle=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=booktitle, width=20)
        self.txtbooktitle.grid(row=1, column=3)

        self.lbltitle=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Title:", padx=2, pady=2, bg="Cadet Blue")
        self.lbltitle.grid(row=2, column=0, sticky=W)
        self.txttitle=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=title, width=20)
        self.txttitle.grid(row=2, column=1)

        self.lblbookauthor=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Author:", padx=2, pady=2, bg="Cadet Blue")
        self.lblbookauthor.grid(row=2, column=2, sticky=W)
        self.txtbookauthor=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=bookauthor, width=20)
        self.txtbookauthor.grid(row=2, column=3)

        self.lblfirstname=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="First Name:", padx=2, pady=2, bg="Cadet Blue")
        self.lblfirstname.grid(row=3, column=0, sticky=W)
        self.txtfirstname=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=firstname, width=20)
        self.txtfirstname.grid(row=3, column=1)

        self.lbldateborrow=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Date Borrowed:", padx=2, pady=2, bg="Cadet Blue")
        self.lbldateborrow.grid(row=3, column=2, sticky=W)
        self.txtdateborrow=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=dateborrow, width=20)
        self.txtdateborrow.grid(row=3, column=3)

        self.lbllastname=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Last Name:", padx=2, pady=2, bg="Cadet Blue")
        self.lbllastname.grid(row=4, column=0, sticky=W)
        self.txtlastname=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=lastname, width=20)
        self.txtlastname.grid(row=4, column=1)

        self.lbldatedue=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Date Due:", padx=2, pady=2, bg="Cadet Blue")
        self.lbldatedue.grid(row=4, column=2, sticky=W)
        self.txtdatedue=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=datedue, width=20)
        self.txtdatedue.grid(row=4, column=3)

        self.lbllatefine=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Late Return Fine:", padx=2, pady=2, bg="Cadet Blue")
        self.lbllatefine.grid(row=5, column=0, sticky=W)
        self.txtlatefine=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=latefine, width=20)
        self.txtlatefine.grid(row=5, column=1)

        self.lbldateoverdue=Label(DataFrameLeft, font=('arial', 12, 'bold'), text="Date Over Due:", padx=2, pady=2, bg="Cadet Blue")
        self.lbldateoverdue.grid(row=5, column=2, sticky=W)
        self.txtdateoverdue=Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=dateoverdue, width=20)
        self.txtdateoverdue.grid(row=5, column=3)

        #================================Listbox and Scrollbar===========================
        scrollbar=Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')

        booklist=Listbox(DataFrameRight, width=45, height=12, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>', selectedbook)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=booklist.yview)

        #====================Buttons===============================
        self.btnadddata=Button(ButtonFrame, text='Add Data', font=('arial', 12, 'bold'), height=2, width=10, bd=4, command=adddata)
        self.btnadddata.grid(row=0, column=0)

        self.btndisplaydata=Button(ButtonFrame, text='Display Data', font=('arial', 12, 'bold'), height=2, width=10, bd=4, command=displaydata)
        self.btndisplaydata.grid(row=0, column=1)

        self.btncleardata=Button(ButtonFrame, text='Clear Data', font=('arial', 12, 'bold'), height=2, width=10, bd=4, command=cleardata)
        self.btncleardata.grid(row=0, column=2)

        self.btndeletedata=Button(ButtonFrame, text='Delete Data', font=('arial', 12, 'bold'), height=2, width=10, bd=4, command=deletedata)
        self.btndeletedata.grid(row=0, column=3)

        self.btnupdatedata=Button(ButtonFrame, text='Update Data', font=('arial', 12, 'bold'), height=2, width=10, bd=4, command=update)
        self.btnupdatedata.grid(row=0, column=4)

        self.btnexit=Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'), height=2, width=10, bd=4, command=iExit)
        self.btnexit.grid(row=0, column=5)
        
if __name__=='__main__':
    root=Tk()
    application=Library(root)
    root.mainloop()
