from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/make/', views.make_reservation, name='make_reservation'),
    path('reservations/update/<int:pk>/', views.update_reservation, name='update_reservation'),
    path('reservations/delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
]