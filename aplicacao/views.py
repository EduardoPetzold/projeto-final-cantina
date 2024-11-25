from django.shortcuts import render

def index(request):
    return render(request, 'aplicacao/index.html')
def index2(request):
    return render(request, 'aplicacao/segunda.html')
