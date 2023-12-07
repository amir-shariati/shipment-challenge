from django.db import models
from django.utils.translation import gettext_lazy as _


class Carrier(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name=_('Carrier name'),)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Carrier name')
        verbose_name_plural = _('Carrier names')


class Address(models.Model):
    street = models.CharField(max_length=128, verbose_name=_("Street"),)
    zip_code = models.CharField(max_length=5, unique=True, verbose_name=_("Zip code"),)
    city = models.CharField(max_length=64, verbose_name=_("City"),)
    country = models.CharField(max_length=64, verbose_name=_("Country"),)

    def __str__(self):
        return f'{self.street}, {self.zip_code} {self.city}, {self.country}'

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class Article(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Article name'),)
    sku = models.CharField(max_length=12, unique=True, verbose_name=_("Stock Keeping Unit (SKU)"),)
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=_('Price'))

    def __str__(self):
        return f'{self.name}, sku={self.sku}'

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')


class Tracking(models.Model):

    DEFAULT_NONE = 'none'
    IN_TRANSIT = 'in-transit'
    TRANSIT = 'transit'
    INBOUND_SCAN = 'inbound-scan'
    SCANNED = 'scanned'
    DELIVERY = 'delivery'

    STATUS_CHOICES = [
        (DEFAULT_NONE, _('None')),
        (IN_TRANSIT, _('in-transit')),
        (TRANSIT, _('transit')),
        (INBOUND_SCAN, _('inbound-scan')),
        (SCANNED, _('scanned')),
        (DELIVERY, _('delivery')),
    ]

    tracking_number = models.CharField(max_length=64, unique=True, verbose_name=_('Tracking number'))
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE, related_name="carriers", verbose_name=_('Carrier'))
    sender_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name="sender_address",
        verbose_name=_('Sender address')
    )
    receiver_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name="receiver_address",
        verbose_name=_('Receiver address')
    )

    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default=DEFAULT_NONE,
        verbose_name=_('Status'),
    )

    def __str__(self):
        return f'{self.tracking_number},  status={self.status}'

    class Meta:
        verbose_name = _('Tracking')
        verbose_name_plural = _('Tracking')


class TrackingItem(models.Model):
    article = models.ForeignKey(
        Article,
        null=True,
        on_delete=models.CASCADE,
        related_name="articles",
        verbose_name=_('Article')
    )
    tracking = models.ForeignKey(
        Tracking,
        null=True,
        on_delete=models.CASCADE,
        related_name="tracking_list",
        verbose_name=_('Tracking')
    )
    quantity = models.PositiveSmallIntegerField(verbose_name=_('Quantity'))

    def __str__(self):
        return f'{self.article}, quantity={self.quantity}'

    class Meta:
        verbose_name = _('Tracking Item')
        verbose_name_plural = _('Tracking Items')


class Weather(models.Model):
    address = models.OneToOneField(
        Address,
        on_delete=models.DO_NOTHING,
        related_name="addresses",
        verbose_name=_('Address')
    )
    # weather = models.JSONField(verbose_name=_('Address'))
    coord_lon = models.FloatField(blank=True, null=True, verbose_name=_('Longitude of the location'))
    coord_lat = models.FloatField(blank=True, null=True, verbose_name=_('Latitude of the location'))

    weather_id = models.IntegerField(blank=True, null=True, verbose_name=_('Weather condition id'))
    weather_main = models.CharField(max_length=64, blank=True, null=True, verbose_name=_('Group of weather parameters'))
    weather_description = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('Weather condition within the group'))
    # weather_icon = None
    # base = None
    main_temp = models.FloatField(blank=True, null=True, verbose_name=_('Temperature'))
    main_feels_like = models.FloatField(blank=True, null=True, verbose_name=_('Temperature feels like'))
    main_pressure = models.FloatField(blank=True, null=True, verbose_name=_('Atmospheric pressure on the sea level'))
    main_humidity = models.FloatField(blank=True, null=True, verbose_name=_('Humidity'))
    main_temp_min = models.FloatField(blank=True, null=True, verbose_name=_('Minimum temperature at the moment'))
    main_temp_max = models.FloatField(blank=True, null=True, verbose_name=_('Maximum temperature at the moment'))
    main_sea_level = models.FloatField(blank=True, null=True, verbose_name=_('Atmospheric pressure on the sea level'))
    main_grnd_level = models.FloatField(blank=True, null=True, verbose_name=_('Atmospheric pressure on the ground level'))

    visibility = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Visibility, meter'))

    wind_speed = models.FloatField(blank=True, null=True, verbose_name=_('Wind speed'))
    wind_deg = models.FloatField(blank=True, null=True, verbose_name=_('Wind direction'))
    wind_gust = models.FloatField(blank=True, null=True, verbose_name=_('Wind gust'))

    clouds_all = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Cloudiness'))

    rain_1h = models.FloatField(blank=True, null=True, verbose_name=_('Rain volume for the last 1 hour'))
    rain_3h = models.FloatField(blank=True, null=True, verbose_name=_('Rain volume for the last 3 hours'))

    dt = models.DateTimeField(blank=True, null=True, verbose_name=_('Time of data calculation, unix, UTC '))

    # sys_type = None
    # sys_id = None
    # sys_message = None
    sys_country = models.CharField(max_length=4, blank=True, null=True, verbose_name=_('Country code'))
    sys_sunrise = models.DateTimeField(blank=True, null=True, verbose_name=_('Sunrise time, unix, UTC'))
    sys_sunset = models.DateTimeField(blank=True, null=True, verbose_name=_('Sunset time, unix, UTC'))

    timezone = models.DateTimeField(blank=True, null=True, verbose_name=_('Shift in seconds from UTC'))

    city_id = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('City ID'))
    city_name = models.CharField(max_length=48, blank=True, null=True, verbose_name=_('City name'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __str__(self):
        return f'{self.city_name}, city_id={self.city_id}, {self.weather_main} {self.main_temp}'

    class Meta:
        verbose_name = _('Current weather')
        verbose_name_plural = _('Current weather list')
