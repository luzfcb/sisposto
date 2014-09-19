# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from core.views import Home, MailNotifyView, TasksNotifyView, NotificationsView, ModalVoicecommandView


urlpatterns = patterns('',


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^account/', include('account.urls')),

    url(r'^ajax/notify/mail/',
        MailNotifyView.as_view(),
        ),
    url(r'^ajax/notify/notifications/',
        NotificationsView.as_view(),
        ),
    url(r'^ajax/notify/tasks/',
        TasksNotifyView.as_view(),
        ),
    url(r'^ajax/modal-content/modal-voicecommand/',
        ModalVoicecommandView.as_view(),
        ),
    url(r'^$',
        Home.as_view(),
        name='home_view'
        ),
)



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
