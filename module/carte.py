

from random import randint,choices
from module.user import User

class CarteId:
    def __init__(self,user:User) -> None:
        self.user = user
        self.ph_bores(True)
        self.barbe = self.ph_barbe()
        self.ss = self.ph_ssil(True)

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

    def ph_head(self,randoms = False,db= False):

        h = ['!','_','^','-','?']
        id = ''
        if randoms and db:
            h = choices(h,k=randint(1,2))
            while len(id) != 10:
                for i in h:id+=i
        elif randoms: id= ''.join(choices(h))*10
        else: id= h[3] *10
        return id

    def ph_bore(self):
        h = ['|','(']
        return h[randint(0,1)]

    def ph_bores(self,randoms=False):
        # modifier les bordure du visage
        self.bh = self.ph_bore()
        self.bb = self.ph_bore()
        if randoms:
            self.bh += self.ph_bore()
            self.bb += self.ph_bore()

            self.bh = self.bh[0]+ ')' if self.bh[1] == '(' else self.bh
            self.bb =self.bb[0] +')' if self.bb[1] == '(' else self.bb
            
        else:
            self.bh +=')' if self.bh == '(' else '|'
            self.bb +=')' if self.bb == '(' else '|'
        
        # print(self.bh)
        # print(self.bb)

    def ph_jou(self,randoms = False):
        return ''.join(choices([' ','*','!','o']))

    def ph_barbe(self,randoms = False):
        return ''.join(choices(['_','=']))
    
    def ph_ssil(self,randoms = False):
        id =''
        if randoms:
            id = ''.join(choices([' ',"\\"]))
            id+= '/' if id == '\\' else ' '
        else:id = '  '
        return id
            
    def __str__(self) -> str:        
        return f''' {'_':_^59}
|{f"république {self.user.pays}".upper():^59}|
|{"carte national d'ientité".upper():^59}|
|{"--------------":^59}|
|--------------  {f'profession : {self.user.job}':^43}|
|| {self.ph_head(True)} {"|":<46}|
|| {self.bh[0]} _{self.ss[0]}  {self.ss[1]}_ {self.bh[1]} | n {self.fmt_pays().upper()} {self.fmt_nb():<39}|
|| {self.bb[0]} {self.ph_jou()} __ {self.ph_jou()} {self.bb[1]} | nom : {self.user.nom.upper():<38}|
||  \{self.barbe}____{self.barbe}/  | prenom : {self.user.prenom.upper():<35}|
||____________| date de naissance : {self.user.date} | sex {self.fmt_sex().upper():<7}|
|               taille {self.user.taille} m | masse {f"{self.user.masse} kg":<22}|
|{'_':_^59}|
'''
