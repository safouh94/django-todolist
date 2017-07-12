from django.conf.urls import url, include
from django.contrib import admin

from .views import TwitterLogin
# JSON Web Token
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

# Token-based Auth
from rest_framework.authtoken import views

from views import (
    TodoCreateAPIView,
    TodoDetailAPIView,
    TodoListAPIView,
    TodoDeleteAPIView,
    TodoUpdateAPIView,
    )

urlpatterns = [
    url(r'^$', TodoListAPIView.as_view(), name='list'),  # For POST method
    url(r'^create/$', TodoCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TodoDetailAPIView.as_view(), name='detail'),  # For GET, DELETE, PUT methods
    url(r'^(?P<pk>\d+)/delete/$', TodoDeleteAPIView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', TodoUpdateAPIView.as_view(), name='update'),

    # JSON Web Token
    # url(r'^json-auth/', obtain_jwt_token),

    # Token Auth
    # url(r'^token-auth/', views.obtain_auth_token),



    # rest_auth
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # social account
    url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login')
]
