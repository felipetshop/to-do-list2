from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    
    status = (
        ('doing', 'Em progresso'),
        ('done', 'Feito'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.CharField(
        max_length=9,
        choices= status,
        default='doing'
    )
    created_at= models.DateTimeField(auto_now_add=True)
    due_date= models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
