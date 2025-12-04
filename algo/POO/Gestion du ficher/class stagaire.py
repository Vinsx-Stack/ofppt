class Stagiaire:
    c = 1
    def __init__(self, numero, nom, prenom, note, filiere):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__note = note
        self.__filiere = filiere
        Stagiaire.c += 1
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, new):
        self.__numero = new

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, new):
        self.__nom = new
    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, new):
        self.__prenom = new
    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, new):
        self.__note = new
    @property
    def filiere(self):
        return self.__filiere
    @filiere.setter
    def filiere(self, new):
        self.__filiere = new
    def __str__(self):
        return f"Stagiaire numero: {self.__numero}, nom: {self.__nom}, prenom: {self.__prenom}, note: {self.__note}, filiere: {self.__filiere}"
    