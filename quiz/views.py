from django.shortcuts import render
from quiz.models import Quiz

def qpage(request):
	questions = Quiz.objects.all()

	return render(request, 'quiz/quiz.html', { 'questions': questions})

def index(request):
	return render(request, 'quiz/index.html')

def questions(request):
	return render(request, 'quiz/quiz.html')

def login(request):
	return render(request, 'quiz/login.html')
	
	
