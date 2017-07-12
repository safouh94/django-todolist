from django.conf.urls import url, include

from . import views

app_name = 'todo'

urlpatterns = [
    # todos/
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    # url(r'^$', views.IndexView.as_view(), name='index'),

    # normal login..
    # url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # url(r'^login_user/$', views.login_user, name='login_user'),
    # url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # todos/<todo_id>
    # url(r'^(?P<todo_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /toodo/add/
    # url(r'todos/add/$', views.TodoCreate.as_view(), name='todo-add'),

    # /toodo/2/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.TodoDelete.as_view(), name='todo-delete'),

    # todos/<todo_id>/achieved
    url(r'^(?P<todo_id>[0-9]+)/achieved/$', views.achieved, name='achieved'),
]
