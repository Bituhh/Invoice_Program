from tkinter import *

root = Tk()

main_page = Frame(width=750, height=500, bd=5, relief=SUNKEN)
nInvoice = Button(main_page, text="New Invoice").pack() #New Invoice Button = nInvoice
# nInvoice.grid(row=0, column=0)
sInvoice = Button(main_page, text="Search Invoices").pack() #Search Invoice Button = sInvoice
# sInvoice.grid(row=0, column=1)
main_page.pack(fill=BOTH, expand=1)

mainloop()