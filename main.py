
from repertoire import effter

effter()

class User:
    """donner vie a un Utilisateur"""
    def __init__(self,nom:str,prenom:str,age:int,sexe:str,taile:str,poids:str,job:str) -> None:
        """initilisation de l'utilisateur"""
        self.nom = nom
        self.prenom = prenom
        self.sex = sexe
        self.age = age
        self.taille = taile
        self.poid = poids
        self.job = job
    
    def __repr__(self) -> str:
        """representation de l'User"""
        return f'User(nom={self.nom}, prenom={self.prenom}, age={self.age}, sexe={self.sex}, taille={self.taille}, poids={self.poid}, job={self.job})'
    
    def __str__(self) -> str:
        """presentation de User"""
        return f'''salut je suis {self.nom} {self.prenom}.
je suis un{' homme' if self.sex.lower() == 'h' else 'e femme'},
je fais a peu prés {self.taille} m pése {self.poid} et j'exerce la fonction de {self.job}'''
    