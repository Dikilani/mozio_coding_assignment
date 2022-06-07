from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from api.models import *

class ProviderCreateSerializer(serializers.Serializer):

    id = serializers.CharField(required=False)  # 1
    name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    phone_number = serializers.IntegerField(required=False)
    language = serializers.CharField(required=False)
    currency = serializers.CharField(required=False)


class ProviderUpdateSerializer(serializers.Serializer):

    id = serializers.CharField(required=False)  # 1
    name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    phone_number = serializers.IntegerField(required=False)
    language = serializers.CharField(required=False)
    currency = serializers.CharField(required=False)


class ProviderSerializer(serializers.Serializer):

    id = serializers.CharField(required=False)  # 1
    name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.IntegerField()
    language = serializers.CharField()
    currency = serializers.CharField()


class ServiceAreaCreateSerializer(serializers.Serializer):

    id = serializers.CharField(required=False)  # 1
    name = serializers.CharField(required=False)
    price = serializers.CharField(required=False)
    geojson_information = serializers.DictField(required=False)


class ServiceAreaUpdateSerializer(serializers.Serializer):

    id = serializers.CharField(required=False)  # 1
    name = serializers.CharField(required=False)
    price = serializers.CharField(required=False)
    geojson_information = serializers.DictField(required=False)


# class GeojsonSerializer(GeoFeatureModelSerializer):
 
#     class Meta:
#         model = ServiceArea
#         geo_fields = ['polygon']


class ServiceAreaSerializer(serializers.Serializer):

    id = serializers.CharField(required=False)  # 1
    name = serializers.CharField()
    price = serializers.CharField()
    geojson_information = GeojsonSerializer()


