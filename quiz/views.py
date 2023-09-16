from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def quiz_view(request, format=None):
    return Response({'quiz1': 'hello'})