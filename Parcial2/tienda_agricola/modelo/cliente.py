from .pedido import Pedido


class Cliente:
    def __init__(self, nombre: str, cedula: str):
        self._nombre = nombre
        self._cedula = cedula
        # un cliente puede tener muchos pedidos asociados
        self._historial: list[Pedido] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def cedula(self) -> str:
        return self._cedula

    @property
    def historial(self) -> list[Pedido]:
        return list(self._historial)

    def agregar_pedido(self, pedido: Pedido) -> None:
        self._historial.append(pedido)

    def total_compras(self) -> float:
        return sum(p.calcular_total() for p in self._historial)

    def __str__(self) -> str:
        return (f"Cliente: {self._nombre} | Cédula: {self._cedula} | "
                f"Pedidos: {len(self._historial)}")
