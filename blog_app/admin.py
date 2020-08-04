from django.contrib import admin

# Register your models here.
from blog_app.models import ( Post,Comment )


class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','status','created_on','category')
	list_filter=('status','category')
	search_fields=['title','content']
	prepopulated_fields={'slug':('title',)}
admin.site.register(Post, PostAdmin)
class CommentAdmin(admin.ModelAdmin):
	list_display=('name','body','post','created_on','active',)
	list_filter=('active','created_on')
	search_fields=['name','email','body']
	actions=['approve_comments']

	def approve_comments(self,request,queryset):
		queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)
