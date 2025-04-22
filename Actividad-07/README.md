# Actividad 7: Proyecto Belly

---

**El repositorio en el que trabajé es [este](https://github.com/AldoLunaBueno/ej-belly-project).**

Aquí solo publico capturas y las comento para referencia personal.

---

Tenía un **token personal** para hacer cambios en mis repos desde mi terminal local, por ejemplo. El problema que encontré fue que para usar un pipeline de **GitHub Actions** en mi repo necesito que mi token personal tenga un permiso especial de **workflow**.

![alt](2025-04-19-23-08-12.png)

El pipeline por fin funcionó. Como no lo había hecho antes, se me pasaron varios errores, como usar guinoes de más o no usar una correcta identación:

![alt](2025-04-19-23-36-04.png)

Si nuestro código pasa todas las pruebas a las que lo somete el pipeline, todo está bien. Pero ¿qué sucede si no pasa las pruebas del pipeline? Se debe **notificar** al desarrollador. Para esto conectamos el pipeline con **Slack**.

![alt](2025-04-20-11-43-55.png)

![alt](2025-04-20-12-19-34.png)

![alt](2025-04-20-12-36-23.png)

![alt](2025-04-20-12-46-48.png)

Aquí vemos la pieza que conecta GitHub Actions con Slack: un **webhook**.

![alt](2025-04-20-12-47-50.png)

```yml
- name: Notify to Slack if fails through a webhook
  if: failure()
  run: |
    curl -X POST -H 'Content-Type: application/json' \
    --data '{"text": "El pipeline falló en el repo ${{ github.repository }}.\nCommit: ${{ github.sha }}\nAutor: ${{ github.actor }}"}' \
    https://hooks.slack.com/services/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
```

Slack rompe el webhook si no se usa **GitHub Secrets** porque así evita que su URL de acceso a la app sea pública. Si no hiciera esto, **¡gente ajena a nuestro proyecto nos llenaría el canal de mensajes!** La referencia a la URL en el pipeline ahora es `secrets.SLACK_WEBHOOK_URL`.

Un bot de Slack (app) se encarga de recibir los mensajes del webhook y retransmitirlos al canal al cual es invitado. Aquí invitamos al bot CI Notifier al canal #ci-notifications para recibir los mensajes del pipeline de GitHub si algo sale mal.

![alt](2025-04-20-13-36-59.png)

Logramos obtener automáticamente el mensaje de fallo en el pipeline, el cual incluye el nombre del repo, el commit que falló y el autor (mi persona):

![alt](2025-04-20-14-40-57.png)

El error fue hecho a propósito, así que solo hacemos revert sobre ese único error y ahora todo funciona bien, como se puede comprobar viendo el check verde:

![alt](2025-04-20-16-23-29.png)

Verificamos la **cobertura de código** de forma local (incluimos análisis de ramas) viendo la carpeta htmlcov generada con el comando:

```bash
pytest --cov=src --cov-branch --cov-report=html
```

![alt](2025-04-21-08-49-49.png)

Añadimos una historia de usuario en **GitHub Issues**, la cual se guarda con un código (#1 en este caso):

![alt](2025-04-21-10-30-36.png)

Este código es el que tenemos que usar en nuestras pruebas BDD para vincularlas con la historia en GitHub Issues:

![alt](2025-04-21-10-34-53.png)

Ya temrinando, instalamos el módulo **flake8** para **verificar la calidad código** en cuanto a su estilo:

![alt](2025-04-22-14-37-47.png)

Tenemos muchos errores, y seguirlos desde las referencias que nos da el módulo no es tan fácil, así que instalamos una extensión de flake8 en VS Code para que se muestren los errores de estilo directamente en nuestro código:

![alt](2025-04-22-14-52-46.png)

Una vez corregidos los errores y habiendo adicionado el paso en el pipeline para que se realice automáticamente la verificación de calidad con GitHub Actions, hacemos el push y el código (tanto tests como código fuente) pasa la verificación:

![alt](2025-04-22-15-24-38.png)

Por último, especificamos en el pipeline que queremos que el reporte de la cobertura de código (html) se publique como artifact y se ve así en GitHub:

![alt](2025-04-22-15-25-46.png)

El despliegue especificado en el ejercicio 15 no lo hice porque considero que no corresponde hacerlo en esta actividad. No definimos una API para permitir consultas HTTP hacia nuestra lógica.
