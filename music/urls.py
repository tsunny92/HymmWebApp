from django.conf.urls import url
from . import views

#from music.views import user_login
app_name='music'


urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
      
        url(r'^login/$',views.user_login, name="user_login"),
        url(r'^success/$',views.user_success, name="user_success"),
        url(r'^logout/$',views.user_logout, name="user_logout"),
        # /music/album/add/ 

        url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
        url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
        url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
        
        url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name='detail'), 
        ]
