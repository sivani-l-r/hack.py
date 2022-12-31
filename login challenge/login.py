from tkinter import*
from tkinter import messagebox




class login_interface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.security()

    def security(self):
        self.master.title("LOGIN")
        self.pack(fill=BOTH, expand=1)
        userlbl=Label(self,text="Username").grid(column=0,row=0)
        lbl = Label(self, text="PASSWORD").grid(column=0, row=1)
        self.userlbl=Entry(self)
        self.userlbl.focus_set()
        self.pwrd = Entry(self, show="*")
        self.pwrd.focus_set()
        self.userlbl.grid(column=1, row=0)
        self.pwrd.grid(column=1, row=1)
        login = Button(self, text="LOGIN", width=20, command=self.login)
        login.grid(column=1, row=2)
    
    
    
    
    def login(self):

        """
        file=open('passwords.txt','r')
        d={}
        for line in file:
            x=line.split(",")
            a=x[0]
            b=x[1]
            c=len(b)-1
            b=b[0:c]
            d[a]=b
        val=self.userlbl.get()
        print(val in d)

        """
        if ( (self.pwrd.get() == "123456") and (self.userlbl.get()=="sivani") ):
            messagebox.showinfo("Successfull! ", "Login Successful!")
        elif self.pwrd.get() != "123456":
            messagebox.showinfo("ERROR ", "The password entered is incorrect!")
        else :
            messagebox.showinfo("ERROR ", "The username entered is incorrect!")
        

            
a = Tk()
a.geometry("300x100")
app = login_interface(a)
app.mainloop()