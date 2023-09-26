
from repertoire import temps

class User:
    """donner vie a un Utilisateur"""
    def __init__(
            self,nom:str,prenom:str,age:int,sexe:str,
            taile:float,masse:float,job:str,pays:str,
            daten:str=temps()[0]
        ) -> None:
        """initilisation de l'utilisateur"""
        daten = daten.split('-')

        for i in range(len(daten)):
            if len(daten[i])==1:daten[i] = '0'+daten[i]
        daten = '-'.join(daten)

        assert nom.isalpha() and len(nom) >=3, 'nom is not isalpha and >= 3'
        assert prenom.isalpha() and len(prenom) >=3, 'prenom is not isalpha and >= 3'
        assert age >= 0, 'age >= 0'
        assert sexe in ['H','F'], 'sex in [ H , F ]'
        assert taile >= 0, 'taile >= 0 and at unity Metre'
        assert masse >= 0, 'masse >= 0 and at unity Kilogramme'
        assert job.isalpha() and len(job) >= 3, 'job not isalpha and >= 3'
        assert pays.isascii() and len(pays) >= 3, 'pays not isalpha and >= 3'
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
        """representation de l'User"""
        return f'User(nom={self.nom}, prenom={self.prenom}, age={self.age}, sexe={self.sex}, taille={self.taille}, poids={self.masse}, job={self.job})'
    
    def __str__(self) -> str:
        """presentation de User"""
        return f'''salut je suis {self.nom} {self.prenom}.
je suis un{' homme' if self.sex.lower() == 'h' else 'e femme'},
je fais a peu prés {self.taille} m pése {self.masse} Kg et j'exerce la fonction de {self.job}'''
    