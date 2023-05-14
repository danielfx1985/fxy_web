from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path,re_path
from django.views.generic import TemplateView
from django.views.i18n import set_language
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.views import LoginView
from mezzanine.conf import settings
from . import views

urlpatterns=[
    path('', views.book_list, name='book_list'),
    path('upload/', login_required(views.book_upload), name='book_upload'),
    path('search/', views.book_search, name='book_search'),
    path('delete/<int:id>/', views.book_delete, name='book_delete'),
]