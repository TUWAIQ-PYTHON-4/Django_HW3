from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, help_text="The user name.")
    email = models.EmailField(help_text="The User email address.")

    def __str__(self) :
        return self.name

class Item(models.Model):
    to_do_item = models.CharField(max_length=50, help_text="The user to do item.")
    completed = models.BooleanField(default=False)
    to_do_list = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) :
        return self.to_do_item



'''
The CRUD commands:

from ToDoListApp.models import User, Item
User1 = User.objects.create(name="Bushra", email="bushra@example.com")
user2  = User.objects.create(name="lily", email="lily@example.com")
item1 = Item.objects.create(to_do_item= 'study',to_do_list= User1)
item2 = Item.objects.create(to_do_item= 'work', completed= True, to_do_list= User1)

User.objects.all()
user = User.objects.get(name='Bushra')
item = Item.objects.filter(to_do_list= User1)




'''