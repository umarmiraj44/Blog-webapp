from django.db import models
class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    on_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    

    

# Create your models here.
