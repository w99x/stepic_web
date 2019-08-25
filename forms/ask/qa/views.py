from django.http import HttpResponse, HttpResponseRedirect
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
    questions = Question.objects.popular()     
    return get_question_paginated_render(request, '/popular/?page=', questions) 

from qa.forms import *
def ask(request):
    user = request.author
    if user is None:
        return HttpResponse('Unauthorized', status=401)
    if request.method == "POST":         
        form = AskForm(request.POST)         
        if form.is_valid():
            form._author = user
            question = form.save()             
            url = "/question/" + str(question.id) + "/"
            return HttpResponseRedirect(url)     
    else:         
        form = AskForm()     
    return render(request, 'ask_form.html', { 'form': form })

def question(request, id):
    user = request.author
    if user is None:
        return HttpResponse('Unauthorized', status=401)
    url = "/question/" + str(id) + "/"
    question = Question.objects.get(id=id, author=user)
    if request.method == "POST":         
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._author = user
            answer = form.save(id)             
            return HttpResponseRedirect(url)     
    else:         
        form = AnswerForm()     
    return render(request, 'answer_form.html', { 'form': form, 'url': url })

 
def signup(request):
    if request.method == "POST":         
        form = SignupForm(request.POST)         
        if form.is_valid():             
            user = form.save()
            import uuid
            session = Session(user=user, key=str(uuid.uuid4()), expires=datetime.now() + timedelta(days=5))
            url = request.POST.get('continue', '/')
            response = HttpResponseRedirect(url)
            response.set_cookie(
                'sessionid', 
                session.key,                 
                httponly=True,                
                expires = session.expires             
            )     
            return response
    else:         
        form = SignupForm()     
    return render(request, 'singup_form.html', { 'form': form })


def login(request):
    if request.method == "POST":         
        form = LoginForm(request.POST)         
        if form.is_valid():             
            session = form.save()             
            url = request.POST.get('continue', '/')
            response = HttpResponseRedirect(url)
            response.set_cookie(
                'sessionid', 
                session.key,                 
                httponly=True,                
                expires = session.expires             
            )
            return response
    else:         
        form = LoginForm()     
    return render(request, 'login_form.html', { 'form': form })

