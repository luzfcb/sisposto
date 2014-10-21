# -*- coding: utf-8 -*-
'''
Local Configurations

- Runs in Debug mode
- Uses console backend for emails
- Use Django Debug Toolbar
- Use sqlite3 as database
'''
import platform
from os.path import join, dirname
from configurations import values
from .common import Common, BASE_DIR


class Local(Common):

    # DEBUG
    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = DEBUG
    # END DEBUG

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # Mail settings
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    # End mail settings

    # django-debug-toolbar
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)

    INSTALLED_APPS += ('django_nose',)
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

    NOSE_ARGS = [
        '--verbosity=2',
        '--with-coverage',
        '--cover-package=sisposto'
        # '--with-notify',
        # '--pdb-failures',
    ]

    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': [
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ],
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    # end django-debug-toolbar

    # DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    #DATABASES = values.DatabaseURLValue('postgres://localhost/projetosgt')
    #DB_NAME = 'sqlite:////{0}.sqlite'.format(join(BASE_DIR, 'projeto_posto'))

    if 'Windows' in platform.system():  # pragma: no cover
        DB_NAME = 'sqlite:\\{0}.sqlite'.format(join(BASE_DIR, 'projeto_posto'))
    else:
        DB_NAME = 'sqlite:////{0}.sqlite'.format(join(BASE_DIR, 'projeto_posto'))

    DATABASES = values.DatabaseURLValue(DB_NAME)
    # END DATABASE CONFIGURATION

    # Your local stuff: Below this line define 3rd party libary settings


# Hack feio para que o autocompletar do Pycharm Funcione quando se usa django-configuration
if 1 == 2:  # pragma: no cover
    INSTALLED_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.humanize',

        # Useful template tags:
        # 'django.contrib.humanize',

        # Admin
        'django.contrib.admin',
        'autoslug',
        'django_extensions',
        'crispy_forms',  # Form layouts
        'account',  # pinax django-user-accounts
        'sitetree',
        'apps.core',  #
        'apps.users',  # custom users app
        'django_tables2',
        'municipios',
        'autocomplete_light',
        'bootstrap3',
        'datetimewidget',
        'apps.posto',
        'apps.veiculos',
        'linaro_django_pagination',
        'resort',
        'coffee_table',
    )
    MIDDLEWARE_CLASSES = (
        # Make sure djangosecure.middleware.SecurityMiddleware is listed first
        'djangosecure.middleware.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    # TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
        # Your stuff: custom template context processers go here
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(BASE_DIR, 'templates'),
    )

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # END TEMPLATE CONFIGURATION

    # STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = join(dirname(BASE_DIR), 'staticfiles')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        join(BASE_DIR, 'static'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    # END STATIC FILE CONFIGURATION

    # MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(BASE_DIR, 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    # END MEDIA CONFIGURATION
