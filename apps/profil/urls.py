from django.urls import path
from . import views

urlpatterns = [
    path('p/<slug:slug>/', views.category_detail, name='category_detail'),
    path('p/<slug:category_slug>/<slug:slug>/', views.pages_detail, name='pages_detail'),
    # Dashboard
    path('p/landing', views.qapuas_pages, name='qapuas_profil'),
    # Post
    path('p/make', views.addPages, name='addPages'),
    path('p/touch=<str:pk>', views.updatePages, name='updatePages'),
    path('p/rm=<str:pk>', views.deletePages, name='deletePages'),
]