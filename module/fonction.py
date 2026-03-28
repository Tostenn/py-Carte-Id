
from os import system,path,getcwd
from time import sleep,localtime
from sys import platform
from json import load
from colorama import init as colorama_init, Fore, Style

colorama_init(autoreset=True)

# modules pour la creation et l'affichage d'image
from PIL import Image, ImageDraw, ImageFont

from cv2 import (
    imread,
    resize,
    moveWindow,
    destroyAllWindows,
    waitKey,
    imshow,
    ROTATE_180,
    imwrite
)

from alive_progress import alive_bar

word_logo = 'Py-Carte-ID'
logo = lambda _ = word_logo : f'\n{Fore.CYAN}{_:-^60}{Style.RESET_ALL}'

def rlt(x = 0.3) -> None:'''renlanti le programme'''; sleep(x)

def effter() -> None:'''efface le terminal''';system("cls") if platform == "win32" else system("clear")

def temps():
    '''renvoir la date et heure'''
    tp = localtime()
    an = [tp.tm_mday,tp.tm_mon,tp.tm_year]
    heur = [tp.tm_hour,tp.tm_min,tp.tm_sec]
    return an,heur

def _alpha_clean(s:str) -> str:
    """enlève les caractères non-alphabétiques courants pour la validation"""
    return s.replace(' ', '').replace('-', '').replace("'", '').replace('é','e').replace('è','e').replace('ê','e').replace('à','a').replace('â','a').replace('ô','o').replace('î','i').replace('û','u').replace('ç','c')

def dataValidation(data:dict):
    """validation des données"""
    data_error = {}
    d = None
    for key, value in data.items():

        if key in ['nom','prenom']:
            if not _alpha_clean(str(value)).isalpha():
                data_error[key] = 'ce champs ne peut contenir que des caractères alphabétiques, tirets ou apostrophes'

        elif key == 'job':
            if not _alpha_clean(str(value)).isalpha():
                data_error[key] = 'ce champs ne peut contenir que des caractères alphabétiques, espaces ou apostrophes'

        elif key == 'sex':
            if not str(value).lower() in ['h','f']:
                data_error[key] = 'ce champs prends comme valeur h ou f | h:homme, f:femme'
        
        elif key in ['taille', 'poids']:
            try:float(value)
            except:data_error[key] = 'ce champs prends comme valeur nombre entier ou decimal'
            
        elif key == 'dtn':
            try:
                parts = str(value).split('/')
                if not len(parts) == 3:
                    data_error[key] = 'ce champs prends comme valeur la date au format jj/mm/aaaa'
                else:
                    d = [int(i) for i in parts]
            except Exception:
                data_error[key] = 'ce champs prends comme valeur la date au format jj/mm/aaaa'

    if d is not None:
        data['dtn'] = d
    if len(data_error) > 0:
        return data, data_error
    return data, False

def __veri_chemin__(chemin:str):
        chemin = chemin if chemin else ''
        if path.exists(chemin):
            if path.isdir(chemin):
                return 'dossier'
            else:
                return 'ficher'
        else : return False

def __conten_fic__(chemin,l = 'r') -> str:
        verifi_ch = __veri_chemin__(chemin)
        if verifi_ch == 'ficher':
            try:
                with open(chemin,l,encoding='utf-8') as file:
                    file = file.read()
            except:
                with open(chemin,l) as file:
                    file = file.read()
            return file
        else : return 

def __ecri_fic__(chemin,text,l = 'w'):
    try:
        with open(chemin,l,encoding='utf-8') as file:
            f= file.write(text)
    except:
        with open(chemin,l) as file:
            f= file.write(text)
    return f
    # renvoir le contenu d'un ficher

def recujson(ch = 'data.json'):
    '''recupere les donners d'un fichier json'''
    try:
        if __veri_chemin__(ch) == 'ficher':
            with open(ch,'r',encoding='utf-8') as file:
                data = load(file)
            return data
    except: return {}
    
