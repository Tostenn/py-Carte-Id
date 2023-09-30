


from os import system
from time import sleep,localtime
from sys import platform



def rlt(x = 0.3) -> True:'''renlanti le programme'''; sleep(x)

def effter():'''efface le terminal''';system("cls") if platform == "win32" else system("clear")

def temps():
    '''renvoir la date et heure'''
    tp = localtime()
    an = [tp.tm_mday,tp.tm_mon,tp.tm_year]
    heur = [tp.tm_hour,tp.tm_min,tp.tm_sec]
    return an,heur
