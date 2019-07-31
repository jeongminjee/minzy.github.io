from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:150]

    
    

class Comment(models.Model):
   post = models.ForeignKey(Blog, on_delete=models.CASCADE,null=True, related_name='comments')
   author = models.CharField(max_length=200)
   text = models.TextField()
   created_date = models.DateTimeField(default=False, null=True)


   def approve(self):
       self.approved_comment = True
       self.save()

   def __str__(self):
       return self.comment

