from django.shortcuts import render
from django.http import HttpResponse

#Polls Index View

def index(request):
	return HttpResponse("Hello there")

#Details view
def detail(request, question_id):
	return HttpResponse("You are seeing details of question %s." % question_id)

#Result View
def results(request, question_id):
	return HttpResponse("You are seeing results of question %s." % question_id)


#Vote View
def vote(request, question_id):
	return HttpResponse("You are voting on question %s." % question_id)




