class User:
    def __init__(self,name,is_admin,is_client,password):
        self.name=name
        self.is_admin =is_admin
        self.is_client =is_client
        self. karzinka=[]
        self.balans =10000
        self.password=password

user1=User("Ali",False,True,1111)
user2=User("Baxrom",False,True,1112)
user3=User("Said",False,True,1113)
user4=User("Diyor",False,True,1114)
admin=User("Ikromali",True,False,1115)