from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from quiz import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login/$', views.login),
	url(r'^questions/', include('quiz.urls')),
	url(r'^quizapi/', views.QuizApiList.as_view()),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)