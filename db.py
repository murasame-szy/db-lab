from pymysql import *
from  datetime  import  *
import time

def conn():
    conn = connect(host = 'localhost', user = 'root', password = '123456', db = 'bm', port = 3306, charset = 'utf8')
    cur = conn.cursor()
    return cur

def search(bookname):
    cur = conn()
    cur.execute("select * from 图书信息 where 书名=%s",(bookname))
    results = cur.fetchall()
    return results

def searchall():
    cur = conn()
    sql = 'select * from 图书信息'
    cur.execute(sql)
    results = cur.fetchall()
    return results

def searchbuylist():
    cur = conn()
    sql = 'select * from 采购'
    cur.execute(sql)
    results = cur.fetchall()
    return results

def searchabandonlist():
    cur = conn()
    sql = 'select * from 淘汰'
    cur.execute(sql)
    results = cur.fetchall()
    return results

def searchleft(no):
    cur = conn()
    cur.execute("select 书名,数量 from 图书信息 where 书号=%s",(no))
    results = cur.fetchall()
    return results

def searchrent():
    cur = conn()
    sql = 'select * from 租借'
    cur.execute(sql)
    results = cur.fetchall()
    return results

def rent(no):
    cur = conn()
    cur.execute(("select 书名,书号,数量,归还情况 from 租借 where 书号=%s"),(no))
    results = cur.fetchall()
    return results

def getallno():
    cur = conn()
    sql = 'select 书号 from 图书信息'
    cur.execute(sql)
    results = cur.fetchall()
    return results

def InsertIntoBuylist(bn, bno, ba, bd, bq, bp):
    conn = connect(host='localhost', user='root', password='123456', db='bm', port=3306, charset='utf8')
    cur = conn.cursor()
    tm = time.strftime("%d/%m/%Y %H:%M")
    cur.execute("insert into 采购(name, no, au, dept, date, quantity, price) values ( '%s', '%s', '%s', '%s', '%s', '%s', '%s');" %(bn, bno, ba, bd, tm, bq, bp))
    conn.commit()

def searchbyno(no):
    cur = conn()
    cur.execute("select * from 图书信息 where 书号=%s",(no))
    results = cur.fetchall()
    return results

def updateinfo(no,bq):
    conn = connect(host='localhost', user='root', password='123456', db='bm', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute("update 图书信息 set 数量=数量+%s where 书号=%s", (bq, no))
    conn.commit()

def upadatenew(bn, bno, ba, bd, bq):
    conn = connect(host='localhost', user='root', password='123456', db='bm', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute("insert into 图书信息(书名, 书号, 作者, 出版社, 数量) values('%s', '%s', '%s', '%s', '%s');" %(bn, bno, ba, bd, bq))
    conn.commit()

def searchname(bno):
    cur = conn()
    cur.execute(("select 书名,数量 from 图书信息 where 书号=%s"),(bno))
    results = cur.fetchall()
    return results

def InsertAbandonList(bn, bno, bq):
    tm = time.strftime("%d/%m/%Y %H:%M")
    conn = connect(host='localhost', user='root', password='123456', db='bm', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute("insert into 淘汰(书名,书号,数量,淘汰时间) values('%s', '%s', '%s', '%s');" %(bn, bno, bq, tm))
    conn.commit()

def UpdateInfoAbandon(bno, bq):
    conn = connect(host='localhost', user='root', password='123456', db='bm', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute("update 图书信息 set 数量=数量-%s where 书号=%s", (bq, bno))
    conn.commit()

def InsertRentList(bn, bno, bq):
    tm1 = time.strftime("%d/%m/%Y %H:%M")
    now = date.today()
    tomorrow = now.replace(day=7)
    delta = tomorrow - now
    tm2 = now + delta * 7
    conn = connect(host='localhost', user='root', password='123456', db='bm', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute("insert into 租借(书名,书号,数量,借出时间,预期归还时间,实际归还时间,归还情况) values('%s', '%s', '%s', '%s', '%s', NULL, '否');" %(bn, bno, bq, tm1, tm2))
    conn.commit()
    return tm1

def BookGiveback(bno, tm):
    conn = connect(host='localhost', user='root', password='123456', db='bm', port=3306, charset='utf8')
    cur = conn.cursor()
    now = date.today()
    cur.execute("update 租借 set 实际归还时间=%s,归还情况='是'where 书号=%s and 借出时间=%s;", (str(now), bno, tm))
    cur.execute("select 数量 from 租借 where 书号=%s and 借出时间=%s" ,(bno, tm))
    results = cur.fetchall()
    count = results[0]
    cur.execute("update 图书信息 set 数量=数量+%s",(count[0]))
    conn.commit()

def DeleteByNo(no):
    conn = connect(host='localhost', user='root', password='123456', db='bm', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute("delete from 图书信息 where 书号=%s", (no))
    conn.commit()

def GivebackCheck(no, tm):
    cur = conn()
    cur.execute("select 归还情况 from 租借 where 书号=%s and 借出时间=%s;" ,(no, tm))
    results = cur.fetchall()
    return results