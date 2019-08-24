from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

from django.shortcuts import render, get_object_or_404 
from django.views.decorators.http import require_GET 
from django.core.paginator import Paginator 
from qa.models import Question, Answer

def get_question_paginated_render(request, base_url, questions, limit=10):
    page = request.GET.get('page', 1)     
    paginator = Paginator(questions, limit)     
    paginator.baseurl = base_url #'/?page='     
    page = paginator.page(page)     
    return render(request, 'questions_by_page.html', {     
        'questions':  page.object_list,
        'question_base_url' : '/question',
        'paginator': paginator, 
        'page': page,     
    })

@require_GET
def main(request):
    questions = Question.objects.new()     
    return get_question_paginated_render(request, '/?page=', questions)

@require_GET
def popular(request):
    questions = Question.objects.new()     
    return get_question_paginated_render(request, '/popular/?page=', questions) 

@require_GET
def question(request, id):
    question = get_object_or_404(Question, id=id)
    try:
        answers = Answer.objects.filter(question=question) 
    except Answer.DoesNotExist:
        answers=[]
    return render(request, 'question_page.html', {
        'question' : question,
        'answers': answers
    }) 