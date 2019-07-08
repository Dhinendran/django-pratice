from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from .models import Post,Comment
from datetime import datetime
from .forms import CommentForm

# Create your views here.

def index(request):
    date = datetime.now().strftime('%Y-%m-%d')
    return render(request,'blog/index.html', {'date':date})
def post_list(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404("Post does not Exists")
    return render(request,'blog/post_list.html', {'posts':posts})
def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    c_number= len(Comment.objects.filter(post_id=pk))
    return render(request, 'blog/post_detail.html',{"post":post,"c_number":c_number})

def post_comment(request,pk):
    comments=Comment.objects.filter(post_id=pk)
    p_id=pk
    return render(request,'blog/comment.html',{"comments":comments,"p_id":p_id})
def add_comment(request,pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name =request.POST["name"]
            comment.comment =request.POST["comment"]
            comment.post_id=pk
            comment.save()
            return redirect('post_detail',pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html',{'form':form})