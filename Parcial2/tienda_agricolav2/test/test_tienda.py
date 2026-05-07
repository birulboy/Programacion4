import unittest
from datetime import date
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from modelo import (
    ProductoControl, ControlPlagas, ControlFertilizante,
    Antibiotico, Pedido, Cliente
)
from crud import TiendaCrud


class TestProductoControl(unittest.TestCase):

    def test_creacion_basica(self):
        p = ProductoControl("ICA-001", "Roundup", 30, 45000)
        self.assertEqual(p.registro_ica, "ICA-001")
        self.assertEqual(p.nombre, "Roundup")
        self.assertEqual(p.frecuencia_aplicacion, 30)
        self.assertEqual(p.valor, 45000)

    def test_str_contiene_nombre(self):
        p = ProductoControl("ICA-002", "Glifosato", 15, 32000)
        self.assertIn("Glifosato", str(p))


class TestControlPlagas(unittest.TestCase):

    def setUp(self):
        self.cp = ControlPlagas("ICA-010", "Confidor", 15, 80000, 21)

    def test_hereda_de_producto_control(self):
        self.assertIsInstance(self.cp, ProductoControl)

    def test_periodo_carencia(self):
        self.assertEqual(self.cp.periodo_carencia, 21)

    def test_str_incluye_carencia(self):
        self.assertIn("21", str(self.cp))


class TestControlFertilizante(unittest.TestCase):

    def setUp(self):
        self.fecha = date(2024, 3, 1)
        self.cf = ControlFertilizante("ICA-020", "Urea 46%", 30, 55000, self.fecha)

    def test_hereda_de_producto_control(self):
        self.assertIsInstance(self.cf, ProductoControl)

    def test_ultima_aplicacion(self):
        self.assertEqual(self.cf.ultima_aplicacion, self.fecha)

    def test_str_incluye_fecha(self):
        self.assertIn("2024-03-01", str(self.cf))


class TestAntibiotico(unittest.TestCase):

    def test_creacion_valida(self):
        ab = Antibiotico("Oxitetraciclina", 500, "bovino", 120000)
        self.assertEqual(ab.nombre, "Oxitetraciclina")
        self.assertEqual(ab.dosis, 500)
        self.assertEqual(ab.tipo_animal, "bovino")

    def test_dosis_fuera_de_rango_lanza_error(self):
        with self.assertRaises(ValueError):
            Antibiotico("X", 200, "bovino", 50000)

    def test_animal_invalido_lanza_error(self):
        with self.assertRaises(ValueError):
            Antibiotico("X", 450, "perro", 50000)

    def test_tipo_animal_normalizado_a_minusculas(self):
        ab = Antibiotico("Penicilina", 450, "Porcino", 90000)
        self.assertEqual(ab.tipo_animal, "porcino")


class TestPedido(unittest.TestCase):

    def setUp(self):
        self.pedido = Pedido(date(2024, 4, 10))
        self.cp = ControlPlagas("ICA-010", "Confidor", 15, 80000, 21)
        self.ab = Antibiotico("Oxitetraciclina", 500, "bovino", 120000)

    def test_agregar_productos(self):
        self.pedido.agregar_producto(self.cp)
        self.pedido.agregar_producto(self.ab)
        self.assertEqual(len(self.pedido.productos), 2)

    def test_calcular_total(self):
        self.pedido.agregar_producto(self.cp)
        self.pedido.agregar_producto(self.ab)
        self.assertEqual(self.pedido.calcular_total(), 200000)

    def test_pedido_vacio_total_cero(self):
        self.assertEqual(self.pedido.calcular_total(), 0)


class TestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Juan Pérez", "1234567890")

        pedido1 = Pedido(date(2024, 1, 15))
        pedido1.agregar_producto(ControlPlagas("ICA-001", "Confidor", 15, 80000, 21))

        pedido2 = Pedido(date(2024, 3, 20))
        pedido2.agregar_producto(Antibiotico("Oxitetraciclina", 500, "bovino", 120000))

        self.cliente.agregar_pedido(pedido1)
        self.cliente.agregar_pedido(pedido2)

    def test_historial_tiene_dos_pedidos(self):
        self.assertEqual(len(self.cliente.historial), 2)

    def test_total_compras(self):
        self.assertEqual(self.cliente.total_compras(), 200000)

    def test_cedula(self):
        self.assertEqual(self.cliente.cedula, "1234567890")

    def test_historial_es_copia(self):
        self.cliente.historial.clear()
        self.assertEqual(len(self.cliente.historial), 2)


class TestTiendaCrud(unittest.TestCase):

    def setUp(self):
        self.crud = TiendaCrud()
        self.crud.registrar_cliente("María López", "9876543210")

    def test_registrar_cliente(self):
        cliente = self.crud.buscar_por_cedula("9876543210")
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.nombre, "María López")

    def test_cedula_duplicada_lanza_error(self):
        with self.assertRaises(ValueError):
            self.crud.registrar_cliente("Otro", "9876543210")

    def test_buscar_cedula_inexistente_retorna_none(self):
        resultado = self.crud.buscar_por_cedula("0000000000")
        self.assertIsNone(resultado)

    def test_registrar_pedido_asocia_al_cliente(self):
        cp = self.crud.crear_control_plagas("ICA-010", "Confidor", 15, 80000, 21)
        self.crud.registrar_pedido("9876543210", [cp])
        cliente = self.crud.buscar_por_cedula("9876543210")
        self.assertEqual(len(cliente.historial), 1)

    def test_pedido_sin_productos_lanza_error(self):
        with self.assertRaises(ValueError):
            self.crud.registrar_pedido("9876543210", [])

    def test_pedido_cliente_inexistente_lanza_error(self):
        with self.assertRaises(ValueError):
            self.crud.registrar_pedido("0000000000", [])

    def test_crear_antibiotico_dosis_invalida(self):
        with self.assertRaises(ValueError):
            self.crud.crear_antibiotico("X", 100, "bovino", 50000)

    def test_listar_clientes(self):
        self.crud.registrar_cliente("Pedro Gómez", "1111111111")
        self.assertEqual(len(self.crud.listar_clientes()), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
