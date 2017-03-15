from tkinter import *

class mainOptions():
    def __init__(self,master):

        self.main_page = Frame(master,width=500, height=500)
        self.main_page.pack(fill=BOTH, expand=1)
        self.nInvoice = Button(self.main_page, text="New Invoice", command=self.newInvoice).pack()  # New Invoice Button = nInvoice
        self.sInvoice = Button(self.main_page, text="Search Invoices", command=self.searchInvoices).pack()  # Search Invoice Button = sInvoice
        self.main_page.pack_propagate(False)    #Set true for next page
    def newInvoice(self):
        self.main_page.pack_forget()
        print("new invoice")
        # Create invoice code
    def searchInvoices(self):
        self.main_page.pack_forget()
        print("search invoices")
        # Search existing invoice library

root = Tk()
mainOptions(root)
mainloop()
