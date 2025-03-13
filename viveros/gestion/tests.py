from django.test import TestCase
from gestion.models import Productor, Finca, Vivero, Labor, ProductoControlHongo, ProductoControlPlaga, ProductoControlFertilizante
from django.utils import timezone

class ProductorTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            documento="123456789",
            nombre="Juan",
            apellido="Pérez",
            telefono="3001234567",
            correo="juan@example.com"
        )
    
    def test_productor_creacion(self):
        self.assertEqual(self.productor.nombre, "Juan")
    
    def test_productor_str(self):
        self.assertEqual(str(self.productor), "Juan Pérez")

class FincaTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            documento="123456789",
            nombre="María",
            apellido="Gómez",
            telefono="3009876543",
            correo="maria@example.com"
        )
        self.finca = Finca.objects.create(
            productor=self.productor,
            numero_catastro="00112233",
            municipio="Medellín"
        )
    
    def test_finca_creacion(self):
        self.assertEqual(self.finca.municipio, "Medellín")
    
    def test_finca_relacion_productor(self):
        self.assertEqual(self.finca.productor.nombre, "María")

class ViveroTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            documento="987654321",
            nombre="Carlos",
            apellido="López",
            telefono="3112233445",
            correo="carlos@example.com"
        )
        self.finca = Finca.objects.create(
            productor=self.productor,
            numero_catastro="44556677",
            municipio="Bogotá"
        )
        self.vivero = Vivero.objects.create(
            finca=self.finca,
            codigo="VIV001",
            tipo_cultivo="Café"
        )
    
    def test_vivero_creacion(self):
        self.assertEqual(self.vivero.tipo_cultivo, "Café")
    
    def test_vivero_relacion_finca(self):
        self.assertEqual(self.vivero.finca.numero_catastro, "44556677")

class LaborTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            documento="555555555",
            nombre="Ana",
            apellido="Martínez",
            telefono="3223344556",
            correo="ana@example.com"
        )
        self.finca = Finca.objects.create(
            productor=self.productor,
            numero_catastro="77889900",
            municipio="Cali"
        )
        self.vivero = Vivero.objects.create(
            finca=self.finca,
            codigo="VIV002",
            tipo_cultivo="Tomate"
        )
        self.labor = Labor.objects.create(
            vivero=self.vivero,
            fecha=timezone.now(),
            descripcion="Aplicación de fertilizante"
        )
    
    def test_labor_creacion(self):
        self.assertEqual(self.labor.descripcion, "Aplicación de fertilizante")
    
    def test_labor_relacion_vivero(self):
        self.assertEqual(self.labor.vivero.tipo_cultivo, "Tomate")

class ProductoControlTestCase(TestCase):
    def setUp(self):
        self.hongo = ProductoControlHongo.objects.create(
            registro_ICA="ICA001",
            nombre_producto="Fungicida X",
            frecuencia_aplicacion=15,
            valor=50000,
            periodo_carencia=10,
            nombre_hongo="Botrytis"
        )
        self.plaga = ProductoControlPlaga.objects.create(
            registro_ICA="ICA002",
            nombre_producto="Insecticida Y",
            frecuencia_aplicacion=20,
            valor=60000,
            periodo_carencia=12
        )
        self.fertilizante = ProductoControlFertilizante.objects.create(
            registro_ICA="ICA003",
            nombre_producto="Fertilizante Z",
            frecuencia_aplicacion=30,
            valor=40000,
            fecha_ultima_aplicacion=timezone.now()
        )
    
    def test_producto_hongo_creacion(self):
        self.assertEqual(self.hongo.nombre_producto, "Fungicida X")
    
    def test_producto_plaga_creacion(self):
        self.assertEqual(self.plaga.periodo_carencia, 12)
    
    def test_producto_fertilizante_creacion(self):
        self.assertEqual(self.fertilizante.valor, 40000)
