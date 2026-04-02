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
 
    def seleccionar_por_numero(self, numero):
        indice = numero - 1
        if 0 <= indice < len(self._opciones):
            return self._opciones[indice]
        return None