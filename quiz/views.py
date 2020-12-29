from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from quiz.models import Quiz
from .serializers import QuizApiSerializer

class QuizApiList(APIView):

	def get(self, request):
		quizapis = Quiz.objects.all()
		serializer = QuizApiSerializer(quizapis, many = True)
		return Response(serializer.data)

	def post(self):
		pass
	
	
def qpage(request):
	questions = Quiz.objects.all()

	return render(request, 'quiz/quiz.html', { 'questions': questions})

def index(request):
	return render(request, 'quiz/index.html')

def questions(request):
	return render(request, 'quiz/quiz.html')

def login(request):
	return render(request, 'quiz/login.html')