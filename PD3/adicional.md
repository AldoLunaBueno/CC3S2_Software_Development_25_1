**Extraer issue IDs de mensajes (`git log`)**

```bash
git log --oneline | \
  grep -Po '(?<=\[)[A-Z]{2,5}-[0-9]+(?=\])' | sort -u
# Explicación:
# (?<=\[)  ─ lookbehind para "["
# [A-Z]{2,5}-[0-9]+  ─ proyecto-1234
# (?=\])   ─ lookahead para "]"
```

**Detectar merges automáticos y extraer la rama objetivo**

```bash
git log --grep='^Merge branch' --pretty=format:'%s' | \
  grep -Po '(?<=Merge branch ')[^']+' 
# Captura el nombre de la rama tras "merge branch '<rama>'"
```

**Paso con grupo nombrado y alternancia**

```python
from behave import given

@given(r'^(?P<user>[A-Za-z0-9_]+) tiene (?P<count>[0-9]+) (artículos|productos)$')
def step_user_items(context, user, count):
    # user: nombre de usuario
    # count: número de artículos o productos
    context.user = user
    context.count = int(count)
```

**Paso con partes opcionales y lookahead**

```python
from behave import when

@when(r'^el usuario intenta(?: iniciar sesión(?: con contraseña "(?P<pw>[^"]+)")?)?$')
def step_login_optional_pw(context, pw=None):
    # El paso coincide con:
    #   "el usuario intenta"
    #   "el usuario intenta iniciar sesión"
    #   'el usuario intenta iniciar sesión con contraseña "abc"'
    context.pw = pw
```

**Validar formatos de fecha dentro de un paso**

```python
from behave import then

@then(r'^la fecha de entrega es (?P<date>\d{4}-\d{2}-\d{2})$')
def step_check_date(context, date):
    # date: "2025-04-16"
    import datetime
    datetime.datetime.strptime(date, '%Y-%m-%d')
```

**Step definition para comandos Git**

```python
from behave import given

@given(r'^estoy en la rama "(?P<branch>[a-z0-9/_-]+)"$')
def step_on_branch(context, branch):
    import subprocess
    current = subprocess.check_output(['git','rev-parse','--abbrev-ref','HEAD']).decode().strip()
    assert current == branch
```

**Capturar tablas Gherkin con regex dinámico**

```python
from behave import then
import re

@then(r'^los siguientes usuarios:$')
def step_table_users(context):
    # context.table tendrá filas:
    # | user   | age |
    # | alice  | 30  |
    # Validación adicional:
    for row in context.table:
        assert re.match(r'^[a-z]+$', row['user'])
        assert re.match(r'^[0-9]{1,3}$', row['age'])
```

**Scenario outline con ejemplos que usan regex**

```gherkin
Scenario Outline: Validación de correos
  Given el email "<email>"
  When valido el formato
  Then debe ser <valid>

Examples:
  | email                 | valid  |
  | user@example.com      | True   |
  | invalid-email@        | False  |
  | otra.cosa@dominio.org | True   |
```

```python
from behave import given, then
import re

EMAIL_RE = re.compile(r'^[[:alnum:]_.+-]+@[[:alnum:]-]+\.[[:alnum:].-]+$')

@given(r'el email "(?P<email>[^"]+)"')
def step_set_email(context, email):
    context.email = email

@then(r'debe ser (?P<valid>True|False)')
def step_check_email(context, valid):
    match = bool(EMAIL_RE.match(context.email))
    assert match == (valid == 'True')
```

#### Paso 14 – BDD con `behave`

1. **Feature** (`features/login.feature`):

   ```gherkin
   Feature: Login
     Scenario Outline: credenciales válidas
       Given el usuario "<user>" con contraseña "<pass>"
       When intenta iniciar sesión
       Then debe ver "Bienvenido, <user>"

     Examples:
       | user  | pass    |
       | alice | secret1 |
   ```

2. **Steps** (`features/steps/login_steps.py`):

   ```python
   from behave import given, when, then
   from myapp.auth import autenticar

   @given(r'el usuario "(?P<user>[^"]+)" con contraseña "(?P<pass>[^"]+)"')
   def step_user(c, user, pass_):
       c.user, c.passwd = user, pass_

   @when('intenta iniciar sesión')
   def step_try(c):
       c.result = autenticar(c.user, c.passwd)

   @then(r'debe ver "(?P<msg>[^"]+)"')
   def step_verify(c, msg):
       assert c.result == msg
   ```

3. Ejecuta:

   ```bash
   behave -q
   ```

#### Paso 15 – Pipelines CI

**GitHub actions** (`.github/workflows/ci.yml`):

```yaml
name: CI
on: [push,pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with: python-version: 3.10
      - run: pip install -r requirements.txt
      - run: pytest -q
      - run: behave -q
```

**Makefile local**:

```makefile
.PHONY: lint test bdd all
lint:
    flake8 src tests
test:
    pytest -q
bdd:
    behave -q
all: lint test bdd
```

#### Scripts de métricas en pipeline CI/CD

Hooks o "post steps"

```yml
- name: Calcular duración de test
  if: always()
  run: |
    TIEMPO_INICIAL=${{ steps.start_time.outputs.time }}
    TIEMPO_FINAL=$(date +%s)
    DURACION=$((TIEMPO_FINAL - TIEMPO_INICIAL))
    echo "ci_test_duration_seconds $DURACION" >> metrics.prom
```

El archivo _metrics.prom_ se expone en un endpoint HTTP sencillo (python -m http.server).

Instalación del módulo pytest-benchamrk

```
pytest --benchmark-json=benchmark_data.json
```

Convertir json a métricas de Prometheus:

```py
# export_benchmarks.py
import json, sys
data = json.load(open(sys.argv[1]))
for bench in data['benchmarks']:
    name = bench['name'].replace('::', '_')
    mean_ns = bench['stats']['mean']
    print(f'benchmark_{name}_ns {mean_ns}')
```

Preparar para scraping en pipeline:

```yml
- name: Export benchmarks to Prometheus format
  run: python export_benchmarks.py benchmark_data.json > metrics.prom
```

Bloquear merge en GitHub Actions si una verificación falla:

```yml
jobs:
  benchmark-compare:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run benchmarks
        run: pytest --benchmark-save=baseline
      - name: Compare
        run: pytest --benchmark-compare --benchmark-fail-max-time-diff=0.05
```

Rechazar PR si falla la verificación de cobertura de código:

```
- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v2
  with:
    fail_ci_if_error: true
    flags: unittests
    coverage_file: coverage.xml
    threshold: 80
```

#### Ejemplos de alertas en Prometheus

```yml
- alert: HighLeadTime
  expr: avg_over_time(ci_pipeline_duration_seconds{stage="deploy"}[6h]) > 3600
  for: 30m
  labels:
    severity: warning
  annotations:
    summary: "Lead Time alto en despliegues"
    description: "El tiempo medio de despliegue en la última 6h es > 1h"
```