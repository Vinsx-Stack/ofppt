class Bank: 
    def __init__(self, code, number, name, lastname, sold):
        self.__code = code
        self.__number = number
        self.__name = name
        self.__lastname = lastname
        self.__sold = sold

    # Getters and setters
    def get_code(self): return self.__code
    def set_code(self, new): self.__code = new

    def get_number(self): return self.__number
    def set_number(self, new): self.__number = new 

    def get_name(self): return self.__name
    def set_name(self, new): self.__name = new

    def get_lastname(self): return self.__lastname
    def set_lastname(self, new): self.__lastname = new

    def get_sold(self): return self.__sold
    def set_sold(self, new): self.__sold = new

    # Display method
    def afficher(self):
        print(f"Code : {self.__code}")
        print(f"Number : {self.__number}")
        print(f"Name : {self.__name}")
        print(f"Last Name : {self.__lastname}")
        print(f"Sold : {self.__sold}")

    # Deposit method
    def depot(self, montant):
        self.__sold += montant

    # Withdraw method
    def retirer(self, montant):
        if montant <= self.__sold:
            print("Retrait avec succès")
            self.__sold -= montant
        else:
            print("Solde insuffisant")

    # String representation
    def __str__(self):
        return f"{self.__code}\t{self.__number}\t{self.__name}\t{self.__lastname}\t{self.__sold} euros"


if __name__=='__main__':
    b1 = Bank(1001, 4384023430, "hello", "Lasfar", 5000)
    b1.afficher()
    print("-----------------------------------")

    montant_depot = float(input("Tapez le montant à déposer: "))
    b1.depot(montant_depot)
    print("-----------------------------------")

    montant_retrait = float(input("Tapez le montant à retirer: "))
    b1.retirer(montant_retrait)
    print("-----------------------------------")

    print(b1)
