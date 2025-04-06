from django.urls import path
from .views import home, contacts
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)