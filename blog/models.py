from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=50)
    images = models.ImageField(upload_to='images/blog/')
    article = models.TextField()
    pub_date = models.DateTimeField()



