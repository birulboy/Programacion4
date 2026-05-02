from .producto_control import ProductoControl


class ControlPlagas(ProductoControl):
    def __init__(self, registro_ica: str, nombre: str, frecuencia_aplicacion: int,
                 valor: float, periodo_carencia: int):
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, valor)
        # días que deben pasar entre última aplicación y la cosecha
        self._periodo_carencia = periodo_carencia

    @property
    def periodo_carencia(self) -> int:
        return self._periodo_carencia

    def __str__(self) -> str:
        return super().__str__() + f" | Carencia: {self._periodo_carencia} días"
