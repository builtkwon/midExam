from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic


# Create your views here.

def index(request):
    #return HttpResponse("하이요")
    latest_question_list= Question.objects.order_by('-pub_date')[:5]

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    #template = loader.get_template('poll/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})

def results(request, question_id):
    # response = HttpResponse("results of Question %s." %question_id)
    # return response
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request, question_id):
    #return HttpResponse("voting on Question %s." %question_id)

    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        #질문 투표 폼 다시 보여주기
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def main(request):
#     return redirect('polls/index')


#제너릭 뷰
class IndexView(generic.ListView): #ListView : 리스트 출력
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' #html에 전달할 파라미터명

    """Return the last five published questions."""
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView): #DetailView : 특정오브젝트의 자세한 정보 출력
    model = Question #대상
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'