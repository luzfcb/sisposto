# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from apps.core.views import Home, MailNotifyView, TasksNotifyView, NotificationsView, ModalVoicecommandView
from apps.users.views import UsersListView

urlpatterns = patterns('',


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^postos/', include('apps.posto.urls')),
    url(r'^veiculos/', include('apps.veiculos.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^account/list/$',         UsersListView.as_view(),
        name='account_users_list'),

    url(r'^ajax/notify/mail/',
        MailNotifyView.as_view(),
        name='mailnotifyview'
        ),
    url(r'^ajax/notify/notifications/',
        NotificationsView.as_view(),
        name='notificationsview'
        ),
    url(r'^ajax/notify/tasks/',
        TasksNotifyView.as_view(),
        name='tasksnotifyview'
        ),
    url(r'^ajax/modal-content/modal-voicecommand/',
        ModalVoicecommandView.as_view(),
        ),
    url(r'^$',
        Home.as_view(),
        name='home_view'
        ),

)

THIRD_PARTY_URLS =  patterns('',
    url(r'^autocomplete/', include('autocomplete_light.urls')),

)

urlpatterns += THIRD_PARTY_URLS



js_info_dict = {
    'packages': ('django.conf',),
}

urlpatterns += patterns('',
   url(r'^inplaceeditform/', include('inplaceeditform.urls')),
   url(r'^jsi18n$', 'django.views.i18n.javascript_catalog', js_info_dict),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
