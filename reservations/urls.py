from django.urls import path
from .views import * # imports all the functions from views

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('reserve/', make_reservation, name='make_reservation'),
]