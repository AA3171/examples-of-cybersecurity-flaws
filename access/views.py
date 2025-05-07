from django.http import HttpResponse
from django.template import loader

from .models import Question
from .forms import PostForm
from django.shortcuts import render
from django.http import HttpResponseRedirect




#Broken access control. Allows posting when not logged in
#from django.contrib.auth.decorators import login_required
#@login_required

def post_create(request):
    submitted = False
    if request.method == 'POST':
        form = PostForm(request.POST)
        #flaw 5
        #if form.is_valid():
        form.save()
        return HttpResponseRedirect('post_create?submitted=True')
    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'access/post_create.html', {'form': form, 'submitted':submitted})


    

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("access/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))