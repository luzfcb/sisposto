from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import (
    PostoList,
    PostoCreate,
    PostoDetail,
    PostoUpdate,
    PostoDelete,


)

urlpatterns = patterns('',
                       # Posto URLs
                       url(r'^$', view=login_required(PostoList.as_view()),
                           name="posto_list"),
                       url(r'^add/$', view=login_required(PostoCreate.as_view()),
                           name="posto_add"),
                       url(r'^(?P<posto_pk>[\d]+)/$',
                           view=login_required(PostoDetail.as_view()),
                           name="posto_detail"),
                       url(r'^(?P<posto_pk>[\d]+)/edit/$',
                           view=login_required(PostoUpdate.as_view()),
                           name="posto_edit"),
                       url(r'^(?P<posto_pk>[\d]+)/delete/$',
                           view=login_required(PostoDelete.as_view()),
                           name="posto_delete"),

                       # # Posto user URLs
                       # url(r'^(?P<posto_pk>[\d]+)/people/$',
                       # view=login_required(PostoUserList.as_view()),
                       #     name="posto_user_list"),
                       # url(r'^(?P<posto_pk>[\d]+)/people/add/$',
                       #     view=login_required(PostoUserCreate.as_view()),
                       #     name="posto_user_add"),
                       # url(r'^(?P<posto_pk>[\d]+)/people/(?P<user_pk>[\d]+)/remind/$',
                       #     view=login_required(PostoUserRemind.as_view()),
                       #     name="posto_user_remind"),
                       # url(r'^(?P<posto_pk>[\d]+)/people/(?P<user_pk>[\d]+)/$',
                       #     view=login_required(PostoUserDetail.as_view()),
                       #     name="posto_user_detail"),
                       # url(r'^(?P<posto_pk>[\d]+)/people/(?P<user_pk>[\d]+)/edit/$',
                       #     view=login_required(PostoUserUpdate.as_view()),
                       #     name="posto_user_edit"),
                       # url(r'^(?P<posto_pk>[\d]+)/people/(?P<user_pk>[\d]+)/delete/$',
                       #     view=login_required(PostoUserDelete.as_view()),
                       #     name="posto_user_delete"),
)
