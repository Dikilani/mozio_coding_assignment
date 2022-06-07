from api.models import *


def get_single_provider(provider_id):
    provider = Provider(id=provider_id)
    provider_obj = Provider.collection.get(provider.key)
    return provider_obj


def get_all_providers():
    return Provider.collection.fetch()


def get_single_service_area(service_area_id):
    service_area = ServiceArea(id=service_area_id)
    service_area_obj = ServiceArea.collection.get(service_area.key)
    return service_area_obj


def get_all_service_areas():
    return ServiceArea.collection.fetch()
