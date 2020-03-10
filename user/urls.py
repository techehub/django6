from django.urls import path
from .views import contactInfo, savecontact
urlpatterns=[
    path ('contactus', contactInfo),
    path ('savecontact', savecontact)
]