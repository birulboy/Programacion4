# Definidos aquí para que un cambio de política universitaria no toque la clase
DESCUENTOS = {
    "subsidiado_alto":  0.70,
    "subsidiado_medio": 0.40,
    "administrativo":   0.10,
    "particular":       0.00,
    "estudiante":      0.05,
}


class Comensal:
    def __init__(self, id_estudiante, nombre, _tipo_subsidio):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self._tipo_subsidio = _tipo_subsidio

    def calcular_descuento(self, valor_plato):
        porcentaje = DESCUENTOS.get(self._tipo_subsidio, 0.0)
        return valor_plato * porcentaje

    def precio_final(self, valor_plato):
        return valor_plato - self.calcular_descuento(valor_plato)