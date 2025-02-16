from django.db import models
from django.contrib.auth.models import User

class SecurityQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    securityAnswer = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.id) + ' - ' + self.securityAnswer