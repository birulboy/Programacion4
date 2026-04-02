from plato import Plato
from menu_dia import MenuDia
from comensal import Comensal
from procesador_venta import ProcesadorVenta
from gestor_menus import GestorMenus
from comensal import DESCUENTOS


def configurar_menus():
    gestor = GestorMenus()

    lunes = MenuDia("lunes")
    lunes.agregar_plato(Plato("Bandeja Paisa",      12000))
    lunes.agregar_plato(Plato("Lentejas con arroz", 10000, es_vegetariano=True))

    martes = MenuDia("martes")
    martes.agregar_plato(Plato("Sudado de pollo",   11500))
    martes.agregar_plato(Plato("Pasta primavera",    9000, es_vegetariano=True))

    miercoles = MenuDia("miercoles")
    miercoles.agregar_plato(Plato("Sancocho",        11000))
    miercoles.agregar_plato(Plato("Arroz con tofu",   9500, es_vegetariano=True))

    jueves = MenuDia("jueves")
    jueves.agregar_plato(Plato("Cazuela de res",     12500))
    jueves.agregar_plato(Plato("Sopa de verduras",    8500, es_vegetariano=True))

    viernes = MenuDia("viernes")
    viernes.agregar_plato(Plato("Trucha asada",      13000))
    viernes.agregar_plato(Plato("Ensalada proteica",  9000, es_vegetariano=True))

    gestor.registrar_menu("lunes",     lunes)
    gestor.registrar_menu("martes",    martes)
    gestor.registrar_menu("miercoles", miercoles)
    gestor.registrar_menu("jueves",    jueves)
    gestor.registrar_menu("viernes",   viernes)

    return gestor


def seleccionar_menu(gestor):
    print("\n¿Cómo deseas seleccionar el menú?")
    print("  1. Menú de hoy (automático)")
    print("  2. Elegir día manualmente")

    while True:
        opcion = input("  Opción (1/2): ").strip()
        if opcion == "1":
            return gestor.menu_de_hoy()
        elif opcion == "2":
            dia  = input("  Ingresa el día (lunes, martes, ...): ").strip()
            menu = gestor.menu_por_dia(dia)
            if menu:
                return menu
        else:
            print("  Opción inválida, intenta de nuevo.")


def pedir_datos_estudiante():
    print("\n--- Datos del estudiante ---")
    id_estudiante = input("  ID          : ").strip()
    nombre        = input("  Nombre      : ").strip()

    tipos_validos = list(DESCUENTOS.keys())
    print(f"  Tipos de subsidio: {', '.join(tipos_validos)}")
    while True:
        tipo = input("  Tipo subsidio: ").strip().lower()
        if tipo in tipos_validos:
            break
        print(f"  Tipo inválido. Opciones: {', '.join(tipos_validos)}")

    return Comensal(id_estudiante, nombre, tipo)


def pedir_seleccion_plato(menu):
    while True:
        preferencia = input("\n  Preferencia (estandar/vegetariano): ").strip().lower()
        if preferencia in ("estandar", "vegetariano"):
            break
        print("  Preferencia inválida, intenta de nuevo.")

    opciones = menu.seleccionar_opcion(preferencia)

    if not opciones:
        print("  No hay platos disponibles para esa preferencia.")
        return None

    print(f"\n  --- Opciones {preferencia} ---")
    for i, plato in enumerate(opciones, start=1):
        print(f"  {i}. {plato.descripcion_detallada()}")

    while True:
        try:
            numero = int(input("\n  Elige tu plato (número): "))
            plato  = menu.seleccionar_por_numero(opciones, numero)
            if plato:
                return plato
            print("  Número fuera de rango, intenta de nuevo.")
        except ValueError:
            print("  Ingresa un número válido.")


def main():
    gestor = configurar_menus()
    menu   = seleccionar_menu(gestor)

    if menu is None:
        return

    procesador = ProcesadorVenta()

    while True:
        menu.mostrar_menu()

        estudiante = pedir_datos_estudiante()
        plato      = pedir_seleccion_plato(menu)

        if plato is None:
            continue

        tiquete = procesador.generar_tiquete(estudiante, plato)
        procesador.validar_pago(tiquete["total"])

        otro = input("¿Atender otro estudiante? (s/n): ").strip().lower()
        if otro != "s":
            break

    procesador.reporte_cierre()


if __name__ == "__main__":
    main()