from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from quiz import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('quiz.urls')), 
	# url(r'^index/', views.index),
	# url(r'^login/$', views.login),
	# url(r'^quizapi/', views.QuizApiList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)