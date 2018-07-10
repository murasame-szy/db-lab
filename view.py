from tkinter import *
from tkinter.messagebox import *
import db

class QueryFrame(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.root = master
        self.bookname = StringVar()
        self.bookno = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid()
        Label(self, text = '图书信息（请输入书名）').grid()
        Entry(self, textvariable = self.bookname).grid()
        Button(self, text = '查询', command = self.querybook).grid()
        Label(self).grid()
        Label(self, text = '采购清单').grid()
        Button(self, text = '查询', command = self.new_window1).grid()
        Label(self).grid()
        Label(self, text = '淘汰清单').grid()
        Button(self, text = '查询', command = self.new_window2).grid()
        Label(self).grid()
        Label(self, text = '库存（请输入书号）').grid()
        Entry(self, textvariable = self.bookno).grid()
        Button(self, text = '查询', command = self.left).grid()
        Label(self).grid()
        Label(self, text = '租借清单').grid()
        Button(self,text = '查询', command = self.new_window3).grid()

    #查询图书信息弹出窗口
    def querybook(self):
        na = self.bookname.get()
        a = db.search(na)
        if a == ():
            showinfo(title = '查询结果', message = '无结果！')
        else:
            results = a[0]
            msg = '书号：'+results[1]+'  作者: '+results[2]+'  出版社: '+results[3]
            showinfo(title = '查询结果', message = msg)

    #查询采购清单显示的界面
    def new_window1(self):
        window1 = Toplevel(self)
        results1 = db.searchbuylist()
        List1 = ['书名', '书号', '作者', '出版社', '日期', '数量', '价格']
        i = 0
        for pro1 in List1:
            Label(window1, text = pro1).grid(row = 1, column = i)
            i = i + 1
        # Label(window).grid(row = 0)
        # Label(window, text = '书名').grid(row = 1, column = 0)
        # Label(window, text = '书号').grid(row = 1, column = 1)
        # Label(window, text = '作者').grid(row = 1, column = 2)
        # Label(window, text = '出版社').grid(row = 1, column = 3)
        # Label(window, text = '日期').grid(row = 1, column = 4)
        # Label(window, text = '数量').grid(row = 1, column = 5)
        # Label(window, text = '价格').grid(row = 1, column = 6)
        j = 2
        for res1 in results1:
            i = 0
            while(i < 7):
                Label(window1, text = res1[i]).grid(row = j, column = i)
                i= i + 1
            j = j + 1

    #查询淘汰清单显示界面
    def new_window2(self):
        window2 = Toplevel(self)
        results2 = db.searchabandonlist()
        List2 = ['书名', '书号', '数量', '淘汰时间']
        i = 0
        for pro2 in List2:
            Label(window2, text = pro2).grid(row = 1, column = i)
            i = i + 1
        j = 2
        for res2 in results2:
            i = 0
            while(i < 4):
                Label(window2, text = res2[i]).grid(row = j, column = i)
                i = i + 1
            j = j + 1

    #查询库存弹出窗口
    def left(self):
        no = self.bookno.get()
        a = db.searchleft(no)
        if a == ():
            showinfo(title = '查询结果', message = '无结果！')
        else:
            results = a[0]
            msg = '书号: ' + no + '   书名: ' + results[0] + '   库存: ' + str(results[1])
            showinfo(title = '查询结果', message = msg)

    #查询租借清单显示窗口
    def new_window3(self):
        window3 = Toplevel()
        results3 = db.searchrent()
        List3 = ['书名', '书号', '数量', '借出时间', '预期归还时间', '实际归还时间', '归还情况']
        i = 0
        for pro3 in List3:
            Label(window3,text = pro3).grid(row = 1, column =i)
            i = i + 1
        j = 2
        for res3 in results3:
            i = 0
            while(i < 7):
                Label(window3, text = res3[i]).grid(row = j, column = i)
                i = i + 1
            j = j + 1





class CountFrame(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.root = master
        self.createPage()

    def createPage(self):
        Label(self).grid()
        Button(self, text = '采购统计', command = self.countbuy).grid()
        Label(self).grid()
        Button(self, text = '库存统计', command = self.countleft).grid()
        Label(self).grid()
        Button(self, text = '淘汰统计', command = self.countabandon).grid()
        Label(self).grid()
        Button(self, text = '租借情况统计', command = self.countrent).grid()

    def countbuy(self):
        window = Toplevel()
        results = db.searchbuylist()
        List = ['书名', '书号', '单价', '数量', '该书总价']
        i = 0
        for pro in List:
            Label(window, text = pro).grid(row = 1, column = i)
            i = i + 1
        j = 2
        totalprice = 0
        totalcount = 0
        for pro in results:
            Label(window, text = pro[0]).grid(row = j, column = 0)
            Label(window, text = pro[1]).grid(row = j, column = 1)
            Label(window, text = pro[6]).grid(row = j, column = 2)
            Label(window, text = pro[5]).grid(row = j, column = 3)
            Label(window, text = pro[5]*pro[6]).grid(row = j, column = 4)
            totalprice = totalprice + pro[5]*pro[6]
            totalcount = totalcount + pro[5]
            j = j + 1
        msg1 = '总价格为' + str(totalprice)
        msg2 = '总数量为' + str(totalcount)
        Label(window).grid(row = j)
        Label(window, text = msg1).grid(row = j + 1)
        Label(window, text = msg2).grid(row = j + 2)

    def countleft(self):
        window = Toplevel()
        results = db.searchall()
        List = ['书名', '书号', '库存']
        i = 0
        for pro in List:
            Label(window, text = pro).grid(row = 0, column = i)
            i = i + 1
        j = 1
        totalleft = 0
        for res in results:
            Label(window, text = res[0]).grid(row = j, column = 0)
            Label(window, text = res[1]).grid(row = j, column = 1)
            Label(window, text = res[4]).grid(row = j, column = 2)
            totalleft = totalleft + res[4]
            j = j + 1
        Label(window).grid(row = j)
        msg = '总库存为' + str(totalleft)
        Label(window, text = msg).grid(row = j + 1)

    def countabandon(self):
        window = Toplevel()
        results = db.searchabandonlist()
        List = ['书名', '书号', '数量']
        i = 0
        for pro in List:
            Label(window, text = pro).grid(row = 0, column = i)
            i = i + 1
        j = 1
        totalcount = 0
        for res in results:
            Label(window, text = res[0]).grid(row = j, column = 0)
            Label(window, text = res[1]).grid(row = j, column = 1)
            Label(window, text = res[2]).grid(row = j, column = 2)
            totalcount = totalcount + res[2]
            j = j + 1
        Label(window).grid(row = j)
        msg = '总废弃数量为' + str(totalcount)
        Label(window, text = msg).grid(row = j + 1)

    def countrent(self):
        window = Toplevel()
        results = db.searchrent()
        List = ['书名', '书号', '借出数量', '是否归还']
        i = 0
        for pro in List:
            Label(window, text = pro).grid(row = 0, column = i)
            i = i + 1
        j = 1
        totalcount = 0
        for res in results:
            Label(window, text = res[0]).grid(row = j, column = 0)
            Label(window, text = res[1]).grid(row = j, column = 1)
            Label(window, text = res[2]).grid(row = j, column = 2)
            Label(window, text = res[6]).grid(row = j ,column = 3)
            if res[6] == '否':
                totalcount =  totalcount + res[2]
            j = j + 1
        Label(window).grid(row = j)
        msg1 = '总借出数量为' + str(totalcount)
        Label(window, text = msg1).grid(row = j + 1)
        Label(window).grid()
        Label(window, text = '详细统计').grid()
        NoList = db.getallno()
        for no in NoList:
            a = db.rent(no)
            if a != ():
                count = 0
                for res in a:
                    if res[3] == '否':
                        count = count + res[2]
                msg2 = no[0] + '  ' + str(count)
                Label(window, text = msg2).grid()





class BuyFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.bno1 = StringVar()
        self.bq1 = StringVar()
        self.bp1 = StringVar()
        self.bno2 = StringVar()
        self.bn2 = StringVar()
        self.ba2 = StringVar()
        self.bd2 = StringVar()
        self.bp2 = StringVar()
        self.bq2 = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row = 0)
        Label(self, text = '已有图书采购').grid(row = 1, column = 1)
        Label(self, text = '书号').grid(row = 2, column = 0)
        Entry(self, textvariable = self.bno1).grid(row = 2, column = 1)
        Label(self, text = '数量').grid(row = 3, column = 0)
        Entry(self, textvariable = self.bq1).grid(row = 3, column = 1)
        Label(self, text = '单价').grid(row = 4, column = 0)
        Entry(self, textvariable = self.bp1).grid(row = 4, column = 1)
        Button(self, text = '采购', command = self.buy1).grid(row = 5, column = 1)
        Label(self).grid(row = 6)
        Label(self, text = '新图书采购').grid(row = 7, column = 1)
        Label(self, text = '书号').grid(row = 8, column = 0)
        Entry(self, textvariable = self.bno2).grid(row = 8, column = 1)
        Label(self, text = '书名').grid(row = 9, column = 0)
        Entry(self, textvariable = self.bn2).grid(row = 9, column = 1)
        Label(self, text = '作者').grid(row = 10, column = 0)
        Entry(self, textvariable = self.ba2).grid(row = 10, column = 1)
        Label(self, text = '出版社').grid(row = 11, column = 0)
        Entry(self, textvariable = self.bd2).grid(row = 11, column = 1)
        Label(self, text = '数量').grid(row = 12, column = 0)
        Entry(self, textvariable = self.bq2).grid(row = 12, column = 1)
        Label(self, text = '单价').grid(row = 13, column = 0)
        Entry(self, textvariable = self.bp2).grid(row = 13, column = 1)
        Button(self, text = '采购', command = self.buy2).grid(row = 14, column =1)

    def buy1(self):
        bno = self.bno1.get()
        bq = self.bq1.get()
        bp = self.bp1.get()
        results = db.searchbyno(bno)
        if results == ():
            showinfo(title = '错误', message = '该图书不存在')
        else:
            results = results[0]
            bn = results[0]
            ba = results[2]
            bd = results[3]
            db.InsertIntoBuylist(bn, bno, ba ,bd, bq, bp)
            db.updateinfo(bno, bq)
            showinfo(title = '结果', message = '采购成功！')

    def buy2(self):
        bno = self.bno2.get()
        bn = self.bn2.get()
        ba = self.ba2.get()
        bd = self.bd2.get()
        bq = self.bq2.get()
        bp = self.bp2.get()
        db.InsertIntoBuylist(bn, bno, ba, bd, bq, bp)
        db.upadatenew(bn, bno, ba, bd, bq)
        showinfo(title = '结果', message = '采购成功！')





class AbandonFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.bno = StringVar()
        self.bq = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row = 0)
        Label(self, text = '书号').grid(row = 1, column = 0)
        Entry(self, textvariable = self.bno).grid(row = 1, column = 1)
        Label(self, text = '数量').grid(row = 2, column = 0)
        Entry(self, textvariable = self.bq).grid(row = 2, column = 1)
        Button(self, text = '淘汰', command = self.abandonbook).grid(row = 3, column = 1)

    def abandonbook(self):
        no = self.bno.get()
        quantity = self.bq.get()
        results = db.searchname(no)
        if results == ():
            showinfo(title = '错误', message = '图书不存在')
        else:
            results = results[0]
            if results[1] < int(quantity):
                showinfo(title = '错误', message = '数量不足')
            else:
                db.InsertAbandonList(results[0], no, quantity)
                db.UpdateInfoAbandon(no, quantity)
                leftcount = db.searchleft(no)
                leftcount = leftcount[0]
                if leftcount[1] == 0:
                    db.DeleteByNo(no)
                showinfo(title = '成功', message = '淘汰成功')





class RentFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.bno = StringVar()
        self.bq = StringVar()
        self.bno2 = StringVar()
        self.tm = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row = 0)
        Label(self, text = '租借').grid(row = 1, column = 1)
        Label(self, text = '书号').grid(row = 2, column = 0)
        Entry(self, textvariable = self.bno).grid(row = 2, column = 1)
        Label(self, text = '数量').grid(row = 3, column = 0)
        Entry(self, textvariable = self.bq).grid(row = 3, column = 1)
        Button(self, text = '租借', command = self.rent).grid(row = 4, column = 1)
        Label(self).grid(row = 5)
        Label(self, text = '归还').grid(row = 6, column = 1)
        Label(self, text = '书号').grid(row = 7, column = 0)
        Entry(self, textvariable = self.bno2).grid(row = 7, column = 1)
        Label(self, text = '借出时间').grid(row = 8, column = 0)
        Entry(self, textvariable = self.tm).grid(row = 8, column = 1)
        Button(self, text = '归还', command = self.giveback).grid(row = 9 ,column = 1)

    def rent(self):
        no = self.bno.get()
        quantity = self.bq.get()
        results = db.searchname(no)
        if results == ():
            showinfo(title = '错误', message = '该图书不存在')
        else:
            results = results[0]
            if results[1] < int(quantity):
                showinfo(title = '失败', message = '库存不足')
            else:
                tm = db.InsertRentList(results[0], no, quantity)
                db.UpdateInfoAbandon(no, quantity)
                msg = '租借成功，时间为' + tm +'，归还时需提供时间'
                showinfo(title = '成功', message = msg)

    def giveback(self):
        no = self.bno2.get()
        time = self.tm.get()
        results = db.GivebackCheck(no, time)
        results = results[0]
        if results[0] == '是':
            showinfo(title = '错误', message = '该书已归还')
        else:
            db.BookGiveback(no, time)
            showinfo(title = '成功', message = '归还成功')