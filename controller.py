import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower()) # PULIZIA DEL TESTO

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handle_language_change(self, e):
        # Recuperiamo la lingua selezionata dal dropdown della view
        lingua = self._view._dd_language.value
        if lingua:
            # Creiamo un messaggio di conferma (SnackBar)
            self._view.page.snack_bar = ft.SnackBar(ft.Text(f"Lingua impostata su: {lingua}"))
            self._view.page.snack_bar.open = True
        self._view.update()

    def handle_spell_check(self, e):
        # 1. Recupero i dati dai componenti della View
        testo_input = self._view._txt_input.value
        lingua = self._view._dd_language.value
        modalita = self._view._dd_modality.value

        # 2. Controlli di validità (come richiesto dalla traccia)
        if not lingua or not modalita or not testo_input:
            self._view.page.snack_bar = ft.SnackBar(ft.Text("Errore: Compila tutti i campi!"))
            self._view.page.snack_bar.open = True
            self._view.update()
            return

        # 3. Chiamata alla logica del Lab 03 (che restituisce parole e tempo)
        # Nota: mappiamo i nomi del dropdown con quelli del tuo match/case
        """ UTILE -> fa capire cosa deve prendere anche se nel view l'ho scritto con parole diverse """
        modality_map = {
            "contains": "Default",
            "linear": "Linear",
            "dicotomic": "Dichotomic"
        }

        risultato_parole, tempo = self.handleSentence(testo_input, lingua, modality_map[modalita])

        # 4. Aggiornamento dell'interfaccia (ListView)
        self._view._lv_output.controls.append(ft.Text(f"Frase: {testo_input}"))
        self._view._lv_output.controls.append(ft.Text(f"Parole errate: {risultato_parole}"))
        self._view._lv_output.controls.append(ft.Text(f"Tempo di esecuzione: {tempo:.6f}s"))
        self._view._lv_output.controls.append(ft.Divider())  # Una riga di separazione

        # 5. Pulizia del campo di testo come richiesto
        self._view._txt_input.value = ""

        # 6. Refresh della pagina
        self._view.update()


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text