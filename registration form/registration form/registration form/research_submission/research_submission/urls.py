# your_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('submission/', include('submission.urls')),  # Include app-specific URLs
]
