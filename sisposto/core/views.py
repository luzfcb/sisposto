from braces.views import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.


# class AutocompleteViewLoginRequired(LoginRequiredMixin, AutocompleteView):
#     pass
#
# class RegistryViewLoginRequired(LoginRequiredMixin, RegistryView):
#     pass
#
# class CreateViewLoginRequired(LoginRequiredMixin, CreateView):
#     pass
from django.views.generic import TemplateView



# class ColaboradorViewSet(CreateView):
#     model = Colaborador
#     success_url = reverse_lazy('home')
#     template_name = 'postos/abastecimento_form.html'


class MailNotifyView(TemplateView):
    template_name = 'smartadmin/ajax/notify/mail.html'

mail = MailNotifyView.as_view()

class NotificationsNotifyView(TemplateView):
    template_name = 'smartadmin/ajax/notify/notifications.html'

notifications = NotificationsNotifyView.as_view()

class TaskNotifyView(TemplateView):
    template_name = 'smartadmin/ajax/notify/tasks.html'

task = TaskNotifyView.as_view()
