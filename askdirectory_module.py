from tkinter import*
import tkinter as tk
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        def searchDirectory():
            dir_file=filedialog.askdirectory(parent=root, initialdir = '/',title = 'Select A Folder')
            if dir_file:
                self.txt_folderP.insert(INSERT,dir_file)


        self.master = master
        self.master.minsize(500,275)
        self.master.maxsize(500,275)
        self.master.title("Search Directory")

        self.folder_Path = Label(self.master, text="Folder Path:",fg='#000')
        self.folder_Path.pack()

        self.txt_folderP = Text(self.master, height=2, fg='#000', bg='white')
        self.txt_folderP.pack()
        self.search_btn = Button(self.master, text='SEARCH', width=10, height=2,command=searchDirectory)
        self.search_btn.pack()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
