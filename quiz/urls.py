# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('', views.qpage, name='quiz'),
	path('index/', views.index, name='index'),
	path('login/', views.login, name='login'),
	path('quizapi', views.QuizApiList.as_view())
]
