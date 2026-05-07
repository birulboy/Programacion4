from crud import TiendaCrud
from datetime import date


def mostrar_menu():
    print("\n╔══════════════════════════════════╗")
    print("║      TIENDA AGRÍCOLA             ║")
    print("╠══════════════════════════════════╣")
    print("║  1. Registrar cliente            ║")
    print("║  2. Registrar pedido             ║")
    print("║  3. Buscar cliente por cédula    ║")
    print("║  4. Listar clientes              ║")
    print("║  0. Salir                        ║")
    print("╚══════════════════════════════════╝")


def menu_productos(crud: TiendaCrud) -> list:
    productos = []
    while True:
        print("\n  Tipo de producto:")
        print("  1. Control de Plagas")
        print("  2. Control de Fertilizante")
        print("  3. Antibiótico")
        print("  0. Terminar y confirmar pedido")

        opcion = input("  Opción: ").strip()

        if opcion == "0":
            break

        elif opcion == "1":
            try:
                registro = input("  Registro ICA: ").strip()
                nombre = input("  Nombre: ").strip()
                frecuencia = int(input("  Frecuencia de aplicación (días): "))
                valor = float(input("  Valor: "))
                carencia = int(input("  Periodo de carencia (días): "))
                p = crud.crear_control_plagas(registro, nombre, frecuencia, valor, carencia)
                productos.append(p)
                print(f"  ✔ Producto agregado: {p}")
            except ValueError as e:
                print(f"  ✘ Error: {e}")

        elif opcion == "2":
            try:
                registro = input("  Registro ICA: ").strip()
                nombre = input("  Nombre: ").strip()
                frecuencia = int(input("  Frecuencia de aplicación (días): "))
                valor = float(input("  Valor: "))
                texto_fecha = input("  Última aplicación (AAAA-MM-DD): ").strip()
                ultima = date.fromisoformat(texto_fecha)
                p = crud.crear_control_fertilizante(registro, nombre, frecuencia, valor, ultima)
                productos.append(p)
                print(f"  ✔ Producto agregado: {p}")
            except ValueError as e:
                print(f"  ✘ Error: {e}")

        elif opcion == "3":
            try:
                nombre = input("  Nombre: ").strip()
                dosis = float(input("  Dosis (400-600 Kg): "))
                tipo = input("  Tipo de animal (bovino/caprino/porcino): ").strip()
                precio = float(input("  Precio: "))
                p = crud.crear_antibiotico(nombre, dosis, tipo, precio)
                productos.append(p)
                print(f"  ✔ Producto agregado: {p}")
            except ValueError as e:
                print(f"  ✘ Error: {e}")

        else:
            print("  ✘ Opción inválida.")

    return productos


def flujo_registrar_cliente(crud: TiendaCrud):
    print("\n── Registrar Cliente ──")
    nombre = input("Nombre: ").strip()
    cedula = input("Cédula: ").strip()
    try:
        cliente = crud.registrar_cliente(nombre, cedula)
        print(f"✔ Cliente registrado: {cliente}")
    except ValueError as e:
        print(f"✘ Error: {e}")


def flujo_registrar_pedido(crud: TiendaCrud):
    print("\n── Registrar Pedido ──")
    cedula = input("Cédula del cliente: ").strip()

    cliente = crud.buscar_por_cedula(cedula)
    if not cliente:
        print("✘ Cliente no encontrado.")
        return

    print(f"Cliente: {cliente.nombre}")
    productos = menu_productos(crud)

    if not productos:
        print("✘ No se agregaron productos. Pedido cancelado.")
        return

    try:
        pedido = crud.registrar_pedido(cedula, productos)
        print(f"\n✔ Pedido registrado | Total: ${pedido.calcular_total():,.0f}")
    except ValueError as e:
        print(f"✘ Error: {e}")


def flujo_buscar_por_cedula(crud: TiendaCrud):
    print("\n── Buscar por Cédula ──")
    cedula = input("Cédula: ").strip()

    cliente = crud.buscar_por_cedula(cedula)
    if not cliente:
        print("✘ Cliente no encontrado.")
        return

    print(f"\n{cliente}")
    print(f"Total histórico: ${cliente.total_compras():,.0f}")

    if not cliente.historial:
        print("  Sin pedidos registrados.")
        return

    for i, pedido in enumerate(cliente.historial, start=1):
        print(f"\n  Pedido #{i} — {pedido.fecha} | Total: ${pedido.calcular_total():,.0f}")
        for producto in pedido.productos:
            print(f"    - {producto}")


def flujo_listar_clientes(crud: TiendaCrud):
    print("\n── Clientes Registrados ──")
    clientes = crud.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return
    for c in clientes:
        print(f"  {c}")


def iniciar(crud: TiendaCrud):
    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            flujo_registrar_cliente(crud)
        elif opcion == "2":
            flujo_registrar_pedido(crud)
        elif opcion == "3":
            flujo_buscar_por_cedula(crud)
        elif opcion == "4":
            flujo_listar_clientes(crud)
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("✘ Opción inválida.")
