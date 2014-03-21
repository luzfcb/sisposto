# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trabalham'
        db.create_table(u'users_trabalham', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trabalhos', to=orm['users.Pessoa'])),
            ('posto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trabalhadores', to=orm['users.Posto'])),
            ('registro', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'users', ['Trabalham'])

        # Adding model 'SubempresaEmpresa'
        db.create_table(u'users_subempresaempresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.SecretariaEstado'])),
            ('subempresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.SubEmpresa'])),
            ('data_vinculo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('data_desvinculo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['SubempresaEmpresa'])

        # Adding model 'Posto'
        db.create_table(u'users_posto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'users', ['Posto'])

        # Adding model 'Estado'
        db.create_table(u'users_estado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'users', ['Estado'])

        # Adding model 'SubEmpresa'
        db.create_table(u'users_subempresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'users', ['SubEmpresa'])

        # Adding model 'Pessoa'
        db.create_table(u'users_pessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='profile', unique=True, null=True, to=orm['users.User'])),
            ('nome_completo', self.gf('django.db.models.fields.CharField')(max_length=85)),
            ('data_de_nascimento', self.gf('django.db.models.fields.DateField')(null=True)),
            ('naturalidade', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cadastro_concluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'users', ['Pessoa'])

        # Adding model 'SecretariaEstado'
        db.create_table(u'users_secretariaestado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.related.OneToOneField')(related_name='secretarias', unique=True, to=orm['users.Estado'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'users', ['SecretariaEstado'])


    def backwards(self, orm):
        # Deleting model 'Trabalham'
        db.delete_table(u'users_trabalham')

        # Deleting model 'SubempresaEmpresa'
        db.delete_table(u'users_subempresaempresa')

        # Deleting model 'Posto'
        db.delete_table(u'users_posto')

        # Deleting model 'Estado'
        db.delete_table(u'users_estado')

        # Deleting model 'SubEmpresa'
        db.delete_table(u'users_subempresa')

        # Deleting model 'Pessoa'
        db.delete_table(u'users_pessoa')

        # Deleting model 'SecretariaEstado'
        db.delete_table(u'users_secretariaestado')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.estado': {
            'Meta': {'object_name': 'Estado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'users.pessoa': {
            'Meta': {'object_name': 'Pessoa'},
            'cadastro_concluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_de_nascimento': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naturalidade': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nome_completo': ('django.db.models.fields.CharField', [], {'max_length': '85'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'profile'", 'unique': 'True', 'null': 'True', 'to': u"orm['users.User']"})
        },
        u'users.posto': {
            'Meta': {'object_name': 'Posto'},
            'funcionarios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['users.Pessoa']", 'through': u"orm['users.Trabalham']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'users.secretariaestado': {
            'Meta': {'object_name': 'SecretariaEstado'},
            'estado': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'secretarias'", 'unique': 'True', 'to': u"orm['users.Estado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subempresas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['users.SubEmpresa']", 'through': u"orm['users.SubempresaEmpresa']", 'symmetrical': 'False'})
        },
        u'users.subempresa': {
            'Meta': {'object_name': 'SubEmpresa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'users.subempresaempresa': {
            'Meta': {'object_name': 'SubempresaEmpresa'},
            'data_desvinculo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'data_vinculo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.SecretariaEstado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subempresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.SubEmpresa']"})
        },
        u'users.trabalham': {
            'Meta': {'object_name': 'Trabalham'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trabalhos'", 'to': u"orm['users.Pessoa']"}),
            'posto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trabalhadores'", 'to': u"orm['users.Posto']"}),
            'registro': ('django.db.models.fields.TextField', [], {})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['users']