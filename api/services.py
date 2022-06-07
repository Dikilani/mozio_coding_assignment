
from api.models import *
from rest_framework.exceptions import NotFound
from api.selectors import *


# Create Provider
def create_provider(data):
    data['id'] = data['name']
    provider = Provider.collection.create(**data)
    return provider


# Update Provider
def update_provider(provider_id, data):
    provider = get_single_provider(provider_id)
    if not provider:
        raise NotFound
    data['name'] = provider.name or provider.id

    for field in data:
        if 'name' not in field:
            setattr(provider, field, data[field])

    provider.update(provider.id)
    return provider

# Delete Provider


def delete_provider(provider_id):
    provider = get_single_provider(provider_id)
    if not provider:
        raise NotFound
    provider = Provider.collection.delete(key=provider.id)
    return provider


# Create Service Area
def create_service_area(data):
    data['id'] = data['name']
    service_area = ServiceArea.collection.create(**data)
    return service_area


# Update Service Area
def update_service_area(service_area_id, data):
    service_area = get_single_service_area(service_area_id)
    if not service_area:
        raise NotFound
    data['name'] = service_area.name or service_area.id

    for field in data:
        if 'name' not in field:
            setattr(service_area, field, data[field])

    service_area.update(service_area.id)
    return service_area


# Delete Service Area
def delete_service_area(service_area_id, ):
    service_area = get_single_provider(service_area_id)
    if not service_area:
        raise NotFound
    service_area = ServiceArea.collection.delete(key=service_area.id)
    return service_area
