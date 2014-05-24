from django.contrib import admin
from django_angular_backend.hello.models import Contact


class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)
