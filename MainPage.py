from tkinter import *
from view import *

class MainPage(object):
    def __init__(self, master = None):
        self.root = master
        self.root.geometry('600x500')
        self.createPage()

    def createPage(self):
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.buyPage = BuyFrame(self.root)
        self.abandonPage = AbandonFrame(self.root)
        self.rentPage = RentFrame(self.root)
        self.queryPage.pack()
        menubar = Menu(self.root)
        menubar.add_command(label = '查询', command = self.toquery)
        menubar.add_command(label = '统计', command = self.tocount)
        menubar.add_command(label = '采购', command = self.tobuy)
        menubar.add_command(label = '淘汰', command = self.toabandon)
        menubar.add_command(label = '租借', command = self.torent)
        self.root['menu'] = menubar

    def toquery(self):
        self.queryPage.pack()
        self.countPage.pack_forget()
        self.buyPage.pack_forget()
        self.abandonPage.pack_forget()
        self.rentPage.pack_forget()

    def tocount(self):
        self.queryPage.pack_forget()
        self.countPage.pack()
        self.buyPage.pack_forget()
        self.abandonPage.pack_forget()
        self.rentPage.pack_forget()

    def tobuy(self):
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.buyPage.pack()
        self.abandonPage.pack_forget()
        self.rentPage.pack_forget()

    def toabandon(self):
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.buyPage.pack_forget()
        self.abandonPage.pack()
        self.rentPage.pack_forget()

    def torent(self):
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.buyPage.pack_forget()
        self.abandonPage.pack_forget()
        self.rentPage.pack()