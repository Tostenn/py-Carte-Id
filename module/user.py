
from module.fonction import temps

class User:
    """Coordonnés de l'utilisateur"""
    def __init__(
            self,nom:str,prenom:str,age:int,sexe:str,
            taile:float,masse:float,job:str,pays:str,
            daten:str=temps()
        ) -> None:
        """initilisation de l'utilisateur"""
        daten = daten.split('/')

        for i in range(len(daten)):
            if len(daten[i])==1:daten[i] = '0'+daten[i]
        daten = '/'.join(daten)

        assert nom.isalpha() and len(nom) >=3, 'nom is not isalpha and >= 3'
        assert prenom.isalpha() and len(prenom) >=3, 'prenom is not isalpha and >= 3'
        assert age >= 0, 'age >= 0'
        assert sexe in ['H','F'], 'sex in [ H , F ]'
        assert taile >= 0, 'taile >= 0 and at unity Metre'
        assert masse >= 0, 'masse >= 0 and at unity Kilogramme'
        assert job.isalpha() and len(job) >= 3, 'job not isalpha and >= 3'
        assert not (pays.isdigit()) and len(pays) >= 3, 'pays not isalpha and >= 3'
        assert daten.isascii() and len(daten) == 10, 'daten == 10 format 01-01-1001 | dd-mm-yyyy'

        taile = f'{taile:.2f}'

        self.nom = nom
        self.prenom = prenom
        self.sex = sexe
        self.age = age
        self.taille = taile
        self.masse = masse
        self.job = job
        self.pays = pays
        self.date = daten
    
    def __repr__(self) -> str:
        """representation de l'Utilisateur"""
        return f'USER:\nnom: {self.nom}\nprenom: {self.prenom}\nage: {self.age}\nsexe: {self.sex}\ntaille: {self.taille}\npoids: {self.masse}\njob: {self.job}'

    