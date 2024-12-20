class User:
    def __init__(self,name,is_admin,is_client,password,phone):
        self.phone=phone
        self.name=name
        self.is_admin =is_admin
        self.is_client =is_client
        self.karzinka={}
        self.balans=151000
        self.password=password

user1=User("Ali",False,True,1111,971112233)
user2=User("Baxrom",False,True,1112,971192233)
user3=User("Said",False,True,1113,971132233)
user4=User("Diyor",False,True,1114,971142233)
admin=User("Ikromali",True,False,1115,971152233)

users=[admin,user1,user2,user3,user4]
