# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FileOwner'
        db.create_table(u'main_fileowner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'main', ['FileOwner'])

        # Adding model 'CodeFile'
        db.create_table(u'main_codefile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('trueorfalse', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['CodeFile'])


    def backwards(self, orm):
        # Deleting model 'FileOwner'
        db.delete_table(u'main_fileowner')

        # Deleting model 'CodeFile'
        db.delete_table(u'main_codefile')


    models = {
        u'main.codefile': {
            'Meta': {'object_name': 'CodeFile'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'trueorfalse': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'main.fileowner': {
            'Meta': {'object_name': 'FileOwner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['main']