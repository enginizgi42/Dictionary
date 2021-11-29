
from tkinter import *
import backend

def getSelectedRow(event):
	global selected_tuple
	index = list1.curselection()[0]
	selected_tuple = list1.get(index)
	e1.delete(0, END)
	e1.insert(END, selected_tuple[1])
	e2.delete(0, END)
	e2.insert(END, selected_tuple[2])

def clean():
        e1.delete(0, END)
        e2.delete(0, END)



        
        
def viewCommand():
	list1.delete(0, END)
	for row in backend.view():
		list1.insert(END, row)
def searchCommand():
	list1.delete(0, END)
	for row in backend.search(ing_text.get(), tr_text.get()):
		list1.insert(END, row)
	clean()

def addCommand():
	backend.insert(ing_text.get(), tr_text.get() )
	list1.delete(0, END)
	list1.insert(END, (ing_text.get()+ ":", tr_text.get()) )
	
	clean()

def deleteCommand():
	backend.delete(selected_tuple[0])
	viewCommand();

def updateCommand():
	backend.update(selected_tuple[0], ing_text.get(), tr_text.get())
	viewCommand();

window = Tk()
window.geometry("550x300")
window.wm_title("Dictionary")
window.attributes("-topmost", True)

#Text ings
l1 = Label(window, text="İngilizce")
l1.grid(row = 0, column = 0)
l2 = Label(window, text="Türkçe")
l2.grid(row = 0, column = 2)

#Entry
ing_text = StringVar()
e1 = Entry(window, textvariable=ing_text)
e1.grid(row = 0, column = 1)
tr_text = StringVar()
e2 = Entry(window, textvariable=tr_text)
e2.grid(row = 0, column = 3)




list1 = Listbox(window, height = 16, width = 65)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)


#Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', getSelectedRow)

##Buttons
b1 = Button(window, text="View All", width=12, command = viewCommand)
b1.grid(row = 2, column = 3)
b2 = Button(window, text="Search Entry", width=12, command = searchCommand)
b2.grid(row = 3, column = 3)
b3 = Button(window, text="Add Entry", width=12, command = addCommand)
b3.grid(row = 4, column = 3)
b4 = Button(window, text="Update Selected", width=12, command = updateCommand)
b4.grid(row = 5, column = 3)
b5 = Button(window, text="Deleted Selected", width=12, command = deleteCommand)
b5.grid(row = 6, column = 3)
b6 = Button(window, text="Close", width=12, command = window.destroy)
b6.grid(row = 7, column = 3)
window.mainloop()
