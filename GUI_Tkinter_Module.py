from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        
        self.master = master
        self.master.minsize(470,170) 
        self.master.maxsize(470,170)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
       

        self.btnBrowse1 = Button(self.master, text="Browse", width=12, font=("Helvetica",12), fg='black')
        self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(10,0))
        
        self.btnBrowse2 = Button(self.master, text="Browse", width=12, font=("Helvetica",12), fg='black')
        self.btnBrowse2.grid(row=1, column=0, padx=(20,0), pady=(5,0))

        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2,font=("Helvetica",12), fg='black')
        self.btnCheck.grid(row=2, column=0, padx=(20,0), pady=(5,0))

        self.txtBrowse1 = Entry(self.master, width=20, font=("Helvetica",20), fg='black',bg='white')
        self.txtBrowse1.grid(row=0, column=1, padx=(10,0), pady=(10,0))
      
        self.txtBrowse2 = Entry(self.master, width=20, font=("Helvetica",20), fg='black',bg='white')
        self.txtBrowse2.grid(row=1, column=1,  padx=(10,0), pady=(5,0))

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2,font=("Helvetica",12), fg='black')
        self.btnClose.grid(row=2, column=1, padx=(0,0), pady=(5,0), sticky=E)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
