from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
"""
gets the question ID parsed by the user in the URL
question_id here is public key
"""

from django.template import loader
from . models import Question


def index(request):
    """latest goes to the database picks all
        instances(object) of Question and returns them as a list.
    The objects were created at the admin or through console using
    q = Question(question_text="Whats up", pub_date=timezone.now())
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def details(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question Not Found')
    """
    question = get_object_or_404(Question, pk=question_id)  # same as the code in docstring only difference is that it does allow custom error message
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    return HttpResponse("You are looking at the results of %s" % (question_id))


def votes(request, question_id):
    return HttpResponse("You are looking at the Vote for %s" % (question_id))
