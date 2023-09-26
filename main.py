
from repertoire import effter
effter()

from module.carte import CarteId,User
# from module.user import User

user = User('kouya','tosten',20,'H',1.8,7200,'developpeur','cote d\'ivoire','1-1-0000')
carte = CarteId(user)
print(carte)
