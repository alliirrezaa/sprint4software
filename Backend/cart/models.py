from django.db import models
from accounts.models import User
from home.models import Forms

class Cart(models.Model):
    form=models.ForeignKey(Forms,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username