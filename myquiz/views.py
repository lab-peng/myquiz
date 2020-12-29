from django.shortcuts import render

def index(request):
	return render(request, 'quiz/index.html')

def questions(request):
	return render(request, 'quiz/quiz.html')

def login(request):
	return render(request, 'quiz/login.html')

