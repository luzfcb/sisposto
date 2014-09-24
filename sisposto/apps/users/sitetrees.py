# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from sitetree.utils import tree, item


    # url(r"^signup/$", SignupView.as_view(), name="account_signup"),
    # url(r"^login/$", LoginView.as_view(), name="account_login"),
    # url(r"^logout/$", LogoutView.as_view(), name="account_logout"),
    # url(r"^confirm_email/(?P<key>\w+)/$", ConfirmEmailView.as_view(), name="account_confirm_email"),
    # url(r"^password/$", ChangePasswordView.as_view(), name="account_password"),
    # url(r"^password/reset/$", PasswordResetView.as_view(), name="account_password_reset"),
    # url(r"^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetTokenView.as_view(), name="account_password_reset_token"),
    # url(r"^settings/$", SettingsView.as_view(), name="account_settings"),
    # url(r"^delete/$", DeleteView.as_view(), name="account_delete"),


# """Dynamically creates and returns a sitetree item object.
# def item
# :param str title:
# :param str url:
# :param list, set children: a list of children for tree item. Children should also be created by `item` function.
# :param bool url_as_pattern: consider URL as a name of a named URL
# :param str hint: hints are usually shown to users
# :param str alias: item name to address it from templates
# :param str description: additional information on item (usually is not shown to users)
# :param bool in_menu: show this item in menus
# :param bool in_breadcrumbs: show this item in breadcrumbs
# :param bool in_sitetree: show this item in sitetrees
# :param bool access_loggedin: show item to logged in users only
# :param bool access_guest: show item to guest users only
# :param list, str, int, Permission access_by_perms: restrict access to users with these permissions
# :param bool perms_mode_all: permissions set interpretation rule:
#             True - user should have all the permissions;
#             False - user should have any of chosen permissions.
# :return:
# """

# Be sure you defined `sitetrees` in your module.
sitetrees = (
    # Define a tree with `tree` function.
    tree('sitemenus', items=[
        # Then define items and their children with `item` function.
        item('Gerência', '#', url_as_pattern=False, children=[
            item('Usuarios', '#', url_as_pattern=False, children=[
                item('Dashboard', 'account_users_list'),
                item('Add a book', 'tasksnotifyview'),
                item('Edit ', 'tasksnotifyview', in_menu=False, in_sitetree=False)
            ]),
            item('Postos', '#', url_as_pattern=False, children=[
                item('Postos', '#', url_as_pattern=False, children=[
                    item('Bombas', '#', url_as_pattern=False),
                    item('Tanques', '#', url_as_pattern=False),
                ])
            ]),
            item('Veiculos', '#', url_as_pattern=False, children=[
                item('Veiculos', '#', url_as_pattern=False,),
            ]),
        ]),
        item('Abastecimento', '#', url_as_pattern=False, children=[
            item('Abastecer', '#', url_as_pattern=False, ),
            item('Postos', '#', url_as_pattern=False, children=[
                item('Postos', '#', url_as_pattern=False, children=[
                    item('Bombas', '#', url_as_pattern=False),
                    item('Tanques', '#', url_as_pattern=False),
                ])
            ]),
            item('Veiculos', '#', url_as_pattern=False, children=[
                item('Veiculos', '#', url_as_pattern=False,),
            ]),
        ]),

    ]),
    tree('sitemenus', items=[
        # Then define items and their children with `item` function.
        item('Gerência', '#', url_as_pattern=False, children=[
            item('Usuarios', '#', url_as_pattern=False, children=[
                item('Dashboard', 'account_users_list'),
                item('Add a book', 'tasksnotifyview'),
                item('Edit ', 'tasksnotifyview', in_menu=False, in_sitetree=False)
            ]),
        ]),
    ])
)
