#!/users/bin/env python3
#coding:utf-8
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
	def __init__(self,master = None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self, text = 'Hello', command = self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message','Hello,%s' % name)

#在GUI中，每一个Button，Label，输入框等都是一个Widget。Frame
#则是可以容纳其他Widget的Widget，所有Widget组合起来就是树
app = Application()
app.master.title('Hello World')
app.mainloop()
  