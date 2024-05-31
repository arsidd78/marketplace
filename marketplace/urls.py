
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/',include('registration.urls')),
    path('registration/',include('django.contrib.auth.urls')),
    path('',include('product.urls')),
    path('',include('django.contrib.auth.urls')),
    path('member/',include('member.urls')),
    path('chat/',include('chat.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
