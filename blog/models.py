from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=None)
    date = models.DateField()

    def __str__(self):
        return self.title
>>>>>>> 1bf9651 (trying to display favicon)
