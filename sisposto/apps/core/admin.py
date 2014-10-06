from django.contrib import admin

# Register your models here.
from django.utils.translation import ugettext_lazy as _
# Register your models here.
from sitetree.admin import TreeItemAdmin, TreeAdmin, override_tree_admin, override_item_admin


# And our custom tree item admin model.
class CustomTreeItemAdmin(TreeItemAdmin):
    # That will turn a tree item representation from the default variant
    # with collapsible groupings into a flat one.
    fieldsets = (
        (_('Basic settings'), {
            'fields': ('parent', 'title', 'url',)
        }),
        (_('Access settings'), {
            'classes': ('collapse',),
            'fields': ('access_loggedin', 'access_guest', 'access_restricted', 'access_permissions', 'access_perm_type')
        }),
        (_('Display settings'), {
            'classes': ('collapse',),
            'fields': ('hidden', 'inmenu', 'inbreadcrumbs', 'insitetree')
        }),
        (_('Additional settings'), {
            'classes': ('collapse',),
            'fields': ('hint', 'description', 'alias', 'urlaspattern')
        }),
        (_('Additional display settings'), {
            'classes': ('collapse',),
            'fields': ('icon_css_class', 'show_icon',)
        })
    )

# Now we tell the SiteTree to replace generic representations with custom.

override_item_admin(CustomTreeItemAdmin)


from apps.utils.autoregister import autoregister_admin

from . import models
autoregister_admin(models)