from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Question

#more descriptive index 
#def index(request):
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	template = loader.get_template('polls/index.html')
#	context = {
#		'latest_question_list': latest_question_list,
#	}
#	return HttpResponse(template.render(context, request))

#index in idiomatic django
#also mean we don't need to import loader and HttpResponse for this implementation
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

#descriptive
#def detail(request, question_id):
#	try:
#		question = Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404("Question does not exist")
#	return render(request, 'polls/detail.html', {'question': question})

#idiomatic	
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
#there's also get_list_or_404 which uses filter instead of get
	
def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response %question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
	