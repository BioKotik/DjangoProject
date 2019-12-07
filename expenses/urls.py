from django.urls import path
from . import views
from django.contrib.auth import views as au_views

app_name = 'expenses'

urlpatterns = [
    path('', views.all_records, name='list_view'),
    path('login/', au_views.LoginView.as_view(), name='login'),
    path('logout/', au_views.LogoutView.as_view(), name='logout'),
]