def recupere_et_afficher_info_personne(numero_personne): 
 nom , age = recupere_info_personne()
 afficher_info_personne(numero_personne,nom,age)

def recupere_info_personne(numero_personne):
    nom_personne = input(f"Nom de la personne {numero_personne} : ")
    age_personne = input(f"Age de la personne {numero_personne} :  ")
    return nom_personne,age_personne
    

def afficher_info_personne(numero_personne,nom,age):
    print(f"La personne {numero_personne} est {nom} et son age est {age} ans  ")
    print (f"Le nom comporte  {len(nom) } de lettre ")


nb_personne = 3 
for i in range(nb_personne) :
    recupere_et_afficher_info_personne(i+1)
