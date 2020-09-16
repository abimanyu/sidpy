from django.urls import path
from apps.core.views import frontpage

urlpatterns = [
    path('', frontpage, name='frontpage'),
]