# tests/test_carrito.py

import pytest
from src.carrito import Carrito, ItemCarrito, Producto
from src.factories import ProductoFactory
from typing import List


def test_agregar_producto_nuevo(carrito: Carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item
        con el producto y cantidad 1.
    """
    # Arrange
    producto = ProductoFactory(nombre="Laptop", precio=1000.00)

    # Act
    carrito.agregar_producto(producto)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Laptop"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad(
        carrito: Carrito, producto_generico: Producto):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)

    # Act
    carrito.agregar_producto(producto_generico, cantidad=2)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto(carrito: Carrito, producto_generico: Producto):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=3)

    # Act
    carrito.remover_producto(producto_generico, cantidad=1)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo(
        carrito: Carrito, producto_generico: Producto):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=2)

    # Act
    carrito.remover_producto(producto_generico, cantidad=2)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


@pytest.mark.parametrize("cantidad_actualizada, items_esperados",
                         [(5, 1), (1, 1), (0, 0), (-2, 1)])
def test_actualizar_cantidad_producto(
        carrito: Carrito, producto_generico: Producto,
        cantidad_actualizada, items_esperados):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a la cantidad actualizada.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)

    # Act y Assert
    items: List[ItemCarrito] = []
    if cantidad_actualizada < 0:
        with pytest.raises(Exception):
            carrito.actualizar_cantidad(
                producto_generico, nueva_cantidad=cantidad_actualizada)
        items = carrito.obtener_items()
        assert len(items) == 1
        assert items[0].cantidad == 1
    else:
        carrito.actualizar_cantidad(
            producto_generico, nueva_cantidad=cantidad_actualizada)
        items = carrito.obtener_items()
        assert len(items) == items_esperados
        if cantidad_actualizada == 0:
            assert items == []
        else:
            assert len(items) == items_esperados
            assert items[0].cantidad == cantidad_actualizada


def test_actualizar_cantidad_a_cero_remueve_producto(
        carrito: Carrito, producto_generico: Producto):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=3)

    # Act
    carrito.actualizar_cantidad(producto_generico, nueva_cantidad=0)

    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total(carrito: Carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos
        con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta
        de cada item (precio * cantidad).
    """
    # Arrange
    producto1 = ProductoFactory(nombre="Impresora", precio=200.00)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto1, cantidad=2)  # Total 400
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150

    # Act
    total = carrito.calcular_total()

    # Assert
    assert total == 550.00


@pytest.mark.parametrize("precio, cantidad, descuento, \
                         total_esperado_con_descuento",
                         [
                             (500.0, 2, 10, 900.0),
                             (300, 5, 20, 1200.0),
                         ])
def test_aplicar_descuento(carrito: Carrito,
                           precio, cantidad, descuento,
                           total_esperado_con_descuento):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto
    con un precio y una cantidad determinada.
    Act: Se aplica un determinado descuento al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    producto = ProductoFactory(nombre="Genérico", precio=precio)
    carrito.agregar_producto(producto, cantidad)

    # Act
    total_con_descuento = carrito.aplicar_descuento(descuento)

    # Assert
    assert total_con_descuento == total_esperado_con_descuento


def test_aplicar_descuento_limites(carrito: Carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento
    fuera del rango [0, 100] genere un error.
    """
    # Arrange
    producto = ProductoFactory(nombre="Smartphone", precio=800.00)
    carrito.agregar_producto(producto, cantidad=1)

    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)


def test_vaciar_carrito(carrito: Carrito):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan algunos items
    Act: Se vacía el carrito
    Assert: Se verifica que no hay productos en el carrito
    """
    # Arrange
    producto1 = ProductoFactory(nombre="Smartphone", precio=800.00)
    carrito.agregar_producto(producto1, cantidad=1)
    producto2 = ProductoFactory(nombre="Dishwasher", precio=300.00)
    carrito.agregar_producto(producto2, cantidad=2)

    # Act
    carrito.vaciar()

    # Assert
    assert carrito.contar_items() == 0
    assert carrito.calcular_total() == 0


def test_descuento_condicional_si_aplicar(carrito: Carrito):
    """
    AAA:
    Arrange: Se crea un carrito, se agregan algunos items
        que sumen un monto total mayor a un mínimo,
        y se establecen el porcentaje y el valor mínimo.
    Act: Se llama al método del descuento condicional.
    Assert: Se verifica que el descuento condicional fue aplicado.
    """
    # Arrange
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


def test_descuento_condicional_no_aplicar(carrito: Carrito):
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


def test_agregar_producto_bajo_limite_stock(carrito: Carrito):
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
    stock = 5
    producto = ProductoFactory(nombre="A", precio=200.00, stock=stock)

    # Act y Assert
    try:
        carrito.agregar_producto(producto, cantidad=2)
        carrito.agregar_producto(producto, cantidad=2)
        carrito.agregar_producto(producto, cantidad=1)
        assert carrito.contar_items() == stock
    except Exception:
        assert False, "Se puede agregar al carrito \
            tantos productos de un mismo tipo como el stock \
            de este producto."


def test_agregar_producto_sobre_limite_stock(carrito: Carrito):
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
    stock = 5
    producto = ProductoFactory(nombre="A", precio=200.00, stock=stock)

    # Act y Assert
    carrito.agregar_producto(producto, cantidad=2)
    carrito.agregar_producto(producto, cantidad=2)
    with pytest.raises(Exception):
        carrito.agregar_producto(producto, cantidad=3)
    assert carrito.contar_items() <= stock


def test_obtener_items_ordenados_por_nombre(carrito: Carrito):
    """
    AAA:
    Arrange: Se crea un carrito y algunos productos para agregarlos al carrito.
    Act: Se ordenan los items del carrito por precio y se obtiene esta lista.
    Assert: Se verifica que estos items sigan el mismo orden
        en el que se agregaron los productos.
    """
    # Arrange
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


def test_obtener_items_ordenados_por_precio(carrito: Carrito):
    """
    AAA:
    Arrange: Se crea un carrito y algunos productos para agregarlos al carrito.
    Act: Se ordenan los items del carrito por precio y se obtiene esta lista.
    Assert: Se verifica que estos items sigan el mismo orden
        en el que se agregaron los productos.
    """
    # Arrange
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
