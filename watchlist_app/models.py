from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True) #if the movie is relesed then active = true 
    
    def __str__(self):
        return self.name
    
    # to convert to sql run python manage.py makemigrations, 
    # #then check __init__.py in migrations folder, you will see sql commands for creating table and inserting data.
    # to apply changes to the database run python manage.py migrate.