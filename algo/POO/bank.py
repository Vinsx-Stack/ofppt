class bank:
    def __init__(self, number, name, balance=0):
        self._name = name
        self._number = number
        self._balance = balance

    def afficher(self):
        print(f"Account Number: {self._number}, Account Holder: {self._name}, Balance: {self._balance}")
afficher = bank.afficher