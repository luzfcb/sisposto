from django.db import models

# Create your models here.
from sitetree.models import TreeItemBase, TreeBase

# class SmartTree(TreeBase):
#     """This is your custom tree model.
#     And here you add `my_tree_field` to all fields existing in `TreeBase`.
#
#     """
#     my_tree_field = models.CharField('My tree field', max_length=50, null=True, blank=True)
#

class SmartTreeItem(TreeItemBase):
    icon_css_class = models.CharField('CSS class of icon', max_length=50, null=True, blank=True)
    show_icon = models.BooleanField('Show icon of item', default=False)

