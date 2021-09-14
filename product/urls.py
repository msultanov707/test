from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken import views
from . import views
from .views import ClientsList, ClientDetail, CarsList, CarsDetail, OrdersList, OrdersDetail, UsersList, UsersDetail

urlpatterns = [
    path('clients/', views.ClientsList.as_view()),
    path('clients/<int:pk>/', views.ClientDetail.as_view()),
    path('cars/', views.CarsList.as_view()),
    path('cars/<int:pk>/', views.CarsDetail.as_view()),
    path('orders/', views.OrdersList.as_view()),
    path('orders/<int:pk>/', views.OrdersDetail.as_view()),
    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>/', views.UsersDetail.as_view()),
]
# urlpatterns += [
#     path('api-token-auth/', views.obtain_auth_token),
# ]