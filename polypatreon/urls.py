from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', Home,name='home'),
    path('create/',CreateOrValidateUser,name='validate'),
    path('in/<str:username>/',UserPage,name='userpage'),
    path('check_username/', check_username, name='check_username'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
