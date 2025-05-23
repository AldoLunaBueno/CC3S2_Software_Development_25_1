# src/factories.py
import factory
from src.carrito import Producto


class ProductoFactory(factory.Factory):
    class Meta:
        model = Producto

    nombre = factory.Faker("word")
    precio = factory.Faker("pyfloat",
                           left_digits=2, right_digits=2, positive=True)
    stock = 10000000  # para que no interfiera por limitaciones de stock
