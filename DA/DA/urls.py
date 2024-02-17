from django.contrib import admin
from django.urls import path, include
# from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depression_detection/', include('depression_detection.urls')),  # Include URL patterns from depression_detection app
]
