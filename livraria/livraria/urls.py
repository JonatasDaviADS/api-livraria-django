from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),        # painel administrativo do Django
    # tudo que começa com /api/ vai para core/urls.py
    path('api/', include('core.urls')),
]
