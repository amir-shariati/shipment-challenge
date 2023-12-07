from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import Carrier, Article, Tracking, TrackingItem, Address, Weather


class CarrierSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Carrier
        fields = '__all__'


class AddressSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ArticleSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class TrackingSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Tracking
        fields = '__all__'
        expandable_fields = {
            'carrier': CarrierSerializer,
            'sender_address': AddressSerializer,
            'receiver_address': AddressSerializer,
        }


class TrackingItemSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = TrackingItem
        fields = '__all__'
        expandable_fields = {
            'article': ArticleSerializer,
            'tracking': Tracking,
        }


class TrackingItemArticleSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = TrackingItem
        fields = ('article',)
        expandable_fields = {
            'article': ArticleSerializer,
        }


class TrackingArticleSerializer(FlexFieldsModelSerializer):
    tracking_list = TrackingItemArticleSerializer(many=True)

    class Meta:
        model = Tracking
        # fields = '__all__'
        fields = ('id', 'tracking_number', 'carrier', 'sender_address', 'receiver_address', 'status', 'tracking_list')
        expandable_fields = {
            'carrier': CarrierSerializer,
            'sender_address': AddressSerializer,
            'receiver_address': AddressSerializer,
            'tracking_list': (TrackingItemArticleSerializer, {'many': True})
        }


class WeatherSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
        expandable_fields = {
            'address': AddressSerializer,
        }
