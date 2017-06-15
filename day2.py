#-*-coding: utf-8 -*-
import pymysql
from datetime import datetime

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

def user_lock(name):
    sql = "select count(*) from lock_user where user='%s'"%(name)
    key = select(sql)[0][0]
    return key

def get_user(name):
    sql = "select user,password from user where user = '%s'"%(name)
    username,passwd = select(sql)[0]
    return (username,passwd)

def re_time():
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return dt

def lock_user(name):
    lt = re_time()
    sql = "insert into lock_user(user,datetime) values('%s','%s')"%(name,lt)
    insert(sql)


count = 0
err_count = 0

while True:
    if err_count == 3:
        lock_user(name)
        print("%s is lock,not use!"%(name))
        break
    print("Welcome!")
    name = input("UserName: ")
    lock_key = user_lock(name)
    if lock_key == 1:
        print("User is locked!")
        break
    user_key = user_exists(name)
    if user_key == 0:
        print("User not exists!")
        break
    passwd = input("Password: ")
    (s_user, s_passwd) = get_user(name)
    if name == s_user and passwd == s_passwd:
        print("Login sussce!")
        break
    else:
        print("Username or password error!")
        err_count += 1
        continue