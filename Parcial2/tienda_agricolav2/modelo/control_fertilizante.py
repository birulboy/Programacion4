from datetime import date
from .producto_control import ProductoControl


class ControlFertilizante(ProductoControl):
    def __init__(self, registro_ica: str, nombre: str, frecuencia_aplicacion: int,
                 valor: float, ultima_aplicacion: date):
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, valor)
        self._ultima_aplicacion = ultima_aplicacion

    @property
    def ultima_aplicacion(self) -> date:
        return self._ultima_aplicacion

    def __str__(self) -> str:
        return super().__str__() + f" | Última aplicación: {self._ultima_aplicacion}"
