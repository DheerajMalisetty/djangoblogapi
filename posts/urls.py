from django.conf.urls import url
from posts.views import post_create
from posts.views import post_list
from posts.views import post_detail
from posts.views import post_delete
from posts.views import post_update

urlpatterns = [
    url(r'^(?P<id>\d+)/$',post_detail,name="detail"),
    url(r'^create/$',post_create,name="create"),
    url(r'^$',post_list,name="list"),
    url(r'^delete/$',post_delete,name="delete"),
    url(r'^update/$',post_update,name="update"),
]