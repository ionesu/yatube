# из модуля db импортируем класс models
from django.db import models
# из модуля auth импортируем функцию get_user_model 
from django.contrib.auth import get_user_model 

User = get_user_model()

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
