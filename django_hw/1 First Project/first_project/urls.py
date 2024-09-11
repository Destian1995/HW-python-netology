from django.contrib import admin
from django.urls import path, include  #  `include` импортирован

urlpatterns = [
    path('', include('app.urls')),  # имя приложения
    path('admin/', admin.site.urls),
]
