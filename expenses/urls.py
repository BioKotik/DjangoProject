from django.urls import path
from . import views
from django.contrib.auth import views as au_views

app_name = 'expenses'

urlpatterns = [
    #path('', views.all_records, name='login'),
    path('', views.user_login, name='list_view'),
    path('workplace/', views.all_records, name='workplace')
    path('login/', views.user_login, name='login'),
    path('logout/', au_views.LogoutView.as_view(), name='logout'),
]