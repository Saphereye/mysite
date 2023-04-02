from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('blog/', include('blog.urls')),
    path('mycv/', include('mycv.urls')),
    path('admin/', admin.site.urls),
]
