from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .forms import SignupForm, LoginForm
from comment.models import HTML as html
from comment.models import CSS as css
from comment.models import JAVASCRIPT as js
from comment.models import PYTHON as python
from .forms1 import *
from .forms2 import *
from comment.models import *


@login_required
def index(request):
     htmlinfo = html.objects.all()
     cssinfo = css.objects.all()
     jsinfo = js.objects.all()
     pythoninfo = python.objects.all()
     html_comment = HTMLComments.objects.all()
     css_comment = CSSComments.objects.all()
     js_comment = JSComments.objects.all()
     python_comment = PythonComments.objects.all()
     return render(request, 'core/index.html', {
          'html': htmlinfo,
          'css': cssinfo,
          'js': jsinfo,
          'python': pythoninfo,
          'htmlcomment': html_comment,
          'csscomment': css_comment,
          'jscomment': js_comment,
          'pythoncomment': python_comment,
     })

def signup(request):
     if request.method == 'POST':
          form = SignupForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/login/')
     else:
          form = SignupForm()
     return render(request, 'core/signup.html', {
          'form': form   
     })

def login(request):
     form = LoginForm()
     return render(request, 'core/login.html', {
          'form': form
     })

@login_required
def HTML(request):
     if request.method == 'POST':
          form = HTMLForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     else:
          form = HTMLForm()
     return render(request, 'core/html.html', {
          'form': form
     })

@login_required
def CSS(request):
     if request.method == 'POST':
          form = CSSForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     else:
          form = CSSForm()
     return render(request, 'core/css.html', {
          'form': form
     })

@login_required
def JAVASCRIPT(request):
     if request.method == 'POST':
          form = JSForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     else:
          form = JSForm()
     return render(request, 'core/javascript.html', {
          'form': form
     })

@login_required
def PYTHON(request):
     if request.method == 'POST':
          form = PYTHONForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     else:
          form = PYTHONForm()
     return render(request, 'core/python.html', {
          'form': form
     })

@login_required
def htmlcomments(request):
     if request.method == 'POST':
          form = HTMLCommentForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     else:
          form = HTMLCommentForm()
     return render(request, 'core/comments.html', {
          'form': form
     })
@login_required
def csscomments(request):
     if request.method == 'POST':
          form = CSSCommentForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     else:
          form = CSSCommentForm()
     return render(request, 'core/comments.html', {
          'form': form
     })
@login_required
def jscomments(request):
     if request.method == 'POST':
          form = JSCommentForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     else:
          form = JSCommentForm()
     return render(request, 'core/comments.html', {
          'form': form
     })
@login_required
def pythoncomments(request):
     if request.method == 'POST':
          form = PYTHONCommentForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     else:
          form = PYTHONCommentForm()
     return render(request, 'core/comments.html', {
          'form': form
     })

@login_required
def add(request):
     return render(request, 'core/add.html', {})

@login_required
def myaccount(request):
     return render(request, 'core/myaccount.html')

def info(request):
     return render(request, 'core/info.html', {})

def terms_and_condition(request):
     return render(request, 'core/terms_and_condition.html', {})
