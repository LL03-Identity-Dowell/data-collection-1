from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_data, name='post_data'),
]
