from .models import Event, Note, User
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import status,authentication, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import EventSerializer, NoteSerializer, UserSerializer
from core import serializers


@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def user_profile(request, pk):

    if request.method == 'GET':
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        serializer.is_valid()
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def registration(request, pk):
    if request.method == 'GET':
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    
    elif request.method == 'POST':
        fields = ('legal_name', 'address2', 'email','telephone', 'city', 'state', 'zipcode')
        user = User.object.filter(fields)
        serializer = UserSerializer(user)
        
        serializer.is_valid()
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def event(request):
    if request.method == 'GET':
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        serializer.is_valid()
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET'])
def eventDetail(request, pk):
    if request.method == 'GET':
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)

@api_view(['PUT'])
def eventEdit(request, pk):
    if request.method == 'PUT':
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(instance=event, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def eventDelete(request, pk):
    if request.method == 'DELETE':
        event = Event.objects.get(id=pk)
        event.delete()
        return Response('Event has been deleted')


@api_view(['GET', 'POST'])
def noteList(request):
    if request.method == 'GET':
        note = Note.objects.all()
        serializers = NoteSerializer(note, many=True)
        return Response (serializers.data)

    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def noteDetail(request, pk):
    if request.method == 'GET':
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)

@api_view(['GET'])
def noteEdit(request, pk):
    if request.method == 'GET':
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def noteDelete(request, pk):
    if request.method == 'DELETE':
        note = Note.objects.get(id=pk)
        note.delete()
        return Response('This note has been deleted')