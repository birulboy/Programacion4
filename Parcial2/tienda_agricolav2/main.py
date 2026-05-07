from crud import TiendaCrud
from ui import iniciar
from datetime import date


def precargar_datos(crud: TiendaCrud):
    # clientes
    crud.registrar_cliente("Juan Pérez", "1234567890")
    crud.registrar_cliente("María López", "9876543210")

    # productos pedido 1
    confidor = crud.crear_control_plagas("ICA-010", "Confidor", 15, 80000, 21)
    urea = crud.crear_control_fertilizante("ICA-020", "Urea 46%", 30, 55000, date(2024, 3, 1))

    # productos pedido 2
    oxitetraciclina = crud.crear_antibiotico("Oxitetraciclina", 500, "bovino", 120000)
    penicilina = crud.crear_antibiotico("Penicilina G", 450, "porcino", 90000)

    # productos pedido 3
    glifosato = crud.crear_control_plagas("ICA-030", "Glifosato", 30, 32000, 14)

    # pedidos juan
    crud.registrar_pedido("1234567890", [confidor, urea])
    crud.registrar_pedido("1234567890", [oxitetraciclina, penicilina])

    # pedido maria
    crud.registrar_pedido("9876543210", [glifosato])


def main():
    crud = TiendaCrud()
    precargar_datos(crud)  # ← pon el breakpoint aquí para el debug
    iniciar(crud)


if __name__ == "__main__":
    main()
