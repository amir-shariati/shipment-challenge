from django.apps import AppConfig


class ShipmentAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.shipment_app'

    def ready(self):
        from . import signals
