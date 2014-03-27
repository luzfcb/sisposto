# -*- coding: utf8 -*-
import re
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import RedirectView
from .models import Pessoa


from django.utils import six

import logging

MIDDLEWARE_DISABLE = getattr(settings, 'USERS_MIDDLEWARE_DISABLE', False)

logger = logging.getLogger(__name__)


URLS_EXCLUIDAS = [
    # casa exatamente com a string
    r'^(%s)$' % '|'.join([reverse('users:update'), reverse('account_logout')]),

    # casa obrigatoriamente com o inicio da string
    r'^(?:%s)' % '|'.join([settings.MEDIA_URL,
                           settings.STATIC_URL,
                           '/__debug__/']),
]


profile_update_url_re = re.compile(r'%s' % '|'.join(URLS_EXCLUIDAS), re.I)

# TODO - checar implementacao
class UsersMiddleware(object):
    def process_request(self, request):
        if not MIDDLEWARE_DISABLE:
            if request.user:
                if request.user.is_authenticated():
                    if not isinstance(request.user, AnonymousUser):
                        try:
                            profile = Pessoa.objects.get(user=request.user)
                            if not profile.cadastro_concluido:
                                if not profile_update_url_re.match(request.path):
                                    return redirect('users:update')
                        except Pessoa.DoesNotExist as e:
                            logger.debug(e.message)
                            if not profile_update_url_re.match(request.path):
                                return redirect('users:update')
                else:
                    print('NÃO esta autenticado')
                    #request.session['postos_disponiveis'] = "MUITOS POSTOS"

