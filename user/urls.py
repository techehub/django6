from django.urls import path
from .views import contactInfo
urlpatterns=[
    path ('contactus', contactInfo)
]