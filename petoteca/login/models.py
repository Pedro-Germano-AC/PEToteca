from django.db import models
from django.contrib.auth.models import User 

class UserPET(User): 
    is_email_verificado = models.BooleanField(default=False)

    def __str__(self): 
        return self.username

