from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("te_demo.urls")),
    path('admin/', admin.site.urls),
]
