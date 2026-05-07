from datetime import date


class Pedido:
    def __init__(self, fecha: date):
        self._fecha = fecha
        # un pedido puede tener muchos productos (ProductoControl o Antibiotico)
        self._productos: list = []

    @property
    def fecha(self) -> date:
        return self._fecha

    @property
    def productos(self) -> list:
        return list(self._productos)

    def agregar_producto(self, producto) -> None:
        self._productos.append(producto)

    def calcular_total(self) -> float:
        total = 0.0
        for p in self._productos:
            # tanto ProductoControl como Antibiotico exponen su precio con atributos distintos
            if hasattr(p, "valor"):
                total += p.valor
            elif hasattr(p, "precio"):
                total += p.precio
        return total

    def __str__(self) -> str:
        lineas = [f"Pedido del {self._fecha} | Total: ${self.calcular_total():,.0f}"]
        for p in self._productos:
            lineas.append(f"  - {p}")
        return "\n".join(lineas)
