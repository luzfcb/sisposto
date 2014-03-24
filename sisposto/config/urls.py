# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView, RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from main.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        HomeView.as_view(),
        name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),
    url(r'^ajax/notify/mail/$', 'core.views.mail', name='mail_ajax'),
    url(r'^ajax/notify/notifications/$', 'core.views.notifications', name='notification_ajax'),
    url(r'^ajax/notify/tasks/$', 'core.views.task', name='task_ajax'),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^usuarios/', include("users.urls", namespace="users")),
    url(r'^usuario/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/smartadmin/img/favicon/favicon.ico'), name='favicon'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
