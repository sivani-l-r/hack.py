from tkinter import *
from random import randint

root = Tk()
root.title('Password Generator')
root.geometry('500x500')


# function for generting password
def new_pw():
	
	pw.delete(0, END)
	pw_length = int(pw_num.get())
	my_password = ''
	for x in range(pw_length):
		my_password += chr(randint(33,126))
	pw.insert(0, my_password)


# function for copying to clipboard
def clip_pw():
	root.clipboard_clear()
	root.clipboard_append(pw.get())

# Label  to prompt the user to enter the number of characters
lab1 = Label(root, text="Enter No of Characters:",font=('times',20))
lab1.pack()

# Entry Box to get the number of characters
pw_num= Entry(root,font=('',15))
pw_num.pack()


#button for generating password
pw_button = Button(root, text="GENERATE", command=new_pw,font=('',15))
pw_button.pack(padx=20)

#button for copying to clipboard
clip_button = Button(root, text="COPY", command=clip_pw,font=('',15))
clip_button.pack(padx=20)


lab2 = Label(root, text="The Password",font=('times',20))
lab2.pack()

# Entry Box for displaying the generated password
pw = Entry(root, text='', bd=0, bg="grey",font=('',15),)
pw.pack()

root.mainloop()
