# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Plane'
        db.create_table(u'hawaii_plane', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('starting', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('destination', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('company', self.gf('django.db.models.fields.CharField')(default=u'\u590f\u5a01\u5937\u822a\u7a7a', max_length=32)),
            ('departure', self.gf('django.db.models.fields.TimeField')()),
            ('arrival', self.gf('django.db.models.fields.TimeField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'plane', ['Plane'])


    def backwards(self, orm):
        # Deleting model 'Plane'
        db.delete_table(u'hawaii_plane')


    models = {
        u'plane.plane': {
            'Meta': {'object_name': 'Plane', 'db_table': "u'hawaii_plane'"},
            'arrival': ('django.db.models.fields.TimeField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'default': "u'\\u590f\\u5a01\\u5937\\u822a\\u7a7a'", 'max_length': '32'}),
            'departure': ('django.db.models.fields.TimeField', [], {}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'starting': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['plane']