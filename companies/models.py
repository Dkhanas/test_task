from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

import mptt


class MainCompany(models.Model):
    name = models.CharField(u"Main company", max_length=30, default='')
    annual_earning = models.PositiveIntegerField(u"Annual earning", blank=True,
                                                 null=True, default=0)

    class Meta:
        db_table = 'main_company'
        verbose_name = u"MainCompany"

    def __unicode__(self):
        return '{}'.format(self.name)


class SubsidiaryCompany(MPTTModel):
    name = models.CharField(u"Subsidiary company", max_length=30, default='')
    annual_earning = models.PositiveIntegerField(u"Annual earning", blank=True,
                                                 null=True, default=0)
    main_company = models.ForeignKey(MainCompany, blank=True, null=True,
                                     related_name=u"child_from_main",
                                     default='')
    parent = TreeForeignKey('self', related_name=u"child_from_sub",
                            blank=True, null=True, default='')

    class Meta:
        verbose_name = u"SubsidiaryCompany"
        ordering = ('tree_id', 'level')

    def __unicode__(self):
        return '{}'.format(self.name)

    class MPTTMeta:
        order_insertion_py = ['name']


mptt.register(SubsidiaryCompany, order_insertion_py=['name'])
