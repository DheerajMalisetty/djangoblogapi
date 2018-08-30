from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .forms import PostForm
from .models import Post
# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()

    context = {
        "form": form,
    }
    return render(request, "postform.html", context)

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context={
        "title": instance.title,
        "instance" : instance
    }
    return render(request, "postdetail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "index.html", context)

def post_update(request, id=None):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "postform.html", context)

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")