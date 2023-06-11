from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='core/change_password.html'), name='change_password'),
    path('password_changed/', auth_views.PasswordChangeDoneView.as_view(template_name='core/password_changed.html'), name='password_changed'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_html_video/', views.HTML, name='add_html_video'),
    path('add_css_video/', views.CSS, name='add_css_video'),
    path('add_js_video/', views.JAVASCRIPT, name='add_js_video'),
    path('add_python_video/', views.PYTHON, name='add_python_video'),
    path('html_comments/', views.htmlcomments, name='htmlcomments'),
    path('css_comments/', views.csscomments, name='csscomments'),
    path('js_comments/', views.jscomments, name='jscomments'),
    path('python_comments/', views.pythoncomments, name='pythoncomments'),
    path('add/', views.add, name='add'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('info/', views.info, name='info'),
    path('terms_and_condition/', views.terms_and_condition, name='terms_and_condition'),
]
