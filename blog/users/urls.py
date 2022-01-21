from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path(r'register', views.register, name='register'),
    path(r'login', views.login_user, name='login'),
    path(r'logout', views.logout_user, name='logout'),
    path('profile', views.my_profile, name='profile'),
    path('chat', views.chat, name='chat'),
    path('all_offers', views.all_offers, name='all_offers'),
    path('my_offers', views.my_offers, name='my_offers'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
