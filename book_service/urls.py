from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += path('__debug__/', include(debug_toolbar.urls))