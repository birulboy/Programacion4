ANIMALES_VALIDOS = {"bovino", "caprino", "porcino"}

DOSIS_MIN = 400
DOSIS_MAX = 600


class Antibiotico:
    def __init__(self, nombre: str, dosis: float, tipo_animal: str, precio: float):
        if not (DOSIS_MIN <= dosis <= DOSIS_MAX):
            raise ValueError(f"La dosis debe estar entre {DOSIS_MIN}Kg y {DOSIS_MAX}Kg.")

        if tipo_animal.lower() not in ANIMALES_VALIDOS:
            raise ValueError(f"Tipo de animal inválido. Opciones: {ANIMALES_VALIDOS}")

        self._nombre = nombre
        self._dosis = dosis
        self._tipo_animal = tipo_animal.lower()
        self._precio = precio

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def dosis(self) -> float:
        return self._dosis

    @property
    def tipo_animal(self) -> str:
        return self._tipo_animal

    @property
    def precio(self) -> float:
        return self._precio

    def __str__(self) -> str:
        return (f"[Antibiótico] {self._nombre} | Animal: {self._tipo_animal} | "
                f"Dosis: {self._dosis}Kg | Precio: ${self._precio:,.0f}")
