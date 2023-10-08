
from os import system,path,getcwd
from time import sleep,localtime
from sys import platform
from json import load
from repertoire import __ecri_fic__
logo = lambda word = 'Py-Carte-ID' : f'\n{word:-^60}'

# modules pour la creation et l'affichage d'image
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2

from tkinter import Tk


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
    
def save(op_s:str,data:str,carteID):
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
        savePng(op_s,carteID)
        return 'png'

def saveTxt(namefile:str,data:str):

    data = data.replace("É","E")
    data = data.replace("N°","N ",1)
    __ecri_fic__(namefile,data)
    print(f'{logo()}\nsauvegarde réussir | fichier {path.join(getcwd(),namefile)} {logo()}')

def savePng(op_s:str,carte):

    attrs = {
        (337, 60):carte.user.job,
        (250, 85): (carte.fmt_pays().upper() + carte.fmt_nb()),
        (240, 110): carte.user.nom.upper(),
        (264, 135): carte.user.prenom.upper(),
        (260, 160): carte.user.date,
        #(257, 162): carte.user.lieu,
        (244, 185): carte.user.taille + " m",
        (377, 185): str(carte.user.masse) + " kg"
    }

    image = Image.open("img/template.png")

    drawer = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 15)

    for attr in attrs:
        drawer.text(attr, attrs[attr], font=font, fill=(0, 0, 0))

    image.save(op_s)

    img = np.array(image)

    # centrer l'affichage de la carte
    # recuperer les dimension de la fenetre
    sizef = Tk()
    sizef = sizef.winfo_screenwidth(),sizef.winfo_screenheight()
    sizef = (sizef[0]//2,sizef[1]//2)

    # recuperer les dimension de l'img
    sizeimg = img.shape
    sizeimg = (sizeimg[0]//2,sizeimg[1]//2)

    fenetre = f'py-Carte-ID-{carte.user.nom}'
    cv2.imshow(fenetre, img)
    cv2.moveWindow(
        fenetre,sizef[0]-sizeimg[1],sizef[1]-sizeimg[0]
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f'{logo()}\nsauvegarde réussir | fichier {path.join(getcwd(),op_s)} {logo()}')
