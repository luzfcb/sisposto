from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import (
    VeiculoList,
    VeiculoCreate,
    VeiculoDetail,
    VeiculoUpdate,
    VeiculoDelete,


)

urlpatterns = patterns('',
                       # Veiculo URLs
                       url(r'^$', view=login_required(VeiculoList.as_view()),
                           name="veiculo_list"),
                       url(r'^add/$', view=login_required(VeiculoCreate.as_view()),
                           name="veiculo_add"),
                       url(r'^(?P<veiculo_pk>[\d]+)/$',
                           view=login_required(VeiculoDetail.as_view()),
                           name="veiculo_detail"),
                       url(r'^(?P<veiculo_pk>[\d]+)/edit/$',
                           view=login_required(VeiculoUpdate.as_view()),
                           name="veiculo_edit"),
                       url(r'^(?P<veiculo_pk>[\d]+)/delete/$',
                           view=login_required(VeiculoDelete.as_view()),
                           name="veiculo_delete"),

                       # # Veiculo user URLs
                       # url(r'^(?P<veiculo_pk>[\d]+)/people/$',
                       # view=login_required(VeiculoUserList.as_view()),
                       #     name="veiculo_user_list"),
                       # url(r'^(?P<veiculo_pk>[\d]+)/people/add/$',
                       #     view=login_required(VeiculoUserCreate.as_view()),
                       #     name="veiculo_user_add"),
                       # url(r'^(?P<veiculo_pk>[\d]+)/people/(?P<user_pk>[\d]+)/remind/$',
                       #     view=login_required(VeiculoUserRemind.as_view()),
                       #     name="veiculo_user_remind"),
                       # url(r'^(?P<veiculo_pk>[\d]+)/people/(?P<user_pk>[\d]+)/$',
                       #     view=login_required(VeiculoUserDetail.as_view()),
                       #     name="veiculo_user_detail"),
                       # url(r'^(?P<veiculo_pk>[\d]+)/people/(?P<user_pk>[\d]+)/edit/$',
                       #     view=login_required(VeiculoUserUpdate.as_view()),
                       #     name="veiculo_user_edit"),
                       # url(r'^(?P<veiculo_pk>[\d]+)/people/(?P<user_pk>[\d]+)/delete/$',
                       #     view=login_required(VeiculoUserDelete.as_view()),
                       #     name="veiculo_user_delete"),
)
