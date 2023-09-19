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
    data = serializer.data
    
    # Calculate the number of questions the user got right
    quiz_id = data['quiz']
    quiz = Quiz.objects.get(pk=quiz_id)
    correct_choices = Choice.objects.filter(question__quiz=quiz, is_answer=True)
    user_choices = Choice.objects.filter(user_responses=user_response)
    num_correct = 0
    for choice in user_choices:
        if choice in correct_choices:
            num_correct += 1
    
    # Add the number of correct answers to the response data
    data['num_correct'] = num_correct
    
    return Response(data)