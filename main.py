
from repertoire import effter

effter()

class User:
    """donner vie a un Utilisateur"""
    def __init__(self,nom:str,prenom:str,age:int,sexe:str,taile:float,masse:float,job:str) -> None:
        """initilisation de l'utilisateur"""

        assert nom.isalpha() and len(nom) >=3, f'{nom} is not isalpha and >= 3'
        assert prenom.isalpha() and len(prenom) >=3, f'{prenom} is not isalpha and >= 3'
        assert age >= 0, f'{age} >= 0'
        assert sexe in ['H','F'], f'sex in [ H , F ]'
        assert taile >= 0, f'{taile} >= 0 and at unity Metre'
        assert masse >= 0, f'{masse} >= 0 and at unity Kilogramme'
        assert job.isalpha() and len(job) >= 3, f'{job} not isalpha and >= 3'

        self.nom = nom
        self.prenom = prenom
        self.sex = sexe
        self.age = age
        self.taille = taile
        self.masse = masse
        self.job = job
    
    def __repr__(self) -> str:
        """representation de l'User"""
<<<<<<< HEAD
        return f'User(nom={self.nom}, prenom={self.prenom}, taille={self.taille}, poids={self.poid}, job={self.job})'
    


=======
        return f'User(nom={self.nom}, prenom={self.prenom}, age={self.age}, sexe={self.sex}, taille={self.taille}, poids={self.masse}, job={self.job})'
    
    def __str__(self) -> str:
        """presentation de User"""
        return f'''salut je suis {self.nom} {self.prenom}.
je suis un{' homme' if self.sex.lower() == 'h' else 'e femme'},
je fais a peu prés {self.taille} m pése {self.masse} Kg et j'exerce la fonction de {self.job}'''
    

user = User('kouya','tosten',20,'H',1.80,70,'dev')
print(user)
print(user.__repr__())
>>>>>>> makefonction
