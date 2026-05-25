import random
import string
import os
import time

choisis = int(input("Choisis le nombre de lettre & chiffre de ton mdps : "))


def mdps():
    charactere = string.punctuation + string.ascii_letters + string.digits
    
    if choisis > 12:
        return "".join(random.choices(charactere, k=choisis))
    
    else:
        print("Salut C'est la petite voix dans ta tete sache qu'un mot de passe avec aussi peux de charactère sais pas une bonne idées voila ;)")
        return "".join(random.choices(charactere, k=choisis))


# choisis = int(input("Choisis le nombre de lettre & chiffre de ton mdps : "))
# On me conseil d'y mètre ici pour moi ca vien du pareil au meme dans mon cas mais voila si vous voulez vous avez justa suprimé l'encien et decomenter celui la :)

print(mdps())
time.sleep(2)
print("Je vais maintenant clear la cnosole")
time.sleep(2)
os.system("cls")
