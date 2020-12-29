from django.db import models

# Create your models here.
class Quiz(models.Model):
	question = models.TextField(max_length = 500)
	option1 = models.TextField()
	option2 = models.TextField()
	option3 = models.TextField()
	option4 = models.TextField()
	answer = models.TextField(null=True)
