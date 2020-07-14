'''from django.contrib import admin
from django.conf.urls import url
from jobs import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^dipesh/', views.dipesh, name="dipesh"),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_roots=settings.MEDIA_ROOT)
'''
from django.contrib import admin
from django.conf.urls import url
from jobs import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^dipesh/', views.dipesh, name="dipesh"),
    url(r'^jobs/(\d+)/', views.detail, name='detail')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
