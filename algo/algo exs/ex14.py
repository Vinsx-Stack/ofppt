couleur = input("Saisir une couleur: ")
if couleur == 'vert':
    print("Le candidat peut passer")
else:
    if couleur == 'orange':
        print("Le candidat doit ralentir et preparer a s'arreter")
    else:
        print("Le candidat doit s'arreter")
        

if not (couleur == 'vert'):
    if (couleur == 'orange'):
        print("Le candidat doit ralentir et preparer a s'arreter")
    else:
        print("Le candidat doit s'arreter")
else:
    print("Le candidat peut passer")