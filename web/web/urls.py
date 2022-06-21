from django.contrib import admin
from django.urls import path, include

from django.contrib import admin

admin.site.site_header = 'FP Website'  # default: "Django Administration"
admin.site.index_title = 'FP Website Modules' # default: "Site administration"
admin.site.site_title = 'ADMIN' # default: "Django site admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('contact/', include('contactforms.urls')),
    path('newsfeed/', include('newsfeed.urls', namespace='newsfeed')),
#    path('profile/', include('profile.urls', namespace='profile')),
]
