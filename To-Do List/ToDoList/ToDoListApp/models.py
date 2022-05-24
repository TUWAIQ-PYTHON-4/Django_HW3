from django.db import models

# Create your models here.


class Users(models.Model):
     name = models.CharField(max_length=50, help_text=" user name ")
     def __str__(self):
         return self.name


class  Tasks (models.Model):
    userId = models.ForeignKey(Users,on_delete=models.CASCADE)
    Titel = models.CharField(max_length=50 , help_text="titel task")
    date_created = models.DateTimeField(auto_now_add=True, help_text = "The date and time the review was created.")
    def __str__(self):
        return self.Titel