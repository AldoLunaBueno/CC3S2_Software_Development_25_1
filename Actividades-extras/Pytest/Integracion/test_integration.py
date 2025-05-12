# test_integration.py
import os
import sqlite3
import pytest
from fastapi.testclient import TestClient

from app import app, DATABASE

@pytest.fixture(scope="module", autouse=True)
def ensure_clean_database():
    # Fixture autouse que prepara y limpia la base antes y después de todos los tests
    # Se ejecuta una sola vez por módulo.
    # Teardown al final: elimina el fichero.
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    yield
    if os.path.exists(DATABASE):
        os.remove(DATABASE)

@pytest.fixture(scope="function")
def db_connection():
    # Fixture de alcance función: abre conexión a la base real
    conn = sqlite3.connect(DATABASE)
    yield conn
    conn.close()

@pytest.fixture(scope="function")
def client():
    # Fixture para el cliente HTTP de FastAPI
    return TestClient(app)

def test_create_and_list_items(db_connection, client):
    # Al inicio la tabla está vacía
    resp = client.get("/items/")
    assert resp.status_code == 200
    assert resp.json() == []

    # Creamos un ítem
    resp = client.post("/items/", json={"id": 42})
    assert resp.status_code == 201
    assert resp.json() == {"id": 42}

    # Verificamos directamente en la DB
    cursor = db_connection.execute("SELECT id FROM items")
    rows = [r[0] for r in cursor]
    assert rows == [42]

    # Y vía API list_items
    resp = client.get("/items/")
    assert resp.json() == [42]

def test_duplicate_item_returns_400(client):
    # Insertamos una primera vez
    client.post("/items/", json={"id": 99})

    # Intentamos insertar de nuevo el mismo id
    resp = client.post("/items/", json={"id": 99})
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Item ya existe"
