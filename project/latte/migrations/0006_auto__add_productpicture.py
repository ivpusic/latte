# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductPicture'
        db.create_table('latte_productpicture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_picture', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['latte.Product'])),
        ))
        db.send_create_signal('latte', ['ProductPicture'])


    def backwards(self, orm):
        # Deleting model 'ProductPicture'
        db.delete_table('latte_productpicture')


    models = {
        'latte.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'latte.productpicture': {
            'Meta': {'object_name': 'ProductPicture'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['latte.Product']"}),
            'product_picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
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