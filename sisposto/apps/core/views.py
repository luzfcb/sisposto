from django.shortcuts import render
from braces.views import AjaxResponseMixin

# Create your views here.
from django.views import generic


class Home(generic.TemplateView):
    template_name = 'account/settings.html'


class NotificationsView(AjaxResponseMixin, generic.TemplateView):
    template_name = 'smartadmin/ajax/notify/notifications.html'


class TasksNotifyView(AjaxResponseMixin, generic.TemplateView):
    template_name = 'smartadmin/ajax/notify/tasks.html'


class MailNotifyView(AjaxResponseMixin, generic.TemplateView):
    template_name = 'smartadmin/ajax/notify/mail.html'


class ModalVoicecommandView(AjaxResponseMixin, generic.TemplateView):
    template_name = 'smartadmin/ajax/modal-content/modal-voicecommand.html'
