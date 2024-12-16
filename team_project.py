from class_User import users
from class_Goods import goods
from class_Market import supermarket1


def Shop():
    # client=input()
    print("No  Mahsulot nomi  Narxi (so'm)  Muddati")
    for i in range(1,len(goods)):
        print(f"{i}".ljust(3),f"{goods[i].name}".ljust(14), f"{goods[i].cost}".ljust(13),f"{(goods[i]).date[0]}.{goods[i].date[1]}.{goods[i].date[2]}")
Shop()
