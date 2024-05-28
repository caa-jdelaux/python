class Eleve:
    """
    Cette classe représente un élève.

    Attributes:
        nom (str): Le nom de l'élève.
        prenom (str): Le prénom de l'élève.
        notes (dict): Un dictionnaire contenant les notes de l'élève pour chaque matière.
    """

    def __init__(self, nom: str, prenom: str):
        """
        Initialise un nouvel élève.
        
        Args:
            nom (str): Le nom de l'élève.
            prenom (str): Le prénom de l'élève.
            notes (dict): Un dictionnaire contenant les notes de l'élève pour chaque matière.
        """
        self.nom = nom.upper()
        self.prenom = prenom.capitalize()
        self.notes = dict()
    
    def __str__(self):
        """
        Retourne une représentation de l'élève sous forme de chaîne de caractères.
        
        Returns:
            str: Une chaîne de caractères représentant l'élève.
        """
        return f"{self.nom} {self.prenom}"
    
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
        if not self.notes:
            return 0
        else:
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
    
    def modifier_note(self, matiere: str, note: float):
        """
        Modifie la note pour une matière donnée.

        Args:
            matiere (str): Le nom de la matière.
            note (float): La nouvelle note.
        """
        self.notes[matiere] = note
        
    def voir_notes(self):
        """
        Affiche les notes de l'élève pour chaque matière.
        """
        for matiere, note in self.notes.items():
            print(f"{matiere} : {note}")


class Notes:
    """
    Cette classe représente une liste de notes.

    Attributes:
        notes (list): Une liste contenant les notes
    """

    def __init__(self):
        """
        Initialise un nouvel ensemble de notes.
        
        Attributes:
            notes (list): Une liste contenant les notes
        """
        self.notes = list()
    
    def ajouter(self, note: float):
        """
        Ajoute une note à la liste.

        Args:
            note (float): La note à ajouter.
        """
        # if note < 0 or note > 20:
        #     # raise ValueError(f"La note doit être comprise entre 0 et 20. La note '{note}'n'a pas été ajoutée.")
        #     print(f"La note '{note}'n'a pas été ajoutée.")
            
        #     print("\n\n")
            
        #     print("Traitements sur les notes")
        #     if not self.notes:
        #         print("Aucune note n'a été ajoutée.")
        #         exit()
        #     else:
        #         print("Voici les notes : ", self.notes)
        #         print("la note maximale est de : ", self.get_max())
        #         print("la note minimale est de : ", self.get_min())
        #         print("La moyenne est de : ", self.get_moyenne())
        #         exit()
        # else:
        #     print(f"La note '{note}' a été ajoutée.", end="\n\n")
        self.notes.append(note)
    
    def get_moyenne(self):
        """
        Calcule la moyenne des notes.

        Returns:
            float: La moyenne des notes.
        """
        if not self.notes:
            return 0
        else:
            return sum(self.notes) / len(self.notes)
    
    def get_max(self):
        """
        Retourne la note maximale.

        Returns:
            float: La note maximale.
        """
        return max(self.notes)
    
    def get_min(self):
        """
        Retourne la note minimale.

        Returns:
            float: La note minimale.
        """
        return min(self.notes)
    
    def voir_notes(self):
        """
        Affiche la liste des notes.
        """
        for note in self.notes:
            print(note, end="\t")
        print()



        
    