from django.apps import AppConfig

## Donde se registra la app y como se llama

class TodosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todos'
