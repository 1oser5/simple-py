#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_tkinter.py
@Time    :   2019/01/04 13:36:22
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        # self.hello()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text= 'Hello', command = self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello.%s'%name)      
app = Application()
#设置标题窗口
app.master.title('Hello, world')
#主信息循环
app.mainloop()


