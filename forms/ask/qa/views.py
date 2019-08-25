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
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)

    if request.method == "POST":         
        form = AskForm(request.POST)         
        if form.is_valid():
            form._author = request.user
            question = form.save()             
            url = "/question/" + str(question.id) + "/"
            return HttpResponseRedirect(url)     
    else:         
        form = AskForm()     
    return render(request, 'ask_form.html', { 'form': form })

def question(request, id):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized', status=401)
    
    url = "/question/" + str(id) + "/"
    question = Question.objects.get(id=id, author=request.user)
    if request.method == "POST":         
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._author = request.user
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
            url = request.POST.get('continue', '/')
            response = HttpResponseRedirect(url)
            response.set_cookie(
                'sessionid', 
                request.session.session_key,                 
                httponly=True             
            )     
            return response
    else:         
        form = SignupForm()     
    return render(request, 'singup_form.html', { 'form': form })


def login(request):
    if request.method == "POST":         
        form = LoginForm(request.POST)         
        if form.is_valid():             
            user = form.save(request)
            username = request.POST['username']
            password = request.POST['password']
            from django.contrib.auth import authenticate, login
            user = authenticate(request, username=username, password=password)
            if user is not None:             
                login(request, user)
                url = request.POST.get('continue', '/')
                response = HttpResponseRedirect(url)
                response.set_cookie(
                    'sessionid', 
                    request.session.session_key,                 
                    httponly=True             
                )
                return response
            #return HttpResponse('Login/password', status=401)
    else:         
        form = LoginForm()     
    return render(request, 'login_form.html', { 'form': form })

