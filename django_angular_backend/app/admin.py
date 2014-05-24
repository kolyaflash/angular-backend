from django.contrib import admin
from django_angular_backend.app.models import Contact


class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)
