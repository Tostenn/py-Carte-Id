
from module.carte import CarteId
from module.user import User
from module.fonction import (
    effter,
    dataValidation,
    __veri_chemin__,
    __conten_fic__,
    recujson,
    logo,
    save
)

# insertion du mode interactif -i || --interactif
from optparse import OptionParser

usage = '''Usage de l'IA
    python main.py
    
        -i || --interactif [console || interface] passer en mode interactif
            ex : python main.py -i console

        -d || --data-path [chemin] | passer en mode data parse
            ex : python main.py -d data.json

        -s || --save [txt || img || ..] sauvegarder la sortir en un format donnée
            vous pouvez le combiné avec tout les4 paramétre de géneration de Carte ID
            ex : python main.py -d data.json -s fichier.png
'''

op = OptionParser(usage,version='2.0.1')

# -i || --interactive
op.add_option(
    '-i','--interactive',dest='op_i',type='string',
    help='passer en mode interactif'
)

# -d || --data-path
op.add_option(
    '-d','--data-path',dest='op_data',type='string',
    help='passer en mode data parse'
)

# -s || --save
op.add_option(
    '-s','--save',dest='op_save',type='string',
    help='sauvegarde la sortir'
)

argument = op.parse_args()[0]
op_save = argument.op_save
effter()


# gestion du mode interactif -i || --interatif
# le parametre est prioritaire sur les autre et les annule tous
op_i = argument.op_i
if op_i == 'console':
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
                if len(value)>3:
                    data[i] = value
                    verifi = False
                else :
                    print('le pays doit avoir un nombre de caractére > 3')
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
                                if 0 < len(str(value)) < 5 :d[2] = value;v= False
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
    userCatre = CarteId(user).__str__()
    op_save = save(op_save,userCatre,CarteId(user))
   
    effter()
    print('annimation ici aussi')

    # affiche la carte dans la console -s txt || no -s
    op_save = save(op_save,userCatre,CarteId(user))
    if op_save == 'txt' or not op_save:
        print(userCatre)
    exit()

# le second parametre est prioritaire
op_data = argument.op_data
if op_data:

    if not __veri_chemin__(op_data) == 'ficher':
        print(f'le chiemin [ {op_data} ] fournir est [invalide] ')
        exit()

    # chemin existe 
    # vérification de l'extension du fichier

    if not op_data.endswith(('.txt','.json')):
        print(f'le format du fichier [ {op_data} ] fournir n\'est pas pris en compte \nformat accepter [json] et [txt] ')
        exit()

    # key obligatoire
    data_key = ['nom','prenom','sex','taille','dtn','poids','pays','job']

    # fichier texte
    if op_data.endswith(('.txt')):
        data = __conten_fic__(op_data).split('\n')
        datas = {}
        for i in data:
            i = i.strip()
            if ':' in i:
                datas[i[:i.index(':')]] = i[i.index(':')+1:]
        del data

    # fichier json
    else:
        datas = recujson(op_data)
        print(datas)
        exit()

    # verification des clés
    no_key = [i for i in data_key if not datas.get(i)]

    if len(no_key) > 0:
        print(f'des données manquantes ont été détecter\nliste\n|{"-"*5}'+f'\n|{"-"*5}'.join(no_key))
        exit()
    
    # validation des données
    datas,error = dataValidation(datas)

    effter()
    if not error:
        user = User(
            nom=datas['nom'],
            prenom=datas['prenom'],
            age= 10,
            sexe=datas['sex'],
            taile=float(datas['taille']),
            masse=int(datas['poids']),
            job=datas['job'],
            pays=datas['pays'],
            daten=datas['dtn']
        )
        userCatre = CarteId(user).__str__()
        effter()
        print('annimation ici aussi')

        # affiche la carte dans la console -s txt || no -s
        op_save = save(op_save,userCatre,CarteId(user))
        if op_save == 'txt' or not op_save:
            print(userCatre)

    else:
        print('erreur survenu\nListe')
        for i,j in error.items():
            print(f'{"-"*5}{i}:{j}')
    exit()

# # programme principale


user = User(
    prenom='kouya',nom='tosten',age=20,
    sexe='H',taile=1.8,masse=72,job='Developpeur',
    pays='Côte d\'ivoire',
    daten=[3,10,196]
)
# print(f'''{user}{logo()}
# repr : {user.__repr__()}
# {logo()}
# ''')

carte = CarteId(user)
print(carte)
# print(f'{logo()}\n{carte.__repr__()}')
print(op.usage)
