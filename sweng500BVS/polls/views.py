from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from django.shortcuts import render
from .models import Choice, Question
from django.views import generic

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


##index manual vie
#def index(request):
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	#template = loader.get_template('polls/index.html')
#	context = { 
#		'latest_question_list' : latest_question_list,
#	 }
#	
#	return render(request, 'polls/index.html', context)
	#return HttpResponse(template.render(context, request))

	#output = ', '.join([q.question_text for q in latest_question_list])
	#return HttpResponse(output)

##rewritten detail view
#def detail(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'polls/detail.html', {'question': question})

## detail view v2	
#def detail(request, question_id):
#	try:
#		question = Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404("Question does not exist")
#	return render(request, 'polls/detail.html', {'question': question})

# detail view v1
#def detail(request, question_id):
#	return HttpResponse("You're looking at question %s." % question_id)

##manual view 
#def results(request, question_id):
#	#response = "You're looking at the response of question %s." 
#	#return HttpResponse(response % question_id)
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request , 'polls/results.html', {'question':question})


def vote(request, question_id):
	#return HttpResponse("You're voting on question %s" % question_id)
	question = get_object_or_404(Question, pk=question_id)

	try:
			selected_choice = question.choice_set.get(pk=request.POST['choice'])

	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form
		return render(request, 'polls/detail.html', 
			{ 'question': question, 'error_message': "You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		# Always return an HTTPResponseRedirect after successfully dealing 
		# with POST data. This prevents data from being posted twice if a
		# user hits the back button.

		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest question listed'

	def get_queryset(self):
		"""Return the last five published question"""
		return Quesiton.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
	