from django.db import models

# Create your models here.

class Item(models.Model):

    # django automatically creates an id field for the table
    # I created a name field below
    name = models.CharField(max_length=12,verbose_name="name",null=False,blank=False)

    def __str__(self):
        return self.name
