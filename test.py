

from repertoire import effter

effter()

# print(f"""{'-':-^60}
# |{"république de côte d'ivoire".upper():^59}|
# |{"carte national d'ientité".upper():^59}|
# |{"----------------":^59}|
# |   _______{"_":<49}|
# |  ( _\  /_ ) n CI {'000564454456545':<41}|
# |  | o __ ! | nom : {'kouya':<40}|
# |   \=____=/  prenom : {"tosten boman":<37}|
# |   date de naissance : 04/05/2003 | sex {'femme':<19}|
# |   taille 1.80 m | masse {"70 kg":<34}|
# |{'_':_^59}|
# """)

d = {
        "nom":"ekra",
        "prenom":"rose",
        "dtn":"00-00-0000",
        "sex":"F",
        "taille":1.70,
        "masse":70,
        "pays":"Côte d'ivoire",
        "job":"docter"
}

for i,j in d.items():print(f'{i}:{j}')