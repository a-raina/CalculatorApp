from django.db import models

class Calculation(models.Model):
    user = models.CharField(max_length=200)
    calculation = models.CharField(max_length=200)
    
    def logEntry(self):
        self.save()
