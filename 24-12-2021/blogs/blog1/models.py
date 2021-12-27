from django.db import models

# Create your models here.
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class signup(models.Model):
      First_name=models.CharField(max_length=100)
      Last_name=models.CharField(max_length=100)
      Phone_no=models.IntegerField()
      Email=models.CharField(max_length=100)
      Password=models.CharField(max_length=100)
      confirm_password=models.CharField(max_length=100)

      def __str__(self):
          return self.First_name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image=models.ImageField(upload_to='images/',blank=True,null=True,verbose_name="")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_profile_picture(self):
        if self.image:
            return self.image
        else:
            return 'your_default_img_url_path'
