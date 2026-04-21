class MenuDia:
    def __init__(self, fecha):
        self.fecha = fecha
        self._opciones = []

    def agregar_plato(self, plato):
        self._opciones.append(plato)

    def mostrar_menu(self):
        print(f"\n=== Menú del {self.fecha} ===")
        for i, plato in enumerate(self._opciones, start=1):
            print(f"  {i}. {plato.descripcion_detallada()}")

    def seleccionar_opcion(self, tipo_preferencia):
        es_vegetariano = tipo_preferencia == "vegetariano"
        return self._aislar_seleccion(es_vegetariano)

    def _aislar_seleccion(self, vegetariano):
        # Si mañana _opciones cambia a un dict o BD, solo se toca aquí
        return [p for p in self._opciones if p.es_vegetariano == vegetariano]

    def seleccionar_por_numero(self, opciones, numero):
        indice = numero - 1
        if 0 <= indice < len(opciones):
            return opciones[indice]
        return None