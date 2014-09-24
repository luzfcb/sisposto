from django.db import models

# Create your models here.
from django.utils.translation import ugettext as _
from sitetree.models import TreeItemBase


class SmartTreeItem(TreeItemBase):

    icon_css_class = models.CharField(_('CSS class of icon'), max_length=50, null=True, blank=True)
    show_icon = models.BooleanField(_('Show icon of this item'), default=False)
