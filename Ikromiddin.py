# def shop():
#     print(f"--------{supermarket1.title}--------")
#     phone_bool = True
#     while True:
#         while phone_bool:
#             print("klient yoki admin telefon raqamini kiriting ")
#             client_phone = input("Telefon raqami : ")
#             for item in range(len(users)):
#                 if int(client_phone) == users[item].phone and int(client_phone) != users[0]:
#                     global num
#                     num = item
#                     phone_bool = False
#         if num != 0:
#             if len(supermarket1.history) != 0:
#                 if not users[num].name in supermarket1.history:
#                     pass
#                 elif len(supermarket1.history[users[num].name]) != 0:
#                     client_debt = supermarket1.history[users[num].name].setdefault("debt", 0)
#                     if client_debt > 0:
#                         print("Sizning qarzingiz bor")
#                         phone_bool = True
#                         continue
#             print("No  Mahsulot nomi  Narxi (so'm)  Ishlab chiqarilgan sana  Miqdori")
#             for i in range(1, len(goods)):
#                 print(f"{i}".ljust(5), f"{goods[i].name}".ljust(15), f"{goods[i].cost}".ljust(16),
#                       f"{(goods[i]).date[0]}.{goods[i].date[1]}.{goods[i].date[2]}".ljust(20),
#                       f"{goods[i].count}")
#             status = input("1. mahsulot sotib olish : \n2. orqaga qaytish : ")
#             if status == "1":
#                 status_bool = True
#                 tot_cost = 0
#                 if len(supermarket1.history) == 0:
#                     purchase_num = 0
#                 else:
#                     if not users[num].name in supermarket1.history:
#                         pass
#                     elif len(supermarket1.history[users[num].name]) == 0:
#                         purchase_num = 0
#                     else:
#                         purchase_num = len(supermarket1.history[users[num].name]) - 2
#                 item_bool = True
#                 while status_bool:
#                     if item_bool:
#                         item = input("mahsulotning raqamini kiriting : ")
#                     for i in range(len(goods)):
#                         if i == int(item) and int(item) != 0:
#                             count = input(f"qancha {goods[i].name} olmoqchisiz ({goods[i].cost}) : ")
#                             cost_client = 0
#                             if int(count) < goods[i].count:
#                                 goods[i].count -= int(count)
#                                 tot_cost += goods[i].cost * int(count)
#                                 cost_client += goods[i].cost * int(count)
#                                 print(f"{count} ta {goods[i].name} olindi \njami narx : {tot_cost} so'm")
#                                 if int(count) != 0:
#                                     purchase_num += 1
#                                     users[num].karzinka[purchase_num] = {
#                                         "good": goods[i].name,
#                                         "number of goods": int(count),
#                                         "cost": cost_client
#                                     }
#                                     if len(supermarket1.history) == 0:
#                                         supermarket1.history[users[num].name] = users[num].karzinka
#                                     elif not users[num].name in supermarket1.history:
#                                         supermarket1.history[users[num].name] = users[num].karzinka
#                                     else:
#                                         (supermarket1.history[users[num].name]).update(users[num].karzinka)
#                             else:
#                                 print(f"{count} ta {goods[i].name} yo'q")
