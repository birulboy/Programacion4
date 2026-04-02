from datetime import date

# Mapeo necesario porque Python usa inglés para los días
DIAS_SEMANA = {
    0: "lunes",
    1: "martes",
    2: "miercoles",
    3: "jueves",
    4: "viernes",
    5: "sabado",
    6: "domingo",
}


class GestorMenus:
    def __init__(self):
        self._menus = {}

    def registrar_menu(self, dia_semana, menu):
        self._menus[dia_semana.lower()] = menu

    def menu_de_hoy(self):
        dia_hoy = DIAS_SEMANA[date.today().weekday()]
        menu = self._menus.get(dia_hoy)

        if menu is None:
            print(f"No hay menú registrado para el {dia_hoy}.")

        return menu