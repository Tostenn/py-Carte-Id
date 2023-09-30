
from module.carte import CarteId,User
from module.user import User
from module.fonction import effter

# insertion du mode interactif -i || --interactif
from optparse import OptionParser

usage = '''Usage de l'IA
    python main.py
        -i || --interactif [active || desactive] passer en mode interactif
        ex : python main.py -i active
'''

op = OptionParser(usage,version='1.0.0.1')
op.add_option(
    '-i','--interactif',dest='op_i',type='string',
    help='passer en mode interactif'
)

argument = op.parse_args()[0]
effter()


# gestion du mode interactif -i || --interatif
op_i = argument.op_i
if op_i == 'active':
    print('intregrer une annimation ici | mode interactif')
    data = [
        'nom','prenom','age','sex','taille','poids',
        'profession','pays','date de naissance'
    ]
    
    for i in range(len(data)):

        verifi = True
        while verifi:
            if i != 8:
                value = input(f'entre votre {data[i]} : ')
            if not value:
                print('entre une valeur ')
                continue

            if i in [0,1,6]:# value str isalpha
                if value.isalpha():
                    data[i] = value
                    verifi = False
                else:
                    print('type d\'entrer inattendu [a-z]')
                    continue

            elif i in [2,4,5]:# value int/float
                try:
                    data[i] = float(value)
                    verifi = False
                except:
                    print('entrer un int || float')
                    continue
       
            elif i == 3:#sex
                if value.lower() in ['h','f']:
                    data[i] = value
                    verifi = False
                else:
                    print('sen in [ h, f ]')
                    continue

            elif i == 7:# pays
                if not value.isdigit():
                    data[i] = value
                    verifi = False
                else :
                    print('le pays ne doit pas contenir de chiffre')
                    continue
            
            else :#date de naissance
                d = ["jours",'mois','année']
                for j in range(len(d)):
                    v = True
                    while v:
                        value = input(f'entre votre {d[j]} de naissance : ')
                        if value.isdigit():
                            value = int(value)
                            if j == 0:
                                if value < 32:d[0] = value;v= False
                                else : 
                                    print('jours <= 31')
                                    continue

                            if j == 1:
                                if value < 13:d[1] = value;v= False
                                else : 
                                    print('mois <= 12')
                                    continue

                            if j == 2:
                                if len(str(value)) == 4 :d[2] = value;v= False
                                else :
                                    print('anne [0000-9999]')
                                    continue
                data[i] = d
                verifi = False
    
    user = User(
        nom=data[0],
        prenom=data[1],
        age=data[2],
        sexe=data[3],
        taile=data[4],
        masse=data[5],
        job=data[6],
        pays=data[7],
        daten=data[8]
    )
    userCatre = CarteId(user)
    effter()
    print('annimation ici aussi')
    print(userCatre)
    exit()


# # programme principale

logo = lambda word = 'Py-Carte-ID' : f'\n{word:-^60}'

user = User(
    prenom='kouya',nom='tosten',age=20,
    sexe='H',taile=1.8,masse=72,job='Developpeur',
    pays='Côte d\'ivoire',
    daten=[3,10,1996]
)
# print(f'''{user}{logo()}
# repr : {user.__repr__()}
# {logo()}
# ''')

carte = CarteId(user)
print(carte)
# print(f'{logo()}\n{carte.__repr__()}')
print(op.usage)

