from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from django_angular_backend.app.models import Contact


class ContactResource(ModelResource):
    class Meta:
        queryset = Contact.objects.all()
        resource_name = 'contact'
        authorization = Authorization()
