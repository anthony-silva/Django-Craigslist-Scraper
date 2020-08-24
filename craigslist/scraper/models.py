from django.db import models

# Create your models here.
class Search(models.Model):
    city = models.CharField(max_length=50, default=None, null=False)
    search = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)
