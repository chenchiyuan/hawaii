# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PlaneInventory'
        db.create_table(u'hawaii_plane_inventory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plane', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plane.Plane'])),
            ('departure', self.gf('django.db.models.fields.DateTimeField')()),
            ('arrival', self.gf('django.db.models.fields.DateTimeField')()),
            ('seat', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.CharField')(default=u'\u5546\u52a1\u8231', max_length=32)),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('child_price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('amount_limit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('baggage_limit', self.gf('django.db.models.fields.CharField')(default=u'20KG', max_length=32)),
            ('limit', self.gf('django.db.models.fields.CharField')(default=u'\u4e0d\u80fd\u9000\u7968', max_length=2056, blank=True)),
        ))
        db.send_create_signal(u'plane', ['PlaneInventory'])

        # Deleting field 'Plane.arrival'
        db.delete_column(u'hawaii_plane', 'arrival')

        # Deleting field 'Plane.departure'
        db.delete_column(u'hawaii_plane', 'departure')

        # Deleting field 'Plane.id'
        db.delete_column(u'hawaii_plane', u'id')


        # Changing field 'Plane.number'
        db.alter_column(u'hawaii_plane', 'number', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True))

    def backwards(self, orm):
        # Deleting model 'PlaneInventory'
        db.delete_table(u'hawaii_plane_inventory')

        # Adding field 'Plane.arrival'
        db.add_column(u'hawaii_plane', 'arrival',
                      self.gf('django.db.models.fields.TimeField')(default=None),
                      keep_default=False)

        # Adding field 'Plane.departure'
        db.add_column(u'hawaii_plane', 'departure',
                      self.gf('django.db.models.fields.TimeField')(default=None),
                      keep_default=False)

        # Adding field 'Plane.id'
        db.add_column(u'hawaii_plane', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)


        # Changing field 'Plane.number'
        db.alter_column(u'hawaii_plane', 'number', self.gf('django.db.models.fields.CharField')(max_length=32, unique=True))

    models = {
        u'plane.plane': {
            'Meta': {'object_name': 'Plane', 'db_table': "u'hawaii_plane'"},
            'company': ('django.db.models.fields.CharField', [], {'default': "u'\\u590f\\u5a01\\u5937\\u822a\\u7a7a'", 'max_length': '32'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'starting': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'plane.planeinventory': {
            'Meta': {'object_name': 'PlaneInventory', 'db_table': "u'hawaii_plane_inventory'"},
            'amount_limit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'arrival': ('django.db.models.fields.DateTimeField', [], {}),
            'baggage_limit': ('django.db.models.fields.CharField', [], {'default': "u'20KG'", 'max_length': '32'}),
            'child_price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'departure': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit': ('django.db.models.fields.CharField', [], {'default': "u'\\u4e0d\\u80fd\\u9000\\u7968'", 'max_length': '2056', 'blank': 'True'}),
            'plane': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plane.Plane']"}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'seat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "u'\\u5546\\u52a1\\u8231'", 'max_length': '32'})
        }
    }

    complete_apps = ['plane']