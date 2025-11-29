class account:
    def __init__(self, number, name, sold=0):
        self.__number=number
        self.__name=name
        self.__sold=sold

    def afficher(self):
        print(f"Number : {self.__number}\t Name :  {self.__name}\t Sold : {self.__sold} euros")

    def getNumber(self):
        return self.__number
    def getName(self):
        return self.__name
    def getSold(self):
        return self.__sold
    def setSold(self, new):
        self.__sold=new
    def deposit(self, amount=None):
        if amount is None:
            amount = float(input("Enter amount to deposit: "))
        self.__sold += amount
    def retire (self, amount):
        if self.__sold >= amount:
            self.__sold -= amount
            print(f"Withdrew {amount}. New balance: {self.__sold} euros")
    def __str__(self):
        return f"{self.__number}\t {self.__name}\t {self.__sold} euros"
    def __str__(self):
        print(f"{self.__number}\t {self.__name}\t {self.__sold} euros")

client = account(10, "Ali", 5000)
print("------------------------------")
client.afficher()
print("------------------------------")
client.deposit()
print("------------------------------")
client.retire(float(input("Enter amount to withdraw: ")))
print("------------------------------")
print(client.__str__())
