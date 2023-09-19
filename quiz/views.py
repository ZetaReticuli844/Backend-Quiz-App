from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz, Question, Choice, UserResponse
from .serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer, UserResponseSerializer

@api_view(['GET'])
def quiz_list(request):
    quizzes = Quiz.objects.all()
    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def quiz_create(request):
    serializer = QuizSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    serializer = QuizSerializer(quiz)
    return Response(serializer.data)

@api_view(['POST'])
def question_create(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(quiz=quiz)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def choice_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(question=question)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_response_create(request):
    serializer = UserResponseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_response_list(request, quiz_id):
    user_responses = UserResponse.objects.filter(quiz_id=quiz_id)
    serializer = UserResponseSerializer(user_responses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_response_detail(request, user_response_id):
    user_response = get_object_or_404(UserResponse, pk=user_response_id)
    serializer = UserResponseSerializer(user_response)
    return Response(serializer.data)