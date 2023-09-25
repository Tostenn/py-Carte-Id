
from repertoire import effter,temps
from random import randint
effter()

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
    
class CarteId:
    def __init__(self,user:User) -> None:
        self.user = user
    
    def __repr__(self) -> str:return f'CarteId(user={self.user.__repr__()})'

    def fmt_pays(self) -> str:
        '''récupération du code pays'''
        pays = self.user.pays
        id = ''
        if pays.count(' ') >= 1: # [1; +oo]
            pays = pays.split(' ')[:2]

            for i in pays:
                if "'" in i:i = i[i.index("'")+1:i.index("'")+2]
                else : i = i[0]
                id += i

        else : id = pays[:2]

        return id
    
    def fmt_nb(seif) -> str:
        '''numéro aléatoire de carte d'identite '''
        n = randint(1,15)
        id = '0'*(15-n)
        for i in range(n): id += str(randint(0,9))
        return id

    def fmt_sex(self) -> str:
        '''formate le sex de User'''
        if self.user.sex.lower() == 'h': return 'male'
        else: return 'femelle'

    def __str__(self) -> str:        
        return f'''{'-':-^60}
|{f"république {self.user.pays}".upper():^59}|
|{"carte national d'ientité".upper():^59}|
|{"--------------":^59}|
|{"--------------":<59}|
||  ________  {"|":<46}|
|| | _    _ | | n {self.fmt_pays().upper()} {self.fmt_nb():<39}|
|| ( * __ | ) | nom : {self.user.nom:<38}|
||  \______/  | prenom : {self.user.prenom:<35}|
||____________| date de naissance : {self.user.date} | sex {self.fmt_sex().upper():<7}|
|               taille {self.user.taille} m | masse {f"{self.user.masse} kg":<22}|
|{'_':_^59}|
'''

user = User('kouya','tosten',20,'F',1.8,7200,'dev','cote d\'ivoire','1-1-0000')
# print(user)
# print(user.__repr__())
carte = CarteId(user)
print(carte)
# print(carte.__repr__())