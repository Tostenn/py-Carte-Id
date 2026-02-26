from module.fonction import temps

class User:
    """nouvelle de l'utilisateur"""

    # nombre d'utilisateur
    nb_User = 0
    def __init__(
            self,nom:str,prenom:str,age:int,sexe:str,
            taile:float,masse:float,job:str,pays:str,
            daten:list=temps()[0]
        ) -> None:
        """initilisation de l'utilisateur"""

        assert len(daten) == 3, 'list [dd,mm,yyyy]'
        daten = [str(i) for i in daten]

        for i in range(len(daten)):
            if i in [0,1] and len(daten[i])==1:daten[i] = '0'+daten[i]
            if i ==2:
                a = 4 - len(daten[i])
                daten[i] = ('0'*a)+daten[i]
                
                
        daten = '/'.join(daten)

        def _alpha_clean(s): return s.replace(' ', '').replace('-', '').replace("'", '').replace('é','e').replace('è','e').replace('ê','e').replace('à','a').replace('â','a').replace('ô','o').replace('î','i').replace('û','u').replace('ç','c')

        assert _alpha_clean(nom).isalpha() and len(nom) >= 3, 'nom is not isalpha and >= 3'
        assert _alpha_clean(prenom).isalpha() and len(prenom) >= 3, 'prenom is not isalpha and >= 3'
        assert age >= 0, 'age >= 0'
        assert sexe.lower() in ['h','f'], 'sex must be  H or F ]'
        assert taile >= 0, 'taile >= 0 and at unity Metre'
        assert masse >= 0, 'masse >= 0 and at unity Kilogramme'
        assert _alpha_clean(job).isalpha() and len(job) >= 3, 'job not isalpha and >= 3'
        assert not (pays.isdigit()) and len(pays) >= 3, 'pays not isalpha and >= 3'
        assert daten.isascii() and len(daten) == 10, 'daten == 10 format 01-01-1001 | dd-mm-yyyy'

        taile = f'{taile:.2f}'

        self.nom = nom
        self.prenom = prenom
        self.sex = sexe.upper()
        self.age = age
        self.taille = taile
        self.masse = masse
        self.job = job
        self.pays = pays
        self.date = daten

        # incrément le nombre d'utilisateur a chaque initilisation
        User.nb_User +=1
    
    def __repr__(self) -> str:
        """representation de l'Utilisateur"""
        return f'User(nom={self.nom}, prenom={self.prenom}, age={self.age}, sexe={self.sex}, taille={self.taille}, poids={self.masse}, job={self.job})'
  
    def __str__(self) -> str:
        """Coordonnés de User"""
        return f'USER: {User.nb_User} \nnom: {self.nom}\nprenom: {self.prenom}\nage: {self.age}\nsexe: {self.sex}\ntaille: {self.taille}\npoids: {self.masse}\njob: {self.job}'
    
    def __description__(self):
        """description de User"""
        return f'''salut je suis {self.nom} {self.prenom}.
je suis un{' homme' if self.sex.lower() == 'h' else 'e femme'},
je fais a peu prés {self.taille} m pése {self.masse} Kg et j'exerce la fonction de {self.job}'''
    
    def __eq__(self,other) -> bool:
        '''egaliter entre utilisateur'''

        # ils seront égaux si ils sont le même sexe, taille, poids
        
        if isinstance(other,User):
            u1 = [self.sex,self.taille,self.pays]
            u2 = [other.sex,other.taille,other.pays]

            if  u1 == u2:return True
        return False

