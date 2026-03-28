""" Questa classe mi dice se la singola parola (di un testo) è scritta correttamente"""
class RichWord:
    def __init__(self, parola):
        self._parola = parola # Memorizzo parola
        self._corretta = False # flag

    # def isCorretta(self):
    #     if self._corretta is not None:
    #         return self._corretta

    @property
    def corretta(self):
        print("getter of parola called" )
        return self._corretta

    """ Creo setter per modificare in corretta """
    @corretta.setter
    def corretta(self, value: bool):
        print("setter of parola called" )
        self._corretta = value

    """ Stampa parola """
    def __str__(self):
        return self._parola