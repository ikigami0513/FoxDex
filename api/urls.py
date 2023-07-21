from django.urls import path
from rest_framework.authtoken import views as rest_views
from .views import *

urlpatterns = [
    path('get_token', rest_views.obtain_auth_token, name='token'),
]