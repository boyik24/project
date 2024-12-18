from class_User import users
from class_Goods import goods
from class_Market import supermarket1
supermarket1.base=[goods]

# client uchun tegishli qismini tugatdim,
# faqat karzinkaga sotib olingan narsalar ro'yxatini qo'shish kerak (37 qatorda qo'shiladi)
# admin uchun tegishli qism qoldi (74 qator)
# karzinka ni dictionary qilsa ham bo'lrkan, shunda klass shart emas ekan

def shop():
    print(f"--------{supermarket1.title}--------")
    phone_bool = True
    while True:
        while phone_bool:
            client_phone = input("Kliyentning telefon raqami : ")
            for item in range(len(users)):
                if int(client_phone)==users[item].phone and int(client_phone)!=users[0]:
                    global num
                    num=item  # new_client olmasdan shu n ni keyinchalk kliyent ning list dagi raqmidan ishlatiladi
                    phone_bool=False
        if num!=0:
            print("No  Mahsulot nomi  Narxi (so'm)  Muddati")
            for i in range(1,len(goods)):
                print(f"{i}".ljust(3),f"{goods[i].name}".ljust(14), f"{goods[i].cost}".ljust(13),f"{(goods[i]).date[0]}.{goods[i].date[1]}.{goods[i].date[2]}")
            status=input("1. mahsulot sotib olish : \n2. orqaga qaytish : ")
            if status=="1":
                status_bool=True
                tot_cost = 0
                purchase_num = 0
                while status_bool:
                    item=input("mahsulotning raqamini kiriting : ")
                    for i in range(len(goods)):
                        if i==int(item) and int(item)!=0:
                            count=input(f"qancha {goods[i].name} olmoqchisiz : ")
                            cost_client=0
                            if int(count)<goods[i].count:
                                goods[i].count-=int(count)
                                tot_cost+=goods[i].cost*int(count)
                                cost_client+=goods[i].cost*int(count)
                                print(f"{count} ta {goods[i].name} olindi -{tot_cost} so'm")
                                if int(count)!=0:
                                    purchase_num+=1
                                    users[num].karzinka[purchase_num]={
                                        "good":goods[i].name,
                                        "number of goods":int(count),
                                        "cost":cost_client,
                                    }
                                    if len(supermarket1.history)==0:
                                        supermarket1.history[users[num].name]=users[num].karzinka
                                    else:
                                        (supermarket1.history[users[num].name]).update(users[num].karzinka)
                            else:
                                print(f"{count} ta {goods[i].name} yo'q")
                    status2=input("1. Savdoni tugatish : ")
                    if status2=="1":
                        supermarket1.history[users[num].name]["total cost"]=tot_cost
                        print(f"Jami {tot_cost} so'm pul bo'ldi")
                        cost=tot_cost
                        card_code_bool=True
                        card_count=0
                        while card_code_bool:
                            card_code = input("kartani kodini kiriting : ")
                            if users[num].password==int(card_code):
                                if tot_cost>users[num].balans:
                                    cost=users[num].balans
                                supermarket1.balance+=cost
                                users[num].balans-=cost
                                print(f"{tot_cost} so'm pul yechib olindi")
                                supermarket1.history[users[num].name]["debt"]=tot_cost-cost
                                if not tot_cost==cost:
                                    print(f"{tot_cost-cost} so'm qarz bo'ldiz")
                                status_bool=False
                                phone_bool=True
                                break
                            else:
                                print("kod xato")
                                card_count+=1
                            if card_count==3:
                                print("karta bloklandi")
                                card_code_bool=False
                                status_bool = False
                                phone_bool = True
                                break
            elif status == "2":
                phone_bool = True
            else:
                phone_bool = False
        elif num==0:
            status_admin=input("1. ro'yxat :\n2. kliyentlar tarixi : \n3. Orgaga")
            if status_admin=="1":
                print("No  Mahsulot nomi  Narxi (so'm)  Muddati")
                for i in range(1, len(goods)):
                    print(f"{i}".ljust(3), f"{goods[i].name}".ljust(14), f"{goods[i].cost}".ljust(13),
                          f"{(goods[i]).date[0]}.{goods[i].date[1]}.{goods[i].date[2]}")
            elif status_admin=="2":
                print("Kliyent ismi  Mahsulot nomi  Soni  Narx  Qarz")
                if len(supermarket1.history)!=0:
                    for item in supermarket1.history:
                        print(item,item["good"],item["number of goods"],item["cost"],item["debt"])
                else:
                    print("savdo amalga oshirilmagan")





shop()
