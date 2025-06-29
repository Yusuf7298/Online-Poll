from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class QuizListView(ListView):
    model = Quiz
    template_name='quizes/main.html'

def quiz_view(request,pk):
    quiz = Quiz.objects.get(id=pk)
    return render(request, 'quizes/quiz.html',{'obj': quiz})


def quiz_data_view(request, pk):
    quiz=Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q):answers})

    return JsonResponse({
        'data':questions,
        'time':quiz.time
    })

def save_quiz_view(request, pk):
    if request.is_ajax():
        data = request.POST
        data_ = dict(data.lists())
        print(data_)
        data_.pop('csrfmiddlewaretoken')
        print(data_)
    return JsonResponse({'text':'works'})