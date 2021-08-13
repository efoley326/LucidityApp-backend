
from rest_framework import serializers
from .models import User, Event, Document, Alert, Note, VolunteerSlot, StatusBar, Tag


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'id', 'display_name','legal_name','pronouns', 'availability', 'email', 'telephone', 
        'address2', 'city','state','zipcode', 'user_status',
        'intake_status','preferred_event']

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['user', 'title', 'date', 'start_time', 'end_time', 'type', 'description']

class UrlSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Document
        fields = ['url']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['user', 'title', 'summary', 'body', 'url', 'required']


class AlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alert
        fields = ['user', 'title', 'date','text']


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['user','text']


class VolunteerSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = VolunteerSlot
        fields = ['user', 'text_slot', 'event', 'time']


class StatusBarSerializer(serializers.ModelSerializer):
    required = serializers.ReadOnlyField(source='Document.required')

    class Meta:
        model = StatusBar
        fields = ['user', 'unfinished', 'pending', 'approved', 'complete']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['user', 'text', 'event']