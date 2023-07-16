from django.urls import path
from applesson4.views import lesson4view

urlpatterns = [
    path('lesson4/', lesson4view, name='lesson4'),
]
