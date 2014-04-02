# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Attendee.status'
        db.delete_column(u'meetups_attendee', 'status')

        # Adding field 'Attendee.profession'
        db.add_column(u'meetups_attendee', 'profession',
                      self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Attendee.email'
        db.add_column(u'meetups_attendee', 'email',
                      self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Attendee.status'
        db.add_column(u'meetups_attendee', 'status',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=20),
                      keep_default=False)

        # Deleting field 'Attendee.profession'
        db.delete_column(u'meetups_attendee', 'profession')

        # Deleting field 'Attendee.email'
        db.delete_column(u'meetups_attendee', 'email')


    models = {
        u'meetups.attendee': {
            'Meta': {'object_name': 'Attendee'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        u'meetups.meetup': {
            'Meta': {'object_name': 'Meetup'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attendees': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['meetups.Attendee']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 2, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['meetups']