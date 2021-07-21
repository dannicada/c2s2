from django.apps import AppConfig


class ExchangeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exchangeApp'

    def ready(self):
        import exchangeApp.signals
