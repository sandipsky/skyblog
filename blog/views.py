from datetime import date
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='login')
def postCreate(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
        return redirect('/')
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'create.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def postManage(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'manage.html', context)

@login_required(login_url='login')
def postDelete(request, pk):
    item = Post.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('manage')
    context = {'item':item}
    return render(request, 'delete.html', context)

def register(request):
    form = CreateUser(request.POST)
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')