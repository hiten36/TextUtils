from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyzer(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    punc='''!@#$%^&*()_={}[]~,;:"'?\/'''
    if removepunc=='on':
        my_text = ""
        for i in djtext:
            if i not in punc:
                my_text+=i
        d={'purpose':'Remove punctuations', 'texts':my_text}
        djtext=my_text
    fullcaps=request.POST.get('fullcaps','off')

    if fullcaps=='on':
        my_text = ""
        for i in djtext:
            my_text+=i.upper()
        d={'purpose':'Capitalization of input', 'texts':my_text}
        djtext=my_text
    exlines=request.POST.get('exlines','off')
    if exlines=='on':
        my_text = ""
        for i in djtext:
            if i!='\n' and i!='\r':
                my_text+=i
        d={'purpose':'removed the extra lines', 'texts':my_text}
        djtext=my_text
    exspaces=request.POST.get('exspaces','off')
    if exspaces=='on':
        my_text = ""
        for index,i in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                my_text+=i
        d={'purpose':'Removed the extra spaces', 'texts':my_text}
        djtext=my_text
    if(removepunc=='off' and fullcaps=='off' and exlines=='off' and exspaces=='off'):
        my_text=djtext
        d={'purpose':'none','texts':my_text}
    return render(request,'analyze.html',d)
def about(request):
    return render(request,'about.html')
def contact(requests):
    return render(requests,'contact.html')