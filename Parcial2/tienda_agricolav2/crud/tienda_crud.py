from modelo import Cliente, Pedido, ControlPlagas, ControlFertilizante, Antibiotico
from datetime import date


class TiendaCrud:
    def __init__(self):
        # lista principal de clientes registrados en el sistema
        self._clientes: list[Cliente] = []

    def registrar_cliente(self, nombre: str, cedula: str) -> Cliente:
        if self.buscar_por_cedula(cedula):
            raise ValueError(f"Ya existe un cliente con cédula {cedula}.")
        cliente = Cliente(nombre, cedula)
        self._clientes.append(cliente)
        return cliente

    def buscar_por_cedula(self, cedula: str) -> Cliente | None:
        for cliente in self._clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    def registrar_pedido(self, cedula: str, productos: list) -> Pedido:
        cliente = self.buscar_por_cedula(cedula)
        if not cliente:
            raise ValueError(f"No existe un cliente con cédula {cedula}.")
        if not productos:
            raise ValueError("El pedido debe tener al menos un producto.")

        pedido = Pedido(date.today())
        for producto in productos:
            pedido.agregar_producto(producto)

        cliente.agregar_pedido(pedido)
        return pedido

    def listar_clientes(self) -> list[Cliente]:
        return list(self._clientes)

    def crear_control_plagas(self, registro_ica: str, nombre: str,
                              frecuencia: int, valor: float, carencia: int) -> ControlPlagas:
        return ControlPlagas(registro_ica, nombre, frecuencia, valor, carencia)

    def crear_control_fertilizante(self, registro_ica: str, nombre: str,
                                    frecuencia: int, valor: float,
                                    ultima_aplicacion: date) -> ControlFertilizante:
        return ControlFertilizante(registro_ica, nombre, frecuencia, valor, ultima_aplicacion)

    def crear_antibiotico(self, nombre: str, dosis: float,
                           tipo_animal: str, precio: float) -> Antibiotico:
        # la validación de dosis y animal la hace el constructor de Antibiotico
        return Antibiotico(nombre, dosis, tipo_animal, precio)
