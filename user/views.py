from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User
@api_view(['GET'])
def user_view(request, format=None):
    return Response({'foo': 'bar'})

@api_view(['PUT'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'user_id': user.id})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)    
    
    
    
    
    
    