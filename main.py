
from module.carte import CarteId,User
from module.user import User
from module.fonction import effter

effter()
# programme principale

logo = lambda word = 'Py-Carte-ID' : f'\n{word:-^60}'

user = User(
    prenom='kouya',nom='tosten',age=20,
    sexe='H',taile=1.8,masse=72,job='Developpeur',
    pays='Côte d\'ivoire',
    daten='3/10/1996'
)
print(f'''{user}{logo()}
repr : {user.__repr__()}
{logo()}
''')

carte = CarteId(user)
print(carte)
print(f'{logo()}\n{carte.__repr__()}')

