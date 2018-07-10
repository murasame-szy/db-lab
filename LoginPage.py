from tkinter import *
from tkinter.messagebox import *
from MainPage import *

class LoginPage(object):
    def __init__(self,master = None):
        self.root = master
        self.root.geometry('300x200')
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page).grid(row = 0, stick= W)
        Label(self.page, text= '账户: ').grid(row = 1, stick = W, pady = 10)
        Entry(self.page, textvariable = self.username).grid(row = 1, column = 1, stick = E)
        Label(self.page, text = '密码: ').grid(row = 2, stick = W, pady = 10)
        Entry(self.page, textvariable = self.password, show = '*').grid(row = 2, column = 1, stick = E)
        Button(self.page, text = '登陆', command = self.loginCheck).grid(row = 3, stick = W, pady = 10)
        Button(self.page, text = '退出', command = self.page.quit).grid(row = 3, column = 1, stick = E)

    def loginCheck(self):
        name = self.username.get()
        passwd = self.password.get()
        if name == 'root' and passwd == '123456':
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title = '错误', message = '用户名或密码错误')