from datetime import date
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    recents = Post.objects.all().order_by('-id')[:5]
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts':posts, 'recents':recents, 'page_obj': page_obj}
    return render(request, 'index.html', context)



def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render(request, 'detail.html', context)

def postCreate(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'create.html', context)

def postUpdate(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'edit.html', context)
