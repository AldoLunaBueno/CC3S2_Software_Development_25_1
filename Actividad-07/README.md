# Actividad 7: Proyecto Belly

El repositorio en el que trabajé es [este](https://github.com/AldoLunaBueno/ej-belly-project).

![alt](2025-04-19-23-08-12.png)

![alt](2025-04-19-23-36-04.png)

![alt](2025-04-20-11-43-55.png)

![alt](2025-04-20-12-19-34.png)

![alt](2025-04-20-12-36-23.png)

![alt](2025-04-20-12-46-48.png)

![alt](2025-04-20-12-47-50.png)

```yml
- name: Notify to Slack if fails through a webhook
  if: failure()
  run: |
    curl -X POST -H 'Content-Type: application/json' \
    --data '{"text": "El pipeline falló en el repo ${{ github.repository }}.\nCommit: ${{ github.sha }}\nAutor: ${{ github.actor }}"}' \
    https://hooks.slack.com/services/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
```

Más adelante vamos a usar GitHub Secrets para ocultar el acceso al webhook: `secrets.SLACK_WEBHOOK_URL`.

![](2025-04-20-13-36-59.png)

La clave fue secrets

![](2025-04-20-14-40-57.png)