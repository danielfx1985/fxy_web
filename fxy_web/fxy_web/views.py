import requests
from django.shortcuts import render,redirect
import xlwt
from django_tables2 import SingleTableView
import django_tables2 as tables
from django_tables2.export.views import ExportMixin
from django_tables2.export.export import TableExport

# Create your views here.
from django.http import HttpResponse
from django.views import generic

def start(request):
   # return render(request,'start.html')
   return HttpResponse('你好')