from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField()
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title



    


