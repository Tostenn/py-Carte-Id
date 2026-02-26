from module.carte import CarteId
from module.user import User
from module.fonction import (
    effter,
    dataValidation,
    __veri_chemin__,
    __conten_fic__,
    recujson,
    logo,
    word_logo,
    barre,
    save
)

from argparse import ArgumentParser
from pyfiglet import Figlet
from colorama import Fore, Style

# affichage du logo du projet
effter()
py_carte_id = Figlet(direction='center').renderText(word_logo)
print(Fore.CYAN + py_carte_id + Style.RESET_ALL)

usage = '''%(prog)s

    -i | --interactive [console | interface]  mode interactif
        ex : %(prog)s -i console

    -d | --data-path [chemin]  mode data parse
        ex : %(prog)s -d data.json

    -s | --save [fichier.txt | fichier.png]  sauvegarder la sortie
        ex : %(prog)s -d data.json -s carte.png
'''

op = ArgumentParser(description="Py-Carte-ID — Générateur de carte d'identité", usage=usage)

# -i || --interactive
op.add_argument(
    '-i','--interactive', dest='op_i', type=str, metavar='MODE',
    help='passer en mode interactif (console)'
)

# -d || --data-path
op.add_argument(
    '-d','--data-path', dest='op_data', type=str, metavar='FICHIER',
    help='passer en mode data parse (json ou txt)'
)

# -s || --save
op.add_argument(
    '-s','--save', dest='op_save', type=str, metavar='FICHIER',
    help='sauvegarde la sortie (txt ou png)'
)

# --profil
op.add_argument(
    '--profil', dest='op_pp', type=str, metavar='IMAGE',
    help='photo de profil de la carte (png, jpg, webp)'
)

# --theme
op.add_argument(
    '--theme', dest='op_th', type=str, metavar='THEME',
    help='thème de la carte image : dark | light | degrader'
)

argument = op.parse_args()
op_save = argument.op_save
op_pp   = argument.op_pp
op_th   = argument.op_th

# ──────────────────────────────────────────────
# MODE INTERACTIF  -i console
# ──────────────────────────────────────────────
op_i = argument.op_i
if op_i == 'console':
    print(Fore.YELLOW + 'Mode interactif — suivez les instructions' + Style.RESET_ALL)
    fields = [
        'nom','prenom','age','sexe','taille','poids',
        'profession','pays','date de naissance'
    ]
    data = list(fields)  # copie pour stocker les valeurs

    for i in range(len(data)):

        verifi = True
        value = ''
        while verifi:
            if i != 8:
                value = input(f'{Fore.CYAN}  ▸ {data[i]}{Style.RESET_ALL} : ').strip()
                if not value:
                    print(f'{Fore.RED}  ✗ Veuillez entrer une valeur.{Style.RESET_ALL}')
                    continue

            if i in [0, 1]:  # nom, prenom : str alpha
                clean = value.replace('-','').replace("'",'')
                if clean.isalpha() and len(value) >= 3:
                    data[i] = value
                    verifi = False
                else:
                    print(f'{Fore.RED}  ✗ Valeur invalide — lettres uniquement (min. 3 caractères){Style.RESET_ALL}')

            elif i == 2:  # age : entier >= 0
                try:
                    v = int(value)
                    if v >= 0:
                        data[i] = v
                        verifi = False
                    else:
                        print(f'{Fore.RED}  ✗ L\'âge doit être >= 0{Style.RESET_ALL}')
                except:
                    print(f'{Fore.RED}  ✗ Entrez un nombre entier{Style.RESET_ALL}')

            elif i == 3:  # sexe
                if value.lower() in ['h', 'f']:
                    data[i] = value
                    verifi = False
                else:
                    print(f'{Fore.RED}  ✗ Valeur attendue : h (homme) ou f (femme){Style.RESET_ALL}')

            elif i in [4, 5]:  # taille, poids : float/int
                try:
                    data[i] = float(value)
                    verifi = False
                except:
                    print(f'{Fore.RED}  ✗ Entrez un nombre entier ou décimal{Style.RESET_ALL}')

            elif i == 6:  # profession
                clean = value.replace(' ','').replace('-','').replace("'",'')
                if clean.isalpha() and len(value) >= 3:
                    data[i] = value
                    verifi = False
                else:
                    print(f'{Fore.RED}  ✗ Valeur invalide — lettres uniquement (min. 3 caractères){Style.RESET_ALL}')

            elif i == 7:  # pays
                if len(value) >= 3:
                    data[i] = value
                    verifi = False
                else:
                    print(f'{Fore.RED}  ✗ Le nom du pays doit avoir au moins 3 caractères{Style.RESET_ALL}')

            else:  # date de naissance
                d_parts = ['jour', 'mois', 'année']
                d_vals  = [0, 0, 0]
                limits  = [(1, 31), (1, 12), (1000, 9999)]
                ok = True
                for j in range(3):
                    v = True
                    while v:
                        raw = input(f'{Fore.CYAN}    ▸ {d_parts[j]} de naissance{Style.RESET_ALL} : ').strip()
                        if raw.isdigit():
                            n = int(raw)
                            lo, hi = limits[j]
                            if lo <= n <= hi:
                                d_vals[j] = n
                                v = False
                            else:
                                print(f'{Fore.RED}    ✗ {d_parts[j]} doit être entre {lo} et {hi}{Style.RESET_ALL}')
                        else:
                            print(f'{Fore.RED}    ✗ Entrez un nombre entier{Style.RESET_ALL}')
                data[i] = d_vals
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
    userCarte = CarteId(user).__str__()

    effter()
    print(Fore.CYAN + py_carte_id + Style.RESET_ALL)
    barre()

    # affiche la carte dans la console -s txt || no -s
    op_save = save(op_save, userCarte, CarteId(user), op_pp, op_th)
    if op_save == 'txt' or not op_save:
        print(userCarte)
    exit()

