from django.contrib import admin
from .models import Carrier, Address, Article, Tracking, TrackingItem, Weather


@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    list_per_page = 25


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'zip_code', 'city', 'country')
    search_fields = ('zip_code', 'city', 'country')

    list_per_page = 25


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price')
    search_fields = ('name', 'sku')

    list_per_page = 25


class TrackingItemTabularInline(admin.TabularInline):
    model = TrackingItem
    extra = 1
    list_display = ('article', 'quantity',)
    list_select_related = ('article', 'tracking',)
    autocomplete_fields = ('article',)


@admin.register(TrackingItem)
class TrackingItemAdmin(admin.ModelAdmin):
    list_display = ('article', 'quantity',)
    list_select_related = ('article', 'tracking')
    readonly_fields = ('article', 'tracking', 'quantity')

    list_per_page = 25


@admin.register(Tracking)
class TrackingAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'sender_address', 'receiver_address', 'status')
    list_select_related = ('carrier', 'sender_address', 'receiver_address',)
    autocomplete_fields = ('carrier', 'sender_address', 'receiver_address',)
    inlines = (TrackingItemTabularInline,)

    list_per_page = 25


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('address', 'city_name', 'city_id', 'weather_main', 'main_temp')
    list_select_related = ('address',)
    autocomplete_fields = ('address',)

    def get_readonly_fields(self, request, obj=None):
        # return [field.name for field in self.model._meta.fields]
        return [field.name for field in self.opts.fields]
        # # make all fields readonly
        # readonly_fields = list(
        #     set(
        #         [field.name for field in self.opts.local_fields] +
        #         [field.name for field in self.opts.local_many_to_many]
        #     )
        # )
        #
        # if 'is_submitted' in readonly_fields:
        #     readonly_fields.remove('is_submitted')
        #
        # return readonly_fields

    list_per_page = 25
