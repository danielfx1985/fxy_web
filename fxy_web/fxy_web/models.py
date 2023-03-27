from django.db import models





class news(models.Model):
    def __str__(self):
        return self.content

    title=models.CharField(max_length=500)
    content=models.CharField(max_length=1500)
    #pubdate=models.DateTimeField('date published')