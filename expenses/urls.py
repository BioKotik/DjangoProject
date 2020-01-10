from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'expenses'

urlpatterns = [
    path('', views.user_login, name='login'),
    # path('', views.all_records, name='list_view'),
    path('workplace/', views.all_records, name='list_view'),
    path('add/', views.create, name='add'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_login, name='logout'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
