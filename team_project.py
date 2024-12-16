from class_User import users
from class_Goods import goods
from class_Market import supermarket1


def Shop():
    print("Mahsulot nomi  Narxi (so'm)  ")
    for item in goods:
        print(item.name)