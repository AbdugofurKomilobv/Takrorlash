
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('/', include('blogs.urls',namespace='blogs')),  # Add blog app URLs here
    path('admin/', admin.site.urls),
]
