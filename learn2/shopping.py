#-*-coding: utf-8 -*-

'''
如果商品列表定义为列表：
for index,item in enumerate(product_list):
    print(index,item)
'''

shop = {1:['iphone',5000],2:['mac_pro',12000],3:['book',105],4:['bick',2500],5:['htc',6000]}
cart = []

salary = input('Pleans input your salary :')
if salary.isdigit():
    salary = int(salary)

while  salary > 0:
    for k,v in shop.items():
        num = k
        name = v[0]
        price = v[1]
        if salary > price:
            print(num,name,price)
    choose = input("Please choose goods or 'q' quit :")

    if choose == "q":
        print(cart)
        print("salary: \033[31;1m%d\033[0m" %(salary))
        break
    else:
        if choose.isdigit():
            choose = int(choose)
        if choose > len(shop) or choose < 0:
            print('Input error,try again!')
            continue
        cart.append(shop[choose])

        salary -= cart[len(cart)-1][1]
        print("salary: \033[31;1m%d\033[0m" %(salary))
        continue

