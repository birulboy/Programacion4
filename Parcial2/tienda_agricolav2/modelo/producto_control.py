class ProductoControl:
    def __init__(self, registro_ica: str, nombre: str, frecuencia_aplicacion: int, valor: float):
        self._registro_ica = registro_ica
        self._nombre = nombre
        # frecuencia en días (ej: 15, 30)
        self._frecuencia_aplicacion = frecuencia_aplicacion
        self._valor = valor

    @property
    def registro_ica(self) -> str:
        return self._registro_ica

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def frecuencia_aplicacion(self) -> int:
        return self._frecuencia_aplicacion

    @property
    def valor(self) -> float:
        return self._valor

    def __str__(self) -> str:
        return (f"[{self.__class__.__name__}] {self._nombre} | "
                f"ICA: {self._registro_ica} | Frecuencia: {self._frecuencia_aplicacion} días | "
                f"Valor: ${self._valor:,.0f}")
