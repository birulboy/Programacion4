# Definidos aquí para que un cambio de política universitaria no toque la clase
DESCUENTOS = {
    ("estudiante", "subsidiado_alto"):0.5,
    ("estudiante", "subsidiado_medio"):0.3,
    
    ("administrativo","subsidiado_alto"):0.3,
    ("administrativo","subsidiado_medio"):0.1,
    
    ("particular", "subsidiado_alto"):0.1,
    ("particular", "subsidiado_medio"):0.0,
}


class Comensal:
    def __init__(self, id_cliente, nombre, _tipo_subsidio, _tipo_cliente):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._tipo_subsidio = _tipo_subsidio
        self._tipo_cliente = _tipo_cliente

    def calcular_descuento(self, valor_plato):
        porcentaje = DESCUENTOS.get((self._tipo_cliente, self._tipo_subsidio), 0.0)
        return valor_plato * porcentaje

    def precio_final(self, valor_plato):
        return valor_plato - self.calcular_descuento(valor_plato)
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def id_cliente(self):
        return self._id_cliente