# ──────────────────────────────────────────────
# MODE DATA PARSE  -d fichier
# ──────────────────────────────────────────────
op_data = argument.op_data
if op_data:

    if not __veri_chemin__(op_data) == 'ficher':
        print(f'{Fore.RED}✗ Le chemin [ {op_data} ] fourni est invalide.{Style.RESET_ALL}')
        exit()

    if not op_data.endswith(('.txt', '.json')):
        print(f'{Fore.RED}✗ Le format du fichier [ {op_data} ] n\'est pas pris en compte.\n  Formats acceptés : json, txt{Style.RESET_ALL}')
        exit()

    # clés obligatoires
    data_key = ['nom', 'prenom', 'sex', 'taille', 'dtn', 'poids', 'pays', 'job']

    # fichier texte
    if op_data.endswith('.txt'):
        raw = __conten_fic__(op_data).split('\n')
        datas = {}
        for line in raw:
            line = line.strip()
            if ':' in line:
                datas[line[:line.index(':')].strip()] = line[line.index(':')+1:].strip()

    # fichier json
    else:
        datas = recujson(op_data)

    # vérification des clés
    no_key = [k for k in data_key if not datas.get(k)]
    if no_key:
        print(f'{Fore.RED}✗ Données manquantes :{Style.RESET_ALL}')
        for k in no_key:
            print(f'  {Fore.YELLOW}• {k}{Style.RESET_ALL}')
        exit()

    # validation des données
    datas, error = dataValidation(datas)

    barre()
    if not error:
        user = User(
            nom=datas['nom'],
            prenom=datas['prenom'],
            age=10,
            sexe=datas['sex'],
            taile=float(datas['taille']),
            masse=int(datas['poids']),
            job=datas['job'],
            pays=datas['pays'],
            daten=datas['dtn']
        )
        userCarte = CarteId(user).__str__()

        op_save = save(op_save, userCarte, CarteId(user), op_pp, op_th)
        if op_save == 'txt' or not op_save:
            print(userCarte)

    else:
        print(f'{Fore.RED}✗ Erreurs de validation :{Style.RESET_ALL}')
        for k, msg in error.items():
            print(f'  {Fore.YELLOW}• {k}{Style.RESET_ALL} : {msg}')
    exit()


# ──────────────────────────────────────────────
# AFFICHAGE PAR DÉFAUT (démo)
# ──────────────────────────────────────────────
user = User(
    prenom='Kouya', nom='Tosten', age=20,
    sexe='H', taile=1.8, masse=72, job='Developpeur',
    pays="Côte d'Ivoire",
    daten=[3, 10, 1996]
)

carte = CarteId(user)
print(carte)
print(op.format_usage())

