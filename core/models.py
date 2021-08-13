from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import BooleanField, DateTimeField, TimeField

class User(AbstractUser):
    display_name = models.CharField(max_length=200, default="preferred name", blank=True, null=True)
    legal_name = models.CharField(max_length=200, default="full legal name", blank=True, null=True)
    pronouns = models.CharField(max_length=200, default="pronouns", blank=True, null=True)
    availability = models.TextField(max_length=500, default='availability', blank=True, null=True)
    email = models.EmailField(max_length=200, null=True, blank=True, default="e-mail address")
    telephone = models.CharField(max_length=250, default="10-digit phone number", blank=True, null=True)
    address2 = models.CharField(max_length=50, default="Address 2", blank=True, null=True)
    city = models.CharField(max_length=50, default="City", blank=True, null=True)
    state = models.CharField(max_length=50, default="State", blank=True, null=True)
    zipcode = models.CharField(max_length=10, default="Zipcode", blank=True, null=True)
    user_status = models.CharField(max_length=50, default="permissions status", blank=True, null=True)
    intake_status = models.CharField(max_length=50, default="volunteer status", blank=True, null=True)
    preferred_event = models.TextField(max_length=500, default="preferred events", blank=True, null=True)

class Event(models.Model):
    user = models.ManyToManyField(User, related_name="volunteer")
    title = models.CharField(max_length=250, primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    type = models.CharField(max_length=250)
    description = models.TextField()

class Document(models.Model):
    user = models.ManyToManyField(User, related_name="volunteer_form")
    title = models.CharField(max_length=250, primary_key=True)
    summary = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    required = models.BooleanField(null=True, blank=True, default=None)

class Alert(models.Model):
    user = models.ForeignKey(User, related_name="creator", on_delete=CASCADE)
    title = models.CharField(max_length=200, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

class Note(models.Model):
    user = models.ManyToManyField(User, related_name="note_creator")
    text = models.TextField(null=True, blank=True, primary_key=True)

class VolunteerSlot(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="slot_chooser")
    text_slot = models.TextField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=DO_NOTHING, related_name="event_slots")
    time = models.DateTimeField(null=True, blank=True)

class StatusBar(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="volunteer_status")
    unfinished = BooleanField(default=False, primary_key=True)
    pending = BooleanField(default=False)
    approved = BooleanField(default=False)
    complete = BooleanField(default=False)

class Tag(models.Model):
    user = models.ManyToManyField(User, related_name="tag")
    text = models.CharField(max_length=100, primary_key=True)
    event = models.ForeignKey(Event, on_delete=DO_NOTHING, related_name="event_tagged")
    










    
