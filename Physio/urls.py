from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service/consultation', views.consultation, name='consultation'),
    path('service/physiotherapy', views.physiotherapy, name='physiotherapy'),
    path('service/medecine_generale', views.medecine_generale, name='medecine_generale'),
    path('service/imagerie_medicale', views.imagerie_medicale, name='imagerie_medicale'),
    path('service/rehabilitation_fonctionnelle', views.rehabilitation_fonctionnelle,
         name='rehabilitation_fonctionnelle'),
    path('event/<int:event_id>/', views.event, name='event'),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
