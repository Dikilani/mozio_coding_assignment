from fireo import fields, models


class BaseModel(models.Model):
    class Meta:
        abstract = True


class Provider(BaseModel):

    id = fields.IDField(required=False)  
    name = fields.TextField()
    email = fields.TextField()
    phone_number = fields.NumberField()
    language = fields.TextField()
    currency = fields.TextField()


class ServiceArea(BaseModel):

    id = fields.IDField(required=False)  # 1
    name = fields.TextField()
    price = fields.TextField()
    geojson_information = fields.GeoPoint()
