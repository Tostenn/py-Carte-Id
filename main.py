
from repertoire import effter

effter()

class User:
    """donner vie a un Utilisateur"""
    def __init__(
            self,nom:str,prenom:str,age:int,sexe:str,
            taile:float,masse:float,job:str,pays:str
        ) -> None:
        """initilisation de l'utilisateur"""

        assert nom.isalpha() and len(nom) >=3, f'{nom} is not isalpha and >= 3'
        assert prenom.isalpha() and len(prenom) >=3, f'{prenom} is not isalpha and >= 3'
        assert age >= 0, f'{age} >= 0'
        assert sexe in ['H','F'], f'sex in [ H , F ]'
        assert taile >= 0, f'{taile} >= 0 and at unity Metre'
        assert masse >= 0, f'{masse} >= 0 and at unity Kilogramme'
        assert job.isalpha() and len(job) >= 3, f'{job} not isalpha and >= 3'
        assert pays.isascii() and len(pays) >= 3, f'{pays} not isalpha and >= 3'

        self.nom = nom
        self.prenom = prenom
        self.sex = sexe
        self.age = age
        self.taille = taile
        self.masse = masse
        self.job = job
        self.pays = pays
    
    def __repr__(self) -> str:
        """representation de l'User"""
        return f'User(nom={self.nom}, prenom={self.prenom}, age={self.age}, sexe={self.sex}, taille={self.taille}, poids={self.masse}, job={self.job})'
    
    def __str__(self) -> str:
        """presentation de User"""
        return f'''salut je suis {self.nom} {self.prenom}.
je suis un{' homme' if self.sex.lower() == 'h' else 'e femme'},
je fais a peu prés {self.taille} m pése {self.masse} Kg et j'exerce la fonction de {self.job}'''
    
class CarteId:
    def __init__(self,user:User) -> None:
        self.user = user
    
    def __repr__(self) -> str:return f'CarteId(user=User)'
    
    def __str__(self) -> str:
        return f'''f"""{'-':-^60}
|{f"république {self.user.pays}".upper():^59}|
|{"carte national d'ientité".upper():^59}|
|{"----------------":^59}|
|   _______{"_":<49}|
|  | _    _ | n CI {'000564454456545':<41}|
|  (   __   ) nom : {self.user.nom:<40}|
|   \______/  prenom : {self.user.prenom:<37}|
|   date de naissance : 04/05/2003 | sex {self.user.sex:<19}|
|   taille 1.80 m | masse {f"{self.user.masse} kg":<34}|
|{'_':_^59}|
"""'''
        
user = User('kouya','tosten',20,'H',1.80,70,'dev','cote d ivoire')
print(user)
print(user.__repr__())