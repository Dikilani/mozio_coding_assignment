from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import credentials, auth
from django.contrib.auth.models import Group
from api.selectors import *
from api.services import *


from api.serializer import *


@api_view(['GET', 'POST'])
def provider_list_create_view(request):
    if request.method == 'GET':
        providers = get_all_providers()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method == 'POST':
        create_serializer = ProviderCreateSerializer(data=request.data)
        if create_serializer.is_valid(raise_exception=True):
            provider = create_provider(create_serializer.validated_data)
            serializer = ProviderSerializer(provider)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def provider_retrive_update_view(request, provider_id):
    provider = get_single_provider(provider_id)
    if not provider:
        raise NotFound
    if request.method == 'GET':
        serializer = ProviderSerializer(provider)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        update_serializer = ProviderUpdateSerializer(data=request.data)
        if update_serializer.is_valid(raise_exception=True):
            provider = update_provider(provider_id, update_serializer.data)
            serializer = ProviderSerializer(provider)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        provider = delete_provider(provider_id)
        return Response({"deleted": True, "provider_id": provider_id}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def service_area_list_create_view(request):
    if request.method == 'GET':
        service_area = get_all_service_areas()
        serializer = ServiceAreaSerializer(service_area, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method == 'POST':
        create_serializer = ServiceAreaCreateSerializer(data=request.data)
        if create_serializer.is_valid(raise_exception=True):
            service_area = create_service_area(create_serializer.validated_data)
            serializer = ServiceAreaSerializer(service_area)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def service_area_retrive_update_view(request, service_area_id):
    service_area = get_single_service_area(service_area_id)
    if not service_area:
        raise NotFound
    if request.method == 'GET':
        serializer = ServiceArea(service_area)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        update_serializer = ServiceAreaUpdateSerializer(data=request.data)
        if update_serializer.is_valid(raise_exception=True):
            service_area = update_service_area(service_area_id, update_serializer.data)
            serializer = ServiceAreaSerializer(service_area)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        service_area = delete_service_area(service_area_id)
        return Response({"deleted": True, "service_area_id": service_area_id}, status=status.HTTP_200_OK)