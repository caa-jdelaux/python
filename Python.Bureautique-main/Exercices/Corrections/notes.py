class Notes:
    def __init__(self):
        self.notes = []
    
    def ajouter_note(self, note):
        self.notes.append(note)

    def min(self):
        return min(self.notes)
    
    def max(self):
        return max(self.notes)
    
    def moyenne(self):
        return sum(self.notes) / len(self.notes)