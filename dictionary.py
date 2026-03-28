class Dictionary:
    """ Inizializziamo l'oggetto """
    def __init__(self, dict=[], language = ""):
        # La _ indica che è una variabile protetta -> ci va il getter
        self._dict = dict  # Lista che conterrà tutte le parole del dizionario
        self._language = language # Memorizzo la lingua del dizionario

    """ Scarichiamo e leggiamo il file dizionario """
    def loadDictionary(self,path):
        file_path = path
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                value = line.strip()
                self._dict.append(value.lower())

    """ Stampa lista del dizionario """
    def printAll(self):
        for value in self._dict:

            print(f" {value}")

    """ Creo il getter per poter accederci in maniera protetta (non è possibile modificarla)"""
    @property
    def dict(self):
        return self._dict