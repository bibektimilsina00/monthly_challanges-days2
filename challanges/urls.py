
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name='home-page' ),
    path("<month>/", views.months_challanges,name="month-challange" ),
]

