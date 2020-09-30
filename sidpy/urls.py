from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from apps.qapuas.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.core.urls')),
    path('', include('apps.profil.urls')),
    path('', include('apps.berita.urls')),    

    path('dashboard/', dashboard, name='dashboard'),
    path('landing', auth_views.LoginView.as_view(template_name='qapuas/auth_login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='qapuas/auth_logout.html'), name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
