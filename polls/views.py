from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-date_pub')[:5]

    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def results(request, pk):
    question = get_object_or_404(Question, id=pk)
    context = {
        'question':question,
    }
    return render(request, 'polls/results.html', context)

def details(request, pk):
    question = Question.objects.get(id=pk)

    context = {
        'question':question,
    }

    return render(request, 'polls/details.html', context)

def vote(request, pk):
    question = get_object_or_404(Question, id=pk)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponse('Thanks for voting')
        #return HttpResponseRedirect(reverse((question.id), 'polls:results' ))
