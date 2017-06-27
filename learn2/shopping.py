#-*-coding: utf-8 -*-



shop = {1:['iphone',5000],2:['mac_pro',12000],3:['book',105],4:['bick',2500],5:['htc',6000]}
cart = []

salary = int(input('Pleans input your salary :'))
while  salary > 0:
    for k,v in shop.items():
        num = k
        name = v[0]
        price = v[1]
        if salary > price:
            print(num,name,price)
    chooes = input("Please chooes goods or 'q' quit :")
    if chooes == "q":
        print(cart)
        print("salary: %d" %(salary))
        break
    else:
        cart.append(shop[int(chooes)])
        salary -= cart[len(cart)-1][1]
        print("salary: %d" %(salary))
        continue

