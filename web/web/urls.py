from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

admin.site.site_header = 'FP Website'  # default: "Django Administration"
admin.site.index_title = 'FP Website Modules' # default: "Site administration"
admin.site.site_title = 'ADMIN' # default: "Django site admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls', namespace='website')),
    path('contact/', include('contactforms.urls')),
    path('newsfeed/', include('newsfeed.urls', namespace='newsfeed')),
#    path('team/', include('team.urls', namespace='team')),
#    path('profile/', include('profile.urls', namespace='profile')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

