
from repertoire import effter

effter()

class User:
    """donner vie a un Utilisateur"""
    def __init__(self,nom,prenom,sexe,taile,poids,job) -> None:
        """initilisation de l'utilisateur"""
        self.nom = nom
        self.prenom = prenom
        self.sex = sexe
        self.taille = taile
        self.poid = poids
        self.job = job
    
    def __repr__(self) -> str:
        """representation de l'User"""
        return f'User(nom={self.nom}, prenom={self.prenom}, taille={self.taille}, poids={self.poid}, job={self.job})'