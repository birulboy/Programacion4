from datetime import date
from modelo import (
    ControlPlagas, ControlFertilizante,
    Antibiotico, Pedido, Cliente
)


def main():
    # --- productos ---
    confidor = ControlPlagas(
        registro_ica="ICA-010",
        nombre="Confidor",
        frecuencia_aplicacion=15,
        valor=80000,
        periodo_carencia=21
    )

    urea = ControlFertilizante(
        registro_ica="ICA-020",
        nombre="Urea 46%",
        frecuencia_aplicacion=30,
        valor=55000,
        ultima_aplicacion=date(2024, 3, 1)
    )

    oxitetraciclina = Antibiotico(
        nombre="Oxitetraciclina",
        dosis=500,
        tipo_animal="bovino",
        precio=120000
    )

    penicilina = Antibiotico(
        nombre="Penicilina G",
        dosis=450,
        tipo_animal="porcino",
        precio=90000
    )

    # --- pedido 1 ---
    pedido1 = Pedido(fecha=date(2024, 4, 10))
    pedido1.agregar_producto(confidor)
    pedido1.agregar_producto(urea)

    # --- pedido 2 ---
    pedido2 = Pedido(fecha=date(2024, 5, 2))
    pedido2.agregar_producto(oxitetraciclina)
    pedido2.agregar_producto(penicilina)

    # --- cliente con historial de pedidos ---
    cliente = Cliente(nombre="Juan Pérez", cedula="1234567890")
    cliente.agregar_pedido(pedido1)
    cliente.agregar_pedido(pedido2)

    # --- salida ---
    print("=" * 55)
    print(cliente)
    print("=" * 55)

    for i, pedido in enumerate(cliente.historial, start=1):
        print(f"\nPedido #{i}")
        print(pedido)

    print(f"\nTotal histórico del cliente: ${cliente.total_compras():,.0f}")


if __name__ == "__main__":
    main()