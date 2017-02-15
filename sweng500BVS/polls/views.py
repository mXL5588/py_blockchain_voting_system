from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from django.shortcuts import render
from .models import Ballot, Choice
from django.views import generic

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


##index manual vie
#def index(request):
#	latest_ballot_list = ballot.objects.order_by('-pub_date')[:5]
#	#template = loader.get_template('polls/index.html')
#	context = { 
#		'latest_ballot_list' : latest_ballot_list,
#	 }
#	
#	return render(request, 'polls/index.html', context)
	#return HttpResponse(template.render(context, request))

	#output = ', '.join([q.ballot_text for q in latest_ballot_list])
	#return HttpResponse(output)

##rewritten detail view
#def detail(request, ballot_id):
#	ballot = get_object_or_404(ballot, pk=ballot_id)
#	return render(request, 'polls/detail.html', {'ballot': ballot})

## detail view v2	
#def detail(request, ballot_id):
#	try:
#		ballot = ballot.objects.get(pk=ballot_id)
#	except ballot.DoesNotExist:
#		raise Http404("ballot does not exist")
#	return render(request, 'polls/detail.html', {'ballot': ballot})

# detail view v1
#def detail(request, ballot_id):
#	return HttpResponse("You're looking at ballot %s." % ballot_id)

##manual view 
#def results(request, ballot_id):
#	#response = "You're looking at the response of ballot %s." 
#	#return HttpResponse(response % ballot_id)
#	ballot = get_object_or_404(ballot, pk=ballot_id)
#	return render(request , 'polls/results.html', {'ballot':ballot})


def vote(request, ballot_id):
	#return HttpResponse("You're voting on ballot %s" % ballot_id)
	ballot = get_object_or_404(Ballot, pk=ballot_id)

	try:
			selected_choice = ballot.choice_set.get(pk=request.POST['choice'])

	except (KeyError, Choice.DoesNotExist):
		# Redisplay the ballot voting form
		return render(request, 'polls/detail.html', 
			{ 'ballot': ballot, 'error_message': "You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		# Always return an HTTPResponseRedirect after successfully dealing 
		# with POST data. This prevents data from being posted twice if a
		# user hits the back button.

		return HttpResponseRedirect(reverse('polls:results', args=(ballot.id,)))


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_ballot_list'

	def get_queryset(self):
		"""Return the last five published ballot"""
		return Ballot.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Ballot
	template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
	model = Ballot
	template_name = 'polls/results.html'
	