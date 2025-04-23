# tests/test_carrito.py

import pytest
from src.carrito import Carrito, ItemCarrito
from src.factories import ProductoFactory
from typing import List



def test_agregar_producto_nuevo():
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item
        con el producto y cantidad 1.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=1000.00)

    # Act
    carrito.agregar_producto(producto)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Mouse", precio=50.00)
    carrito.agregar_producto(producto, cantidad=1)

    # Act
    carrito.agregar_producto(producto, cantidad=2)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Teclado", precio=75.00)
    carrito.agregar_producto(producto, cantidad=3)

    # Act
    carrito.remover_producto(producto, cantidad=1)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Monitor", precio=300.00)
    carrito.agregar_producto(producto, cantidad=2)

    # Act
    carrito.remover_producto(producto, cantidad=2)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_actualizar_cantidad_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Auriculares", precio=150.00)
    carrito.agregar_producto(producto, cantidad=1)

    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=5)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Cargador", precio=25.00)
    carrito.agregar_producto(producto, cantidad=3)

    # Act
    carrito.actualizar_cantidad(producto, nueva_cantidad=0)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos
        con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta
        de cada item (precio * cantidad).
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Impresora", precio=200.00)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150

    # Act
    total = carrito.calcular_total()

    # Assert
    assert total == 550.00


def test_aplicar_descuento():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto
    con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Tablet", precio=500.00)
    carrito.agregar_producto(producto, cantidad=2)  # Total 1000

    # Act
    total_con_descuento = carrito.aplicar_descuento(10)

    # Assert
    assert total_con_descuento == 900.00


def test_aplicar_descuento_limites():
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento
    fuera del rango [0, 100] genere un error.
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Smartphone", precio=800.00)
    carrito.agregar_producto(producto, cantidad=1)

    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)


def test_vaciar_carrito():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan algunos items
    Act: Se vacía el carrito
    Assert: Se verifica que no hay productos en el carrito
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Smartphone", precio=800.00)
    carrito.agregar_producto(producto1, cantidad=1)
    producto2 = ProductoFactory(nombre="Dishwasher", precio=300.00)
    carrito.agregar_producto(producto2, cantidad=2)

    # Act
    carrito.vaciar()

    # Assert
    assert carrito.contar_items() == 0
    assert carrito.calcular_total() == 0


def test_descuento_condicional_si_aplicar():
    """
    AAA:
    Arrange: Se crea un carrito, se agregan algunos items
        que sumen un monto total mayor a un mínimo,
        y se establecen el porcentaje y el valor mínimo.
    Act: Se llama al método del descuento condicional.
    Assert: Se verifica que el descuento condicional fue aplicado.
    """
    # Arrange
    carrito = Carrito()
    precio1 = 800.0
    precio2 = 300.0
    producto1 = ProductoFactory(nombre="A", precio=precio1)
    carrito.agregar_producto(producto1, cantidad=1)
    producto2 = ProductoFactory(nombre="B", precio=precio2)
    carrito.agregar_producto(producto2, cantidad=1)
    total = precio1 + precio2
    porcentaje = 15
    minimo = 1000

    # Act
    total_descontado = carrito.aplicar_descuento_condicional(
        porcentaje, minimo)

    # Assert
    assert total_descontado == total - total * porcentaje / 100


def test_descuento_condicional_no_aplicar():
    """
    AAA:
    Arrange: Se crea un carrito, se agregan algunos items
        que sumen un monto total menor o igual a un mínimo,
        y se establecen el porcentaje y el valor mínimo.
    Act: Se llama al método del descuento condicional.
    Assert: Se verifica que el descuento condicional no fue aplicado,
        es decir, que el total sigue siendo el mismo.
    """
    # Arrange
    carrito = Carrito()
    precio1 = 600.0
    precio2 = 300.0
    producto1 = ProductoFactory(nombre="A", precio=precio1)
    carrito.agregar_producto(producto1, cantidad=1)
    producto2 = ProductoFactory(nombre="B", precio=precio2)
    carrito.agregar_producto(producto2, cantidad=1)
    total = precio1 + precio2
    porcentaje = 15
    minimo = 1000

    # Act
    total_descontado = carrito.aplicar_descuento_condicional(
        porcentaje, minimo)

    # Assert
    assert total_descontado == total


