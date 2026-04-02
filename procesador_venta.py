from datetime import datetime
 
 
class ProcesadorVenta:
    def __init__(self):
        self._ventas = []
 
    def generar_tiquete(self, estudiante, plato):
        precio_base = plato.precio
        total       = estudiante.precio_final(precio_base)
        descuento   = estudiante.calcular_descuento(precio_base)
 
        tiquete = {
            "id_estudiante": estudiante.id_estudiante,
            "nombre":        estudiante.nombre,
            "plato":         plato.nombre,
            "precio_base":   precio_base,
            "descuento":     descuento,
            "total":         total,
            "hora":          datetime.now().strftime("%H:%M:%S"),
        }
 
        self._ventas.append(tiquete)
        self._imprimir_tiquete(tiquete)
        return tiquete
 
    def _imprimir_tiquete(self, tiquete):
        print("\n" + "=" * 42)
        print("          CAFETERÍA NutriUTP")
        print("=" * 42)
        print(f"  Hora       : {tiquete['hora']}")
        print(f"  Estudiante : {tiquete['nombre']} ({tiquete['id_estudiante']})")
        print(f"  Plato      : {tiquete['plato']}")
        print(f"  Precio base: ${tiquete['precio_base']:>10,.0f}")
        print(f"  Descuento  : ${tiquete['descuento']:>10,.0f}")
        print(f"  TOTAL      : ${tiquete['total']:>10,.0f}")
        print("=" * 42)
 
    def validar_pago(self, total):
        # Punto de integración con el sistema de tesorería de la UTP
        print(f"  [Tesorería] Pago de ${total:,.0f} aprobado.\n")
        return True
 
    def reporte_cierre(self):
        if not self._ventas:
            print("No hay ventas registradas.")
            return
 
        total_recaudado = sum(v["total"] for v in self._ventas)
 
        print("\n" + "=" * 42)
        print("          REPORTE DE CIERRE")
        print("=" * 42)
        for v in self._ventas:
            print(f"  {v['nombre']:<22} ${v['total']:>8,.0f}")
        print("-" * 42)
        print(f"  {'TOTAL RECAUDADO':<22} ${total_recaudado:>8,.0f}")
        print("=" * 42)
 