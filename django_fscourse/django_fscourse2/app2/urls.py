from django.conf.urls import url
from app2 import views

urlpatterns = [
    url(r'^$',views.help, name='help'),
]