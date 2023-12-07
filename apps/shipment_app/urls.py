from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import (
    CarrierListView, CarrierRetrieveView,
    AddressListView, AddressRetrieveView,
    ArticleListView, ArticleRetrieveView,
    TrackingItemListView, TrackingItemRetrieveView,
    TrackingListView, TrackingRetrieveView,
    TrackingArticleListView, TrackingArticleRetrieveView,
    WeatherListView, WeatherRetrieveView,
)

urlpatterns = [
    path('carrier/', CarrierListView.as_view(), name='carrier-list'),
    path('carrier/<int:pk>', CarrierRetrieveView.as_view(), name='carrier-detail'),

    path('address/', AddressListView.as_view(), name='address-list'),
    path('address/<int:pk>', AddressRetrieveView.as_view(), name='address-detail'),

    path('article/', ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>', ArticleRetrieveView.as_view(), name='article-detail'),

    path('tracking-item/', TrackingItemListView.as_view(), name='trackingitem-list'),
    path('tracking-item/<int:pk>', TrackingItemRetrieveView.as_view(), name='trackingitem-detail'),

    path('tracking/', TrackingListView.as_view(), name='tracking-list'),
    path('tracking/<int:pk>', TrackingRetrieveView.as_view(), name='tracking-detail'),

    path('tracking-info/', TrackingArticleListView.as_view(), name='tracking-info-list'),
    path('tracking-info/<int:pk>', TrackingArticleRetrieveView.as_view(), name='tracking-info-detail'),

    path('weather/', WeatherListView.as_view(), name='weather-list'),
    path('weather/<int:pk>', WeatherRetrieveView.as_view(), name='weather-detail'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
