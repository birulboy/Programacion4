class Plato:
    def __init__(self, nombre, precio_base, es_vegetariano=False):
        self.nombre = nombre
        self._precio_base = precio_base
        self.es_vegetariano = es_vegetariano
    @property
    def precio(self):
        return self._precio_base
 
    def descripcion_detallada(self):
        tipo = "Vegetariano" if self.es_vegetariano else "Estándar"
        return f"{self.nombre} ({tipo}) - ${self._precio_base:,.0f}"
 