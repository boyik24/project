from class_User import users
from class_Goods import goods
from class_Market import supermarket1
supermarket1.base=[goods]

def shop():
    print(f"--------{supermarket1.title}--------")
    phone_bool = True
    while True:
        while phone_bool:
            print("klient yoki admin telefon raqamini kiriting ")
            client_phone = input("Telefon raqami : ")
            for item in range(len(users)):
                if int(client_phone)==users[item].phone and int(client_phone)!=users[0]:
                    global num
                    num=item
                    phone_bool=False
        if num!=0:
            if len(supermarket1.history)!=0:
                if not users[num].name in supermarket1.history:
                    pass
                elif len(supermarket1.history[users[num].name])!=0:
                    client_debt=supermarket1.history[users[num].name].setdefault("debt",0)
                    if client_debt>0:
                        print("Sizning qarzingiz bor")
                        phone_bool=True
                        continue
            print("No  Mahsulot nomi  Narxi (so'm)  Ishlab chiqarilgan sana  Miqdori")
            for i in range(1,len(goods)):
                print(f"{i}".ljust(5),f"{goods[i].name}".ljust(15), f"{goods[i].cost}".ljust(16),
                      f"{(goods[i]).date[0]}.{goods[i].date[1]}.{goods[i].date[2]}".ljust(20),
                      f"{goods[i].count}")
            status=input("1. mahsulot sotib olish : \n2. orqaga qaytish : ")
            if status=="1":
                status_bool=True
                tot_cost = 0
                if len(supermarket1.history)==0:
                    purchase_num=0
                else:
                    if not users[num].name in supermarket1.history:
                        pass
                    elif len(supermarket1.history[users[num].name])==0:
                        purchase_num=0
                    else:
                        purchase_num=len(supermarket1.history[users[num].name])-2
                item_bool=True
                while status_bool:
                    if item_bool:
                        item=input("mahsulotning raqamini kiriting : ")
                    for i in range(len(goods)):
                        if i==int(item) and int(item)!=0:
                            count=input(f"qancha {goods[i].name} olmoqchisiz ({goods[i].cost}) : ")
                            cost_client=0
                            if int(count)<goods[i].count:
                                goods[i].count-=int(count)
                                tot_cost+=goods[i].cost*int(count)
                                cost_client+=goods[i].cost*int(count)
                                print(f"{count} ta {goods[i].name} olindi \njami narx : {tot_cost} so'm")
                                if int(count)!=0:
                                    purchase_num+=1
                                    users[num].karzinka[purchase_num]={
                                        "good":goods[i].name,
                                        "number of goods":int(count),
                                        "cost":cost_client
                                    }
                                    if len(supermarket1.history)==0:
                                        supermarket1.history[users[num].name]=users[num].karzinka
                                    elif not users[num].name in supermarket1.history:
                                        supermarket1.history[users[num].name] = users[num].karzinka
                                    else:
                                        (supermarket1.history[users[num].name]).update(users[num].karzinka)
                            else:
                                print(f"{count} ta {goods[i].name} yo'q")

                    item_bool=False
                    item=input("0.Savdoni tugatish :\n1-10.mahsulot sotib olish : ")
                    if item=="0":
                        prev_tot_cost=supermarket1.history[users[num].name].setdefault("total cost", 0)
                        supermarket1.history[users[num].name].pop("total cost")
                        supermarket1.history[users[num].name]["total cost"]=tot_cost+prev_tot_cost
                        print(f"Jami {tot_cost} so'm bo'ldi")
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
                                prev_debt=supermarket1.history[users[num].name].setdefault("debt",0)
                                supermarket1.history[users[num].name].pop("debt")
                                supermarket1.history[users[num].name]["debt"]=(tot_cost-cost)+prev_debt
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
                print("bunday amal bajarishni iloji yo'q")
                status_bool=True
        elif num==0:
            status_admin=input("1. Mahsulotlat ro'yxati :\n2. Kliyentlar tarixi : \n3. Orgaga : ")
            if status_admin=="1":
                print("No  Mahsulot nomi  Narxi (so'm)  Ishlab chiqarilgan sana  Miqdori")
                for i in range(1, len(goods)):
                    print(f"{i}".ljust(5), f"{goods[i].name}".ljust(15),f"{goods[i].cost}".ljust(16),
                          f"{(goods[i]).date[0]}.{goods[i].date[1]}.{goods[i].date[2]}".ljust(20),
                          f"{goods[i].count}")
            elif status_admin=="2":
                if len(supermarket1.history)!=0:
                    d=supermarket1.history
                    for client, data in d.items():
                        print(f"Kliyent ismi: {client}")
                        print("Mahsulot nomi".ljust(15), "Soni".ljust(7), "Narx (so'm)")
                        for key, details in data.items():
                            if isinstance(details, dict):
                                print(
                                    " ".ljust(3),
                                    str(details['good']).ljust(11),
                                    str(details["number of goods"]).ljust(7),
                                    str(details["cost"])
                                )
                        print(f"Jami : {data['total cost']} so'm")
                        print(f"Qarzi: {data['debt']} so'm\n")
                else:
                    print("\nSavdo amalga oshirilmagan\n")
            elif status_admin=="3":
                phone_bool=True
shop()