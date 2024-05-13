from django.urls import path, include

from story.admin import admin_site
from core.views import home_page

urlpatterns = [
    path('admin/', admin_site.urls),
    path('api/v1/', include('story.urls')),
    path('', home_page, name='home-page'),
    path('s/<str:pk>', home_page, name='story-page'),
]
