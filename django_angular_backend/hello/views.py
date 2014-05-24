from annoying.decorators import render_to
from django.contrib.auth.models import User
from django_angular_backend.hello.models import Contact


@render_to('index.html')
def home(request):
    users = User.objects.filter()
    contacts = Contact.objects.all()

    return {
        'users': users,
        'contacts': contacts,
    }
