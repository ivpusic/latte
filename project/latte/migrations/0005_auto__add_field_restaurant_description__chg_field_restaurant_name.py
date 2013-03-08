# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Restaurant.description'
        db.add_column('latte_restaurant', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


        # Changing field 'Restaurant.name'
        db.alter_column('latte_restaurant', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'Restaurant.description'
        db.delete_column('latte_restaurant', 'description')


        # Changing field 'Restaurant.name'
        db.alter_column('latte_restaurant', 'name', self.gf('django.db.models.fields.TextField')())

    models = {
        'latte.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'latte.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['latte.Product']", 'through': "orm['latte.RestaurantProduct']", 'symmetrical': 'False'})
        },
        'latte.restaurantproduct': {
            'Meta': {'object_name': 'RestaurantProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['latte.Product']"}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['latte.Restaurant']"})
        }
    }

    complete_apps = ['latte']