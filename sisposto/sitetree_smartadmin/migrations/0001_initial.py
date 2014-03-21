# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'SmartTreeItem'
        db.create_table(u'sitetree_smartadmin_smarttreeitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hint', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('urlaspattern', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('tree', self.gf('django.db.models.fields.related.ForeignKey')(related_name='smarttreeitem_tree',
                                                                           to=orm['sitetree.Tree'])),
            ('hidden', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            (
            'alias', self.gf('sitetree.models.CharFieldNullable')(db_index=True, max_length=80, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('inmenu', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('inbreadcrumbs', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('insitetree', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('access_loggedin', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('access_guest', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('access_restricted', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('access_perm_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('parent',
             self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='smarttreeitem_parent',
                                                                   null=True,
                                                                   to=orm['sitetree_smartadmin.SmartTreeItem'])),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('icon_css_class', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('show_icon', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sitetree_smartadmin', ['SmartTreeItem'])

        # Adding unique constraint on 'SmartTreeItem', fields ['tree', 'alias']
        db.create_unique(u'sitetree_smartadmin_smarttreeitem', ['tree_id', 'alias'])

        # Adding M2M table for field access_permissions on 'SmartTreeItem'
        m2m_table_name = db.shorten_name(u'sitetree_smartadmin_smarttreeitem_access_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('smarttreeitem', models.ForeignKey(orm[u'sitetree_smartadmin.smarttreeitem'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['smarttreeitem_id', 'permission_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'SmartTreeItem', fields ['tree', 'alias']
        db.delete_unique(u'sitetree_smartadmin_smarttreeitem', ['tree_id', 'alias'])

        # Deleting model 'SmartTreeItem'
        db.delete_table(u'sitetree_smartadmin_smarttreeitem')

        # Removing M2M table for field access_permissions on 'SmartTreeItem'
        db.delete_table(db.shorten_name(u'sitetree_smartadmin_smarttreeitem_access_permissions'))


    models = {
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')",
                     'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': (
            'django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sitetree.tree': {
            'Meta': {'object_name': 'Tree'},
            'alias': (
            'django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'sitetree_smartadmin.smarttreeitem': {
            'Meta': {'unique_together': "(('tree', 'alias'),)", 'object_name': 'SmartTreeItem'},
            'access_guest': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'access_loggedin': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'access_perm_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'access_permissions': ('django.db.models.fields.related.ManyToManyField', [],
                                   {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'access_restricted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'alias': ('sitetree.models.CharFieldNullable', [],
                      {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'hint': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'icon_css_class': (
            'django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inbreadcrumbs': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'inmenu': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'insitetree': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [],
                       {'blank': 'True', 'related_name': "'smarttreeitem_parent'", 'null': 'True',
                        'to': u"orm['sitetree_smartadmin.SmartTreeItem']"}),
            'show_icon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree': ('django.db.models.fields.related.ForeignKey', [],
                     {'related_name': "'smarttreeitem_tree'", 'to': u"orm['sitetree.Tree']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'urlaspattern': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'})
        }
    }

    complete_apps = ['sitetree_smartadmin', 'sitetree']
