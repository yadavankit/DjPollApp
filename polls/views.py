from django.shortcuts import render
from django.http import HttpResponse

#Polls Index View

def index(request):
	return HttpResponse("Hello there")
