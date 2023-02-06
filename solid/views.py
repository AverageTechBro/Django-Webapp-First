from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import NewUserForm, UserProfileForm, BlogForm, MessageForm, HomeWatchForm
from solid.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def starter(request, id):
    watch = HomeWatch.objects.all()
    watches = HomeWatch.objects.filter(pk=id)
    context = {'watches': watches, 'watch': watch}
    return render(request, "home.html", context)


def home_watch(request):
    if request.method == 'POST':
        form = HomeWatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HomeWatchForm()
    home_watches = HomeWatch.objects.all()
    context = {
        'form': form,
        'home_watches': home_watches,
    }
    return render(request, 'home-watch.html', context)


def watch(request, id):
    watch = HomeWatch.objects.all()
    watches = HomeWatch.objects.filter(pk=id)
    context = {'watches': watches, 'watch': watch}
    return render(request, "watch.html", context)


def homeRedirect(request):
    return redirect('starter', id=1)


def register_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect("profile-pic")
            messages.error(
                request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
        return render(request=request, template_name="register.html", context={"register_form": form})
    else:
        return redirect("home")


def logout_user(request):
    logout(request)
    return redirect('home')


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('http://127.0.0.1:8000/1')
            else:
                messages.success(
                    request, ("There Was An Error Logging In, Try Again..."))
                return redirect('login')

        else:
            return render(request, 'login-page.html', {})
    else:
        return redirect('home')


def blog_user(request):
    context = {}
    return render(request, 'act-blog.html', context)


def blog_page(request, id):
    username = ""
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
    else:
        user = None

    blogs = Blogs.objects.all()
    blog = Blogs.objects.get(pk=id)

    if blog.user:
        try:
            profileImage = Profile.objects.get(user_id=blog.user.id)
        except Profile.DoesNotExist:
            profileImage = None
    else:
        profileImage = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blogPage = blog
            comment.user = user
            comment.save()
            messages.success(request, 'Comment posted successfully')
            return redirect(request.path)
    else:
        form = MessageForm()
        comments = Message.objects.filter(blogPage=blog).order_by('created_at')

    for comment in comments:
        try:
            profile = Profile.objects.get(user_id=comment.user.id)
            if profile.profile_pic:
                comment.profile_pic = profile.profile_pic
            else:
                comment.profile_pic = None
        except Profile.DoesNotExist:
            comment.profile_pic = None

    context = {"blogs": blogs, 'blog': blog,
               "username": username, 'bloguser': user, 'profile': profileImage, 'form': form, 'comments': comments.reverse()}
    return render(request, 'index.html', context)


def avatarView(request):

    if request.method == 'POST':

        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
    else:
        form = UserProfileForm()
    return render(request, 'profile-picpage.html', {'form': form})


def create_blog(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.user = request.user
                blog.save()
                return redirect('blogHome')
        else:
            form = BlogForm()
        return render(request, 'create-blog.html', {'form': form})
    else:
        return HttpResponse('You are not an Admin')


def blog_home(request):
    blogs = Blogs.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog-home-page.html', context)
