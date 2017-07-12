from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include("todos.api.urls", namespace='todos-api')),
    # url(r'^', include('todos.urls')),
    url(r'^todos/', include('todos.urls')),
    url(r'^admin/', admin.site.urls),

    # 'allauth'
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    ]
