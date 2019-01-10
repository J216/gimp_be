#!/usr/bin/python3

import sys
import os
import re
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):
    tags = []
    meta = {}
    template = ""
    replace = []
    E1 = []
    L1 = []

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("JSI - JReplace Template")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Open", command=self.openFile)
        file.add_command(label="Save", command=self.saveFile)
        file.add_command(label="Exit", command=self.space_rats)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Clear", command=self.clearWindow)

        #added "file" to our menu
        menu.add_cascade(label="View", menu=edit)
        self.showImg()

        clearButton = Button(self, text="Clear",command=self.clearWindow)
        # placing the button on my window
        clearButton.place(x=375, y=560)
        quitButton = Button(self, text="Quit",command=self.space_rats)
        # placing the button on my window
        quitButton.place(x=435, y=560)

    def drawEntry(self):
        tag_count = 0
        for tag in self.tags:
            self.L1.append( Label(self, text=tag))
            self.L1[tag_count].place(x=0, y=tag_count*28)
            self.E1.append(Entry(self, bd =5))
            self.E1[tag_count].place(x=128, y=tag_count*28)
            tag_count += 1

    def showImg(self):
        load = Image.open("jsi-logo-256.png")
        render = ImageTk.PhotoImage(load)
        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=240, y=300)

    def openFile(self):
        self.filename =  filedialog.askopenfilename(initialdir = "~/scripts/",title = "Select file",filetypes = (("ini files","*.ini"),("all files","*.*")))
        self.loadTemplate()
        self.drawEntry()

    def saveFile(self):
        self.filename =  filedialog.asksaveasfilename(initialdir = "~/scripts/",title = "Select file",filetypes = (("ini files","*.ini"),("all files","*.*")))
        for t in self.E1:
            self.replace.append(t.get())
        self.replaceTags()
        with open(self.filename, "w") as f:
            f.write(self.template)

    def clearWindow(self):
        for i in range(len(self.E1)):
            self.E1[i].destroy()
            self.L1[i].destroy()
        self.E1 = []
        self.L1 = []
        self.tags = []
        self.meta = {}
        self.template = ""
        self.replace = []

    def loadTemplate(self):
        if os.path.isfile(self.filename):
            # Read tags and create set
            with open(self.filename) as file:
                self.template = file.read()
            file_tags=re.findall(re.escape('<')+"(.*)"+re.escape('>'),self.template)
            for i in file_tags:
                if ':' in i:
                    self.meta[i.split(':')[0]] = i.split(':')[1]
                    self.template = template.replace('<'+i+'>','')
                else:
                    if not i in self.tags:
                        self.tags.append(i)

    def replaceTags(self):
        tag_count = 0
        for t in self.tags:
            self.template=self.template.replace("<"+t+">", self.replace[tag_count])
            tag_count += 1
        print(self.tags)
        print(self.replace)
        print(self.template)

    #Quit button function
    def space_rats(self):
        exit()

root = Tk()

#size of the window
root.geometry("500x600")

app = Window(root)
root.mainloop() 
