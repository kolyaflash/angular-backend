from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField(null=True, blank=True)

    email = models.CharField(max_length=128, blank=True)
    phone_number = models.CharField(max_length=128, blank=True)
    cellphone_number = models.CharField(max_length=128, blank=True)
    jabber_id = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
