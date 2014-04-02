# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Meetup'
        db.create_table(u'meetups_meetup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('event_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 1, 0, 0))),
            ('location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'meetups', ['Meetup'])

        # Adding M2M table for field attendees on 'Meetup'
        m2m_table_name = db.shorten_name(u'meetups_meetup_attendees')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('meetup', models.ForeignKey(orm[u'meetups.meetup'], null=False)),
            ('attendee', models.ForeignKey(orm[u'meetups.attendee'], null=False))
        ))
        db.create_unique(m2m_table_name, ['meetup_id', 'attendee_id'])

        # Adding model 'Attendee'
        db.create_table(u'meetups_attendee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'meetups', ['Attendee'])


    def backwards(self, orm):
        # Deleting model 'Meetup'
        db.delete_table(u'meetups_meetup')

        # Removing M2M table for field attendees on 'Meetup'
        db.delete_table(db.shorten_name(u'meetups_meetup_attendees'))

        # Deleting model 'Attendee'
        db.delete_table(u'meetups_attendee')


    models = {
        u'meetups.attendee': {
            'Meta': {'object_name': 'Attendee'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'meetups.meetup': {
            'Meta': {'object_name': 'Meetup'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attendees': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['meetups.Attendee']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 1, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['meetups']