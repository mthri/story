from django.urls import path, include
from django.conf import settings

from story.admin import admin_site
from core.views import home_page

urlpatterns = [
    path(settings.ADMIN_URL, admin_site.urls),
    path('api/v1/', include('story.urls')),
    path('', home_page, name='home-page'),
    path('s/<str:pk>', home_page, name='story-page'),
]
