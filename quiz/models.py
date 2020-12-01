from django.db import models

# Create your models here.
class Quiz(models.Model):
	question = models.TextField(max_length = 500)
	option1 = models.TextField(max_length = 20)
	option2 = models.TextField(max_length = 20)
	option3 = models.TextField(max_length = 20)
	option4 = models.TextField(max_length = 20)
	answer = models.TextField(max_length = 20, null=True)
