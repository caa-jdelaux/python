class Eleve:
    """
    Cette classe représente un élève.

    Attributes:
        nom (str): Le nom de l'élève.
        prenom (str): Le prénom de l'élève.
        notes (dict): Un dictionnaire contenant les notes de l'élève pour chaque matière.
    """

    def __init__(self, nom: str, prenom: str):
        self.nom = nom.upper()
        self.prenom = prenom.capitalize()
        self.notes = dict()
    
    def ajouter_note(self, matiere: str, note: float):
        """
        Ajoute une note pour une matière donnée.

        Args:
            matiere (str): Le nom de la matière.
            note (float): La note à ajouter.
        """
        self.notes[matiere] = note
    
    def get_moyenne(self):
        """
        Calcule la moyenne des notes de l'élève.

        Returns:
            float: La moyenne des notes.
        """
        return sum(self.notes.values()) / len(self.notes)
    
    def voir_moyenne(self):
        """
        Retourne un texte avec la moyenne de l'élève.

        Returns:
            str: Texte contenant la moyenne de l'élève.
        """
        return f"{self.nom} {self.prenom} a une moyenne de {self.get_moyenne():.1f}"
    
    def supprimer_note(self, matiere: str):
        """
        Supprime la note pour une matière donnée.

        Args:
            matiere (str): Le nom de la matière.
        """
        del self.notes[matiere]
        
    def voir_notes(self):
        """
        Affiche les notes de l'élève pour chaque matière.
        """
        for matiere, note in self.notes.items():
            print(f"{matiere} : {note}")

#------------------------------------------------------------------------------------------------
# Help
#help(Eleve)



        
    