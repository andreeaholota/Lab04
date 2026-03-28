import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER' # Allinea il testo al centro
        self.page.theme_mode = ft.ThemeMode.LIGHT # Mettiamo come predefinito sfondo chiaro
        # Controller
        self.__controller = None # Quando si preme -> manda il mess al controller
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page
        self._dd_language = None
        self._dd_modality = None
        self._txt_input = None
        self._btn_spell_check = None
        self._lv_output = None

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        row0 = ft.Row(
            spacing=30,
            controls=[self.__theme_switch, self.__title],
            alignment=ft.MainAxisAlignment.START # Mette tutti gli elementi uno vicino all'altro senza spazi
        )
        # --- RIGA 1: Dropdown Lingua ---
        """ 
        ft.Dropdown -> crea menù a tendina
            .option -> inserisco le opzioni all'interno del menù
        label -> quello che c'è scritto quando non selezioni 
        expand = True -> di espande fino alla fine dello schermo il menù
        width = valore -> ferma prima il menù a tendina in base al valore
        .ElevatedButton -> crea bottone 
        """
        self._dd_language = ft.Dropdown(
            label="Seleziona Lingua",
            expand=True,
            options=[
                ft.dropdown.Option("italian", "Italiano"),
                ft.dropdown.Option("english", "Inglese"),
                ft.dropdown.Option("spanish", "Spagnolo"),
            ],
            # Qui diciamo alla View di chiamare il controller quando cambia lingua
            on_change=self.__controller.handle_language_change
        )
        """ Inseriamo sulla riga 1 """
        row1 = ft.Row([self._dd_language], alignment=ft.MainAxisAlignment.START)

        # --- RIGA 2: Ricerca + Input + Bottone ---
        self._dd_modality = ft.Dropdown(
            label="Ricerca",
            width=200,
            options=[
                ft.dropdown.Option("contains", "Contains"),
                ft.dropdown.Option("linear", "Linear"),
                ft.dropdown.Option("dicotomic", "Dicotomica"),
            ]
        )

        self._txt_input = ft.TextField(label="Frase da controllare", expand=True)

        self._btn_spell_check = ft.ElevatedButton( # RICORDA
            text="Spell Check",
            on_click=self.__controller.handle_spell_check
        )

        """ Inseriamo sulla riga 2 """
        row2 = ft.Row([self._dd_modality, self._txt_input, self._btn_spell_check])

        """ --- RIGA 3: Area di Testo (Output) ---"""
        self._lv_output = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        """ --- AGGIUNTA FINALE ALLA PAGINA | INSERIAMO TUTTE LE RIGHE --- """
        # Aggiungiamo tutte le righe create una sotto l'altra
        self.page.add(row0, row1, row2, self._lv_output)

        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