def save(op_s:str,data:str,carteID,profile:str,theme:str):
    """determine le format d'enregistre de la sortir"""

    if not op_s:return
    
    action = True
    if not op_s.endswith(('.txt','.png')):
        action = False

    # accepte les fichiers sans extensions
    if not "." in op_s:
        action = True
    
    if not action:
        print(f'{logo()}\n{Fore.RED}le format du fichier indiquer n\'est pas pris en charge{Style.RESET_ALL}{logo()}')
        return

    if op_s.endswith('.txt') or not '.' in op_s:
        saveTxt(op_s,data)
        return 'txt'

    else :
        if theme:
            th = ['dark','light','degrader']
            if not theme in th:
                print(f'{logo()}\n{Fore.RED}erreur | le theme indiquer n\'existe pas | [{", ".join(th)}]{Style.RESET_ALL} {logo()}')
                return 
            
        if profile:
            if not  __veri_chemin__(profile) == 'ficher':
                print(f'{logo()}\n{Fore.RED}erreur | le fichier indiquer [ {profile} ] n\'existe pas{Style.RESET_ALL} {logo()}')
                return
            
            elif not profile.endswith(('.png','.jpeg','.jpg','.webp')):
                print(f'{logo()}\n{Fore.RED}erreur | le fichier indiquer [ {profile} ] n\'est pas une image{Style.RESET_ALL} {logo()}')
                return

        savePng(op_s,carteID,theme,profile)
        return 'png'

def saveTxt(namefile:str,data:str):

    data = data.replace("É","E")
    data = data.replace("N°","N ",1)
    __ecri_fic__(namefile,data)
    print(f'{logo()}\n{Fore.GREEN}sauvegarde réussie | fichier {path.join(getcwd(),namefile)}{Style.RESET_ALL} {logo()}')

# from carte import CarteId
def savePng(op_s:str,carte,theme,profile):

    # position des different champs
    attrs = {
        (275, 102): carte.fmt_pays().upper()+carte.fmt_nb(),
        (250, 140): carte.user.nom.upper(),
        (250, 180): carte.user.prenom.upper(),
        (270, 230): carte.user.date,
        (405, 230): carte.user.sex,
        (255, 280): f'{carte.user.taille} m'.upper(),
        (315, 280): f'{carte.user.masse} kg'.upper(),
        (13, 290):carte.user.job.upper(),
    }

    paths = ['template-dark-id.png','template-light-id.png','template-degrader-id.png']

    # choisir le theme de la carte
    
    color_text = 0
    if theme:
        paths = [i for i in paths if theme in i][0]
        if theme == 'dark': color_text = 255
    else : paths = paths[1]
    
    image = Image.open(path.join('template-id', paths))
    drawer = ImageDraw.Draw(image)
    font_path = path.join('font', 'Roboto-Bold.ttf')
    font = ImageFont.truetype(font_path, 15)


    for attr in attrs:
        drawer.text(attr, attrs[attr], font=font, fill=(color_text, color_text, color_text))
    font = ImageFont.truetype(font_path, 25)
    if theme == 'degrader':
        color_text = 255
    drawer.text((240, 17), carte.user.pays.upper(), font=font, fill=(color_text, color_text, color_text))


    image.save(op_s)


    image = imread(op_s)

    # positionner la photo de profil
    x = 15
    y = 115
    if profile:
        size = (200,170)
        photo = imread(profile)
        photo = resize(photo,size)
        image[y:size[1]+y,x:size[0]+x] =photo[0:size[1],0:size[0]]


    # centrer l'affichage de la carte
    # recuperer les dimension de la fenetre
    from tkinter import Tk
    sizef = Tk()
    sizef = sizef.winfo_screenwidth(),sizef.winfo_screenheight()
    sizef = (sizef[0]//2,sizef[1]//2)

    # recuperer les dimension de l'img
    sizeimg = image.shape
    sizeimg = (sizeimg[0]//2,sizeimg[1]//2)

    fenetre = f'py-Carte-ID-{carte.user.nom}'
    imwrite(op_s,image)
    imshow(fenetre, image)
    moveWindow(
        fenetre,sizef[0]-sizeimg[1],sizef[1]-sizeimg[0]
    )

    waitKey(0)
    destroyAllWindows()

    print(f'{logo()}\n{Fore.GREEN}sauvegarde réussie | fichier {path.join(getcwd(),op_s)}{Style.RESET_ALL} {logo()}')

def barre(total:int=80):
    with alive_bar(total, title=word_logo, receipt=True) as bar:
        for i in range(total):
            rlt(0.01)
            bar.text(word_logo)
            bar()
