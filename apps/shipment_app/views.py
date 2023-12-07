from rest_framework import generics, views, filters
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, F, Max, Min
from .models import Tracking, TrackingItem, Article, Address, Carrier, Weather
from .serializers import (
    CarrierSerializer,
    ArticleSerializer,
    AddressSerializer,
    TrackingSerializer,
    TrackingItemSerializer,
    TrackingArticleSerializer,
    WeatherSerializer,
)


class CarrierListView(generics.ListAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer


class CarrierRetrieveView(generics.RetrieveAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer


class AddressListView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressRetrieveView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrieveView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TrackingListView(generics.ListAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer


class TrackingRetrieveView(generics.RetrieveAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer


class TrackingItemListView(generics.ListAPIView):
    queryset = TrackingItem.objects.all()
    serializer_class = TrackingItemSerializer


class TrackingItemRetrieveView(generics.RetrieveAPIView):
    queryset = TrackingItem.objects.all()
    serializer_class = TrackingItemSerializer


class TrackingArticleListView(generics.ListAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingArticleSerializer


class TrackingArticleRetrieveView(generics.RetrieveAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingArticleSerializer


class WeatherListView(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer


class WeatherRetrieveView(generics.RetrieveAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
