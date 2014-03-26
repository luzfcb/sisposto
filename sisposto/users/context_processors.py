# -*- coding: utf-8 -*-

# TODO - checar implementacao
def posto(request):
    """
    Returns context variables required by apps that use Django's authentication
    system.

    If there is no 'user' attribute in the request, uses AnonymousUser (from
    django.contrib.auth).
    """
    if hasattr(request, 'user'):
        user = request.user
        posto_atual = 'Brasilia'
        postos = None
    else:
        posto_atual = None
        postos = None

    return {
        'posto_atual': posto_atual,
        'postos': postos,
    }