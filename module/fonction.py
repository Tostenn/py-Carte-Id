

from os import system,path
from time import sleep,localtime
from sys import platform
from json import load


def rlt(x = 0.3) -> True:'''renlanti le programme'''; sleep(x)

def effter():'''efface le terminal''';system("cls") if platform == "win32" else system("clear")

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

def recujson(ch = 'data.json'):
    '''recupere les donners d'un fichier json'''
    try:
        if __veri_chemin__(ch) == 'ficher':
            with open(ch,'r',encoding='utf-8') as file:
                data = load(file)
            return data
    except: return {}
    