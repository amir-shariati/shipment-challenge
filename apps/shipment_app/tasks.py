import requests
import celery
from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime
from django.utils.timezone import make_aware
from django.conf import settings
from .models import Address, Weather


logger = get_task_logger(__name__)


@shared_task
def request_weather_for_city(address_id, city):
    logger.info(f' request weather for city: {city}')

    with requests.Session() as session:
        response = session.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.OPEN_WEATHER_API_KEY}'
        )

    res_json = response.json()

    weather_data = dict()
    if response.status_code == 200:
        weather_data['coord_lon'] = res_json.get('coord', {}).get('lon')
        weather_data['coord_lat'] = res_json.get('coord', {}).get('lat')
        weather_data['weather_id'] = res_json.get('weather', {})[0].get('id')
        weather_data['weather_main'] = res_json.get('weather', {})[0].get('main')
        weather_data['weather_description'] = res_json.get('weather', {})[0].get('description')
        weather_data['main_temp'] = res_json.get('main', {}).get('temp')
        weather_data['main_feels_like'] = res_json.get('main', {}).get('feels_like')
        weather_data['main_pressure'] = res_json.get('main', {}).get('pressure')
        weather_data['main_humidity'] = res_json.get('main', {}).get('humidity')
        weather_data['main_temp_min'] = res_json.get('main', {}).get('temp_min')
        weather_data['main_temp_max'] = res_json.get('main', {}).get('temp_max')
        weather_data['main_sea_level'] = res_json.get('main', {}).get('sea_level')
        weather_data['main_grnd_level'] = res_json.get('main', {}).get('grnd_level')
        weather_data['visibility'] = res_json.get('visibility')
        weather_data['wind_speed'] = res_json.get('wind', {}).get('speed')
        weather_data['wind_deg'] = res_json.get('wind', {}).get('deg')
        weather_data['wind_gust'] = res_json.get('wind', {}).get('gust')
        weather_data['clouds_all'] = res_json.get('clouds', {}).get('all')
        weather_data['rain_1h'] = res_json.get('rain', {}).get('1h')
        weather_data['rain_3h'] = res_json.get('rain', {}).get('3h')
        weather_data['dt'] = make_aware(datetime.fromtimestamp((res_json.get('dt'))))
        weather_data['sys_country'] = res_json.get('sys', {}).get('country')
        weather_data['sys_sunrise'] = make_aware(datetime.fromtimestamp(res_json.get('sys', {}).get('sunrise')))
        weather_data['sys_sunset'] = make_aware(datetime.fromtimestamp(res_json.get('sys', {}).get('sunset')))
        # weather_data['timezone'] = datetime.fromtimestamp(res_json.get('timezone'))
        weather_data['city_id'] = res_json.get('id')
        weather_data['city_name'] = res_json.get('name')

    weather, created = Weather.objects.update_or_create(
        address_id=address_id,
        defaults=weather_data
    )
    logger.info(f' Weather.objects created:{created}, weather: {weather}')

    return f'weather response status for city - {city} : {response.status_code}'


@shared_task
def weather_update_every_two_hours():
    logger.info(f'update weather at : {datetime.now()}')
    group = celery.group([request_weather_for_city.s(address.id, address.city) for address in Address.objects.all()])
    group.apply_async()
    return True
