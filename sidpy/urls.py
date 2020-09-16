from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



from apps.qapuas.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),

    path('', include('apps.core.urls')),
    path('', include('apps.profil.urls')),
    path('', include('apps.berita.urls')),


    

    

    path('landing/', dashboard, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
