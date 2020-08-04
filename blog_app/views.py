from django.shortcuts import render,get_object_or_404,redirect
from blog_app.forms import CommentForm,PostForm,ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from blog_app.serializers import PostSerializer
from rest_framework import viewsets


# Create your views here.
from blog_app.models import Post
from django.views.generic import ( 
    View,
	DetailView,
	ListView,
	UpdateView,
    CreateView,)



class PostList(ListView):
	# queryset=Post.objects.filter(status=1).order_by('-created_on')
    queryset=Post.objects.all().order_by('-created_on')
    template_name='index.html'


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            # new_comment.slug=slugify(new_comment.title)
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    print(comment_form)
    # print(post)

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class PostCreateView(LoginRequiredMixin,CreateView):
    form_class=PostForm
    template_name="create_form.html"
    
    login_url="/login/"
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.author=self.request.user
        return super(PostCreateView, self).form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context=super(PostCreateView,self).get_context_data(*args,**kwargs)
        return context
    def get_success_url(self):
        return reverse('blog:Home')
    # queryset=Post.objects.filter(status=1).order_by('-created_on')
    # template_name='index.html'

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all().order_by('-created_on')
    serializer_class=PostSerializer

def contact(request):
    if request.method=="GET":
        form=ContactForm()
    else:
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['contact_name']
            email=form.cleaned_data['contact_email']
            message=form.cleaned_data['content']
            try:
                send_mail("Feedback on Blog from"+name,
                    message,
                    email,['admin@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header information')
    context={'form':form}
    return render(request, "contact_form.html",context)

