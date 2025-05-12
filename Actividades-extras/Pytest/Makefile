# Makefile para ejecución de pruebas con Pytest y Pytest-xdist

# Configura el directorio donde están los tests
TEST_DIR = tests

# Comando base para pytest
PYTEST = pytest -v

# Ejecución paralela automática con todos los núcleos disponibles
PYTEST_PARALLEL = $(PYTEST) -n auto

# Ejecuta todas las pruebas en paralelo
test:
	$(PYTEST_PARALLEL) $(TEST_DIR)

# Ejecuta solo pruebas unitarias
test-unit:
	$(PYTEST_PARALLEL) -m "unit" $(TEST_DIR)

# Ejecuta solo pruebas de integración
test-integration:
	$(PYTEST_PARALLEL) -m "integration" $(TEST_DIR)

# Ejecuta solo pruebas BDD
test-bdd:
	$(PYTEST_PARALLEL) -m "bdd" $(TEST_DIR)

# Ejecuta todas menos las BDD
test-no-bdd:
	$(PYTEST_PARALLEL) -m "not bdd" $(TEST_DIR)

# Limpia caché de pytest y carpetas de compilación
clean:
	rm -rf .pytest_cache __pycache__ $(TEST_DIR)/__pycache__
