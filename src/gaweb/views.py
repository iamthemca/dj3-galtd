from django.shortcuts import render
from portfolio.models import Portfolio

def index(request):

    return render(request, 'index.html',{})

def portfolio(request):
    queryset=Portfolio.objects.filter(featured=True)
    context={'object_list':queryset}
    return render(request, 'portfolio.html',context)
