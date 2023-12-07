from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Address
from .tasks import request_weather_for_city


@receiver(post_save, sender=Address)
def add_weather_for_address(sender, **kwargs):
    if kwargs['created']:
        print('------------ signal post save for address ------------')
        address = kwargs['instance']

        print(f'call request weather task for city: {address.city}')
        print(f'call request weather task for address id: {address.id}')

        # request_weather_for_city.apply_async(args=(address.city,))
        request_weather_for_city.delay(address.id, address.city)
