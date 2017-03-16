from tkinter import *

class mainOptions():
    def __init__(self,master):
        self.main_page = Frame(master,width=750, height=500, background="white")
        self.main_page.pack(fill=BOTH, expand=1)
        self.option_frame = Frame(self.main_page, background="white")
        self.option_frame.place(relx=0.5, rely=0.5 , anchor="c")
        self.nInvoice = Button(self.option_frame, text="New Invoice", command=self.newInvoice).pack(side=LEFT)  # New Invoice Button = nInvoice
        self.sInvoice = Button(self.option_frame, text="Search Invoices", command=self.searchInvoices).pack(side=LEFT)  # Search Invoice Button = sInvoice
        self.main_page.pack_propagate(False)    #Set true for next page, if not  appropriated
    def newInvoice(self):
        self.main_page.pack_forget()
        print("new invoice")
        # Create invoice code
    def searchInvoices(self):
        self.main_page.pack_forget()
        print("search invoices")
        # Search existing invoice library

class invoiceTemplate():
    def doSomething(self):
        self.print = print("do something")
    #formating template information, to create invoice

root = Tk()
mainOptions(root)
mainloop()
