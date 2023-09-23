
from repertoire import effter

effter()

class User:

    def __init__(self,nom,prenom,sexe,taile,poids,job) -> None:
        self.nom = nom
        self.prenom = prenom
        self.sex = sexe
        self.taille = taile
        self.poid = poids
        self.job = job
    
    def __repr__(self) -> str:
        return f'User(nom={self.nom}, prenom={self.prenom}, taille={self.taille}, poids={self.poid}, job={self.job})'