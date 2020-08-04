from blog_app.models import (
	Comment, Post )
from django import forms

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=('name','email','body')


class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=("title","content","pictures","category")

class ContactForm(forms.Form):
	contact_name=forms.CharField(required=True)
	contact_email=forms.EmailField(required=True)
	content=forms.CharField(
		required=True,
		widget=forms.Textarea
		)