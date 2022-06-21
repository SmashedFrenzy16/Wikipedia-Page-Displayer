import wikipedia
from tkinter import *

root = Tk()

root.title("Wikipedia Page Displayer")

entry1 = Entry(root, width=50, borderwidth=5)
entry1.grid(row=0, column=0)
entry1.insert(0, "What are you searching for?")

page = entry1.get()

contents = wikipedia.page(page).content

references = wikipedia.page(page).references

label1 = Label(root, text="Contents: ").grid(row=1, column=0)

label2 = Label(root, text=contents).grid(row=2, column=0)

label3 = Label(root, text="References: ").grid(row=3, column=0)

label4 = Label(root, text=references).grid(row=4, column=0)




root.mainloop()