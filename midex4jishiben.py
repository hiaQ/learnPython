#!/user/bin/env python
#coding:utf-8

from Tkinter import *
import os      #导入模块

#创建日记本文件夹
def initDiary():
	dir = os.getcwd()                  #获取当前的.py文件目录
	list = os.listdir(dir)             #获取当前目录中的所有文件
	haveDiary = False                  #设置一个变量，是否存在Diary文件夹，默认为False
	for item in list:                  #遍历  
		if item == 'diary':            #判断是否存在diary文件夹
			haveDiary = True           #如果有，设置haveDiary为True
	if haveDiary == False:              #如果遍历完之后，仍然没有diary文件
		os.mkdir("diary")              #创建diary文件夹

	os.chdir("./diary")               #改变.py工作目录到diary下

#写日记
def write():
	textVar.set("")    #清空entry（清空字符串变量的内容）
	text.delete("0.0","end")   #清空text（清空写日记窗口内的内容）
	label.config(text = '写日记模式')    #config表示label的内容
	listBox.pack_forget()      #隐藏ListBox
	entry.pack()               #显示entry
	text.pack()                #显示text

#保存日记
def save():
	title = textVar.get()+".txt"    #获取标题
	content = text.get("0.0","end") #获取内容
	if title != ".txt":
		fileobj = open(title,"wb")   #打开一个文件
		fileobj.write(content);      #写入内容
		fileobj.close()  
		label.config(text = "已保存")
	else:
		label.config(text = "请输入标题")

#看日记
def read():
	listBox.delete(0,END)   #清空listBox
	dir = os.getcwd()
	list = os.listdir(dir)
	showText = "看日记模式"
	if len(list) ==0:
		showText+="(日记本是空的)"
	label.config(text = showText)
	for item in list:
		listBox.insert(0,item)
	listBox.bind('<Double-Button-1>',showDiary)   #双击绑定事件
	entry.pack_forget()
	text.pack_forget()
	listBox.pack()

#showDiary函数
def showDiary(event):
	title = listBox.get(listBox.curselection())
	showTitle = title[:-4]     #？？？？
	textVar.set(showTitle)

	fileobj = open(title,"r+")
	content = fileobj.read();
	text.delete(0.0,"end")
	text.insert("end",content)
	fileobj.close()

	listBox.pack_forget()
	entry.pack()
	text.pack()

initDiary()

root = Tk() #创建窗口
root.geometry('500x400')  #控制窗口的大小
root.title('日记本')   #定义窗口的标题

savebtn = Button(root,text = "保存",command = save)
savebtn.pack(side = LEFT, anchor = 'sw')

quitbtn = Button(root,text = "退出",command = quit)
quitbtn.pack(side = RIGHT, anchor = 'se')

writebtn = Button(root,text = '写日记',command = write)
writebtn.pack(side = BOTTOM)

readbtn = Button(root,text = "读日记",command = read)
readbtn.pack(side = BOTTOM)

label = Label(root)
label.pack()
label.config(text = "这是一个演示程序")

textVar = StringVar()  #StringVar()是一个字符串变量类型
entry = Entry(root, textvariable = textVar)    #textvariable表示文本框中的内容
text = Text(root)

listBox = Listbox(root,height = '300')

root.mainloop()    #显示窗口代码

