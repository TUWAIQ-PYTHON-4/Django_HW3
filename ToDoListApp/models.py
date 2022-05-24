from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50, help_text="The user's first name.")
    last_name = models.CharField(max_length=50, help_text="The user's last name.")

    def __str__(self) :
        return self.first_name+' '+self.last_name

class Item(models.Model):
    item = models.CharField(max_length=50, help_text="The item the user.")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time the review was created.")
    todo = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) :
        return self.item
   

 