from django.db import models
from django.conf import settings
from blog_app.utils import unique_slug_generator
from django.urls import reverse
from django.shortcuts import redirect
from django.db.models.signals import pre_save,post_save
# Create your models here.
User=settings.AUTH_USER_MODEL
Status=(
	(0,"Draft"),
	(1,"Publish")
)
Category=(
	("Automotive","Automotive"),
	("Gadgets","Gadgets"),
	("Science","Science"),
	("Technology","Technology"))
class Post(models.Model):
	title=models.CharField(max_length=200,unique=True)
	slug=models.SlugField(max_length=200,null=True, blank=True)
	author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog_posts")
	updated_on=models.DateTimeField(auto_now=True)
	content=models.TextField()
	created_on=models.DateTimeField(auto_now_add=True)
	status=models.IntegerField(choices=Status,default=0)
	category=models.IntegerField(choices=Category,default="Automotive")
	pictures=models.ImageField(upload_to='images',default=None,blank=True,null=True)

	class Meta:
		ordering=['-created_on']

	# def get_absolute_url(self):
	# 	return redirect("Home")

	def __str__(self):
		return self.title


class Comment(models.Model):
	post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
	name=models.CharField(max_length=100)
	email=models.EmailField()
	body=models.TextField()
	created_on=models.DateTimeField(auto_now_add=True)
	active=models.BooleanField(default=False)

	class Meta:
		ordering=['-created_on']

	def __str__(self):
		return 'Comment {} by {}'.format(self.body,self.name)

# def rl_pre_save_receiver(sender,instance, *args, **kwargs):
# 	print('saving...')
# 	print(instance.timestamp)
# 	if not instance.slug:
# 		instance.slug=unique_slug_generator(instance)

# def rl_post_save_receiver(sender,instance, *args, **kwargs):
# 	print('saved...')
# 	print(instance.timestamp)

def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 

pre_save.connect(pre_save_receiver, sender = Post) 