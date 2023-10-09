
from os import system,path,getcwd
from time import sleep,localtime
from sys import platform
from json import load

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

from tkinter import Tk

logo = lambda word = 'Py-Carte-ID' : f'\n{word:-^60}'

def rlt(x = 0.3) -> None:'''renlanti le programme'''; sleep(x)

def effter() -> None:'''efface le terminal''';system("cls") if platform == "win32" else system("clear")

def temps():
    '''renvoir la date et heure'''
    tp = localtime()
    an = [tp.tm_mday,tp.tm_mon,tp.tm_year]
    heur = [tp.tm_hour,tp.tm_min,tp.tm_sec]
    return an,heur

def dataValidation(data:dict):
    """validation des donnée"""
    data_error = {}
    for key, value in data.items():

        if key in ['nom','prenom','job']:
            if not value.isalpha():
                data_error[key] = 'ce champs ne peut contenir que des caractére alphabétique | [a-zA-Z]'
        
        elif key == 'sex':
            if not value.lower() in ['h','f']:
                data_error[key] = 'ce champs prends comme valeur h ou f | h:homme, f:femme'
        
        elif key in ['taille', 'poids']:
            try:float(value)
            except:data_error[key] = 'ce champs prends comme valeur nombre entier ou decimal'
            
        elif key == 'dtn':
            try:
                d = value.split('/')
                if not len(d) == 3:
                    data_error[key] = 'ce champs prends comme valeur la date au foramt jj/dd/aaaa'
                    
                else:d = [int(i) for i in d]
            except Exception:
                data_error[key] = 'ce champs prends comme valeur la date au foramt jj/dd/aaaa'

    data['dtn'] = d
    if len(data_error)>0:
        return data,data_error
    return data,False

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
        print(f'{logo()}\nle format du fichier indiquer n\'est pas pris en charge{logo()}')
        return

    if op_s.endswith('.txt') or not '.' in op_s:
        saveTxt(op_s,data)
        return 'txt'

    else :
        if theme:
            th = ['dark','light','degrader']
            if not theme in th:
                print(f'{logo()}\nerreur | le theme indiquer n\'existe pas | [{", ".join(th)}] {logo()}')
                return 
            
        if profile:
            if not  __veri_chemin__(profile) == 'ficher':
                print(f'{logo()}\nerreur | le fichier indiquer [ {profile} ] n\'existe pas {logo()}')
                return
            
            elif not profile.endswith(('.png','.jpeg','.jpg','.webp')):
                print(f'{logo()}\nerreur | le fichier indiquer [ {profile} ] n\'est pas une image {logo()}')
                return

        savePng(op_s,carteID,theme,profile)
        return 'png'

def saveTxt(namefile:str,data:str):

    data = data.replace("É","E")
    data = data.replace("N°","N ",1)
    __ecri_fic__(namefile,data)
    print(f'{logo()}\nsauvegarde réussir | fichier {path.join(getcwd(),namefile)} {logo()}')

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

    paths = ['template-dark-id.png','template-ligth-id.png','template-degrader-id.png']

    # choisir le theme de la carte
    
    color_text = 0
    if theme:
        paths = [i for i in paths if theme in i][0]
        if theme == 'dark': color_text = 255
    else : paths = paths[1]
    
    image = Image.open('template-id/'+paths)
    drawer = ImageDraw.Draw(image)
    font = ImageFont.truetype(r"font\Roboto-Bold.ttf", 15)


    for attr in attrs:
        drawer.text(attr, attrs[attr], font=font, fill=(color_text, color_text, color_text))
    font = ImageFont.truetype(r"font\Roboto-Bold.ttf", 25)
    drawer.text((240, 17), carte.user.pays.upper(), font=font, fill=(color_text, color_text, color_text))


    image.save(op_s)

    
    image = imread(op_s)

    # positionner la photo de profil
    x = 15
    y = 112
    if profile:
        size = (200,170)
        photo = imread(profile)
        photo = resize(photo,size)
        print(photo.size)
        image[y:size[1]+y,x:size[0]+x] =photo[0:size[1],0:size[0]]


    # posionner le drapeau
    # size = (50,33)
    # photo = resize(photo,size)
    # photo = rotate(photo,ROTATE_180)
    # x = 434
    # y = 19
    # image[y:size[1]+y,x:size[0]+x] =photo[0:size[1],0:size[0]]


    # centrer l'affichage de la carte
    # recuperer les dimension de la fenetre
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

    print(f'{logo()}\nsauvegarde réussir | fichier {path.join(getcwd(),op_s)} {logo()}')
