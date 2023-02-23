from django.db import models

from accounts.models import CustomUser



class HighEduInstitution(models.Model):
    author = models.ForeignKey(CustomUser, related_name='heis', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)

    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.name = ' '.join(self.name.strip().split())
        super().save(*args, **kwargs)




    




