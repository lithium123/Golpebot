import sqlite3
from utente import *

conn = sqlite3.connect("impresa.db")
cursor = conn.cursor()


class Impresa:
    def __init__(self, iva, logo, stato, oggetto, ceo, soci, dipendenti, rimanenze):
        self.iva = iva
        self.logo = logo
        self.stato = stato
        self.oggetto = oggetto
        self.ceo = ceo
        self.soci = soci
        self.dipendenti = dipendenti
        self.rimanenze = rimanenze

    def get_iva(self):
        return self.iva
    
    def get_stato(self):
        return self.stato
    
    def get_logo(self):
        return self.logo
    
    def get_oggetto(self):
        return self.oggetto
    
    def get_ceo(self):
        return self.ceo
    
    def get_soci(self):
        return self.soci
    
    def get_dipendenti(self):
        return self.dipendenti
    
    def get_rimanenze(self):
        return self.rimanenze
    
    


