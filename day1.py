#-*-coding: utf-8 -*-

'''
简单实现用户注册功能；
1、输入用户进行注册；
2、在数据库里查询用户名是否已经被注册，如果已经注册，需要重新输入；
3、输入数据库里没有的用户名后，将用户名和密码写入数据库；
'''
import pymysql

def select(sql):
    conn = pymysql.connect(user='root', passwd='admin', host='192.168.174.129', db='learn')
    cur = conn.cursor()
    cur.execute(sql)
    values=cur.fetchall()
    cur.close()
    conn.close()
    return values

def insert(sql):
    conn = pymysql.connect(user='root', passwd='admin', host='192.168.174.129', db='learn')
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    cur.close()
    conn.close()

def user_exists(name):
    sql = "select count(*) from user where user='%s'"%(name)
    key = select(sql)[0][0]
    return key

if __name__ == "__main__":
    print("Welcome regster,please input your infomation.")
    while True:
        name = input("UserName:")
        aa = user_exists(name)
        if aa == 1:
            print("ERROR, UserName is exists,pleas change a UserName.")
            continue
        passwd = input("Password:")
        sql = "insert into user(user,password) values('%s','%s')"%(name,passwd)
        insert(sql)
        print("Regster Succeed !")
        exit()