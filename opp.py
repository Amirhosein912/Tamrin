class Person:
    name = ""
    family = ""
    def __init__ (self,name,family, age):
        self.name = name
        self.family = family
        self.__age = age
    
    def getAge (self):
        return self.__age
    

class Child(Person):
    pass

class User(Person):
    activeuser = 0

    def __init__ (self, username, password, name, family, age):
        self.__username = username
        self.__password = password
        super().__init__(name, family, age)
        User.activeuser += 1
        print(f"{self.__username} is login")


    def logout(self):
        User.activeuser -= 1
        print(f"{self.__username} is logout")

    @classmethod
    def getActiveUser(cls):
        print(f"{cls.activeuser}")

    def __repr__(self):
        return f"{self.__username} {super().getAge()}"
    
amirUser = User("amir2","123456", "amir", "solimani", 24)

alirezaUser = User("alipc","54321", "ali", "mortzavi", 26)

print(amirUser.name)
print(alirezaUser.family)
print(User.activeuser)
amirUser.logout()
print(User.activeuser)
User.getActiveUser()

print(amirUser)