def test_agregar_producto_bajo_limite_stock():
    """
    AAA:
    Arrange: Se crea un carrito, se establece un stock y se crea el
        producto con este stock.
    Act y Assert: Se ejecuta el método agregar_producto() agregando
        tantos productos como sea posible según el stock establecido,
        y se verifica que no se lance ninguna excepción en el proceso
        y que al final la cantidad de items en el carrito sea igual
        que el stock establecido en un principio.
    """
    # Arrange
    carrito = Carrito()
    stock1 = 5
    producto1 = ProductoFactory(nombre="A", precio=200.00, stock=stock1)

    # Act y Assert
    try:
        carrito.agregar_producto(producto1, cantidad=2)
        carrito.agregar_producto(producto1, cantidad=2)
        carrito.agregar_producto(producto1, cantidad=1)
        assert carrito.contar_items() == stock1
    except Exception:
        assert False, "Se puede agregar al carrito \
            tantos productos de un mismo tipo como el stock \
            de este producto."


def test_agregar_producto_sobre_limite_stock():
    """
    AAA:
    Arrange: Se crea un carrito, se establece un stock y se crea el
        producto con este stock.
    Act y Assert: Se ejecuta el método agregar_producto() agregando
        más productos de los que son posibles según el stock establecido,
        y se verifica que se lance una excepción cuando esto pase
        y que al final la cantidad de items en el carrito no sea mayor
        que el stock establecido en un principio.
    """
    # Arrange
    carrito = Carrito()
    stock1 = 5
    producto1 = ProductoFactory(nombre="A", precio=200.00, stock=stock1)

    # Act y Assert
    carrito.agregar_producto(producto1, cantidad=2)
    carrito.agregar_producto(producto1, cantidad=2)
    with pytest.raises(Exception):
        carrito.agregar_producto(producto1, cantidad=3)
    assert carrito.contar_items() <= stock1


def test_obtener_items_ordenados_por_nombre():
    """
    AAA:
    Arrange: Se crea un carrito y algunos productos para agregarlos al carrito.
    Act: Se ordenan los items del carrito por precio y se obtiene esta lista.
    Assert: Se verifica que estos items sigan el mismo orden
        en el que se agregaron los productos.
    """
    # Arrange
    carrito = Carrito()
    p1 = ProductoFactory(nombre="Laptop", precio=4)
    p2 = ProductoFactory(nombre="Smartphone", precio=2)
    p3 = ProductoFactory(nombre="Mouse", precio=7)
    p4 = ProductoFactory(nombre="Dishwasher", precio=9)
    p5 = ProductoFactory(nombre="Monitor", precio=3)

    carrito.agregar_producto(producto=p1, cantidad=1)
    carrito.agregar_producto(producto=p2, cantidad=1)
    carrito.agregar_producto(producto=p3, cantidad=1)
    carrito.agregar_producto(producto=p4, cantidad=1)
    carrito.agregar_producto(producto=p5, cantidad=1)

    # Act
    por_nombre: List[ItemCarrito] = carrito.obtener_items_ordenados(
        criterio="nombre")

    # Assert
    # orden por nombre: Dishwasher, Laptop, Monitor, Mouse, Smartphone
    # orden de productos: p4, p1, p5, p3, p2
    assert por_nombre[0].producto == p4
    assert por_nombre[1].producto == p1
    assert por_nombre[2].producto == p5
    assert por_nombre[3].producto == p3
    assert por_nombre[4].producto == p2


def test_obtener_items_ordenados_por_precio():
    """
    AAA:
    Arrange: Se crea un carrito y algunos productos para agregarlos al carrito.
    Act: Se ordenan los items del carrito por precio y se obtiene esta lista.
    Assert: Se verifica que estos items sigan el mismo orden
        en el que se agregaron los productos.
    """
    # Arrange
    carrito = Carrito()
    p1 = ProductoFactory(nombre="Laptop", precio=4)
    p2 = ProductoFactory(nombre="Smartphone", precio=2)
    p3 = ProductoFactory(nombre="Mouse", precio=7)
    p4 = ProductoFactory(nombre="Dishwasher", precio=9)
    p5 = ProductoFactory(nombre="Monitor", precio=3)

    carrito.agregar_producto(producto=p1, cantidad=1)
    carrito.agregar_producto(producto=p2, cantidad=1)
    carrito.agregar_producto(producto=p3, cantidad=1)
    carrito.agregar_producto(producto=p4, cantidad=1)
    carrito.agregar_producto(producto=p5, cantidad=1)

    # Act
    por_precio: List[ItemCarrito] = carrito.obtener_items_ordenados(
        criterio="precio")

    # Assert
    # orden por precio: p2 (2), p5 (3), p1 (4), p3 (7), p4 (9)
    assert por_precio[0].producto == p2
    assert por_precio[1].producto == p5
    assert por_precio[2].producto == p1
    assert por_precio[3].producto == p3
    assert por_precio[4].producto == p4
