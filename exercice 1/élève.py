class etudiant:

    def __init__(self,p_nom,p_nb,):
        self.nbetudiant = p_nb
        self.nometudiant = p_nom

    def __str__(self):
        affiche = "\nNuméro d'élève :" + self.nbetudiant
        affiche += "\nNom de l'élève :" + self.nometudiant
        return affiche