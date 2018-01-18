
from django.db import models
from django.utils import timezone

class Post(models.Model): #defines our model that is named Post (which is an object)
    #defining the properties
    author = models.ForeignKey('auth.User') #ForeignKey is a link to another model
    title = models.CharField(max_length=200) #CharField is how you define text with a limited number of characters
    text = models.TextField() #TextField is for long text without a limit
    created_date = models.DateTimeField( #DateTimeField is a date and time
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title

