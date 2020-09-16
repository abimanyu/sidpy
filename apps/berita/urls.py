from django.urls import path
from apps.berita.views import Berita_Detail, Category_Detail, qapuas_berita

urlpatterns = [
    path('berita/<slug:slug>/', Category_Detail, name='Category_Detail'),
    path('berita/<slug:category_slug>/<slug:slug>/', Berita_Detail, name='Berita_Detail'),
    # Dashboard
    path('a/berita/', qapuas_berita, name='qapuas_berita'),
]