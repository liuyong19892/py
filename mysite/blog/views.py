#coding:utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>欢迎来到！</h1>")