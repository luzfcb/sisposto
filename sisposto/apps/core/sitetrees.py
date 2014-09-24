# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from sitetree.utils import tree, item

# Be sure you defined `sitetrees` in your module.
sitetrees = (
    # Define a tree with `tree` function.
    tree('sitemenus', items=[
        item('Vistoria', '#', url_as_pattern=False, children=[
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
        ])
    ]),
    # ... You can define more than one tree for your app.
)
