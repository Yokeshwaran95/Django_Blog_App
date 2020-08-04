from blog_app.models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Post
		fields=("title","content","pictures","category")