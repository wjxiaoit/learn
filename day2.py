#-*-coding: utf-8 -*-
import pymysql
import time

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

count = 0
err_count = 0
while count < 4:
    if err_count > 3:
        print("Account is locked,Please contact administrator!")
        break
    print("Welcome Login in !")
    name=input("UserName:")
    lock_key = user_lock(name)
    if lock_key == 1:
        print("User is locked! Please contact administrator!")
        break
    user_key = user_exists(name)
    if user_key == 1:
        passwd = input("Password: ")
        (s_user,s_passwd) = get_user(name)
        if s_user == name and passwd == s_passwd:
            print("Login sussce!")
            break
        else:
            print("Username or password error!")
            err_count += 1
            break
    else:
        print("UserName not exists,Please try again!")
        count += 1
        continue
