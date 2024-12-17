from class_User import users, user1
from class_Goods import goods, good1, good2, good3, good4, good10, good5, good6, good7, good8, good9
from class_Market import supermarket1
from class_Karzinka import karzinkalar, karzinka1


def Shop():
    while True:
        client_phone=input("Kliyentning telefon raqami : ")
        for client in users:
            if int(client_phone)==client.phone:
                new_client=client
        print("No  Mahsulot nomi  Narxi (so'm)  Muddati")
        for i in range(1,len(goods)):
            print(f"{i}".ljust(3),f"{goods[i].name}".ljust(14), f"{goods[i].cost}".ljust(13),f"{(goods[i]).date[0]}.{goods[i].date[1]}.{goods[i].date[2]}")

        offer=input("1.xarid amalga oshirmoqchimisiz 2.chiqish")
        if offer=="1":
            status=input("qanday mahsulotni xarid qilmoqchisiz:")
            if status=="saryoq":
                status2=input("nechchi pachka:")
                new_client.karzinka+=f"{status2}ta {status}= {sum(good1.cost*status2)}"
            elif status=="gosht":
                status3=input("nechchi kilo sotib olmoqchisiz:")
                new_client.karzinka += f"{status3}kilo {status}= {sum(good2.cost * status3)}"
            elif status=="tuxum":
                status4=input("nechchi dona sotib olmoqchisiz:")
                new_client.karzinka += f"{status4}dona {status}= {sum(good3.cost * status4)}"
            elif status=="moy":
                status5=input("nechchi litr sotib olmoqchisiz:")
                new_client.karzinka += f"{status5}kilo {status}= {sum(good4.cost * status5)}"
            elif status=="pomidor":
                status6=input("nechchi kilo sotib olmoqchisiz:")
                new_client.karzinka += f"{status6}kilo {status}= {sum(good5.cost * status6)}"
            elif status=="bodring":
                status7=input("nechchi kilo sotib olmoqchisiz:")
                new_client.karzinka += f"{status7}kilo {status}= {sum(good6.cost * status7)}"
            elif status=="olma":
                status8=input("nechchi kilo sotib olmoqchisiz:")
                new_client.karzinka += f"{status8}kilo {status}= {sum(good7.cost * status8)}"
            elif status=="suv":
                status9=input("nechchi litr sotib olmoqchisiz:")
                new_client.karzinka += f"{status9}kilo {status}= {sum(good8.cost * status9)}"
            elif status=="choy":
                status10=input("nechchi kilo sotib olmoqchisiz:")
                new_client.karzinka += f"{status10}kilo {status}= {sum(good9.cost * status10)}"
            elif status=="shokolad":
                status11=input("nechchi pachka sotib olmoqchisiz:")
                new_client.karzinka += f"{status11}kilo {status}= {sum(good10.cost * status11)}"
        else:
            print("salomat buling")
            break