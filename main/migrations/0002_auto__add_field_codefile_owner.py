# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CodeFile.owner'
        db.add_column(u'main_codefile', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.FileOwner'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CodeFile.owner'
        db.delete_column(u'main_codefile', 'owner_id')


    models = {
        u'main.codefile': {
            'Meta': {'object_name': 'CodeFile'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.FileOwner']", 'null': 'True', 'blank': 'True'}),
            'trueorfalse': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'main.fileowner': {
            'Meta': {'object_name': 'FileOwner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['main']