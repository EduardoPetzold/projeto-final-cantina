from django.shortcuts import render

def index(request):
    return render(request, 'aplicacao/index.html')

def semana(request, semana):
    context = {}
    if semana == 'segunda':
        context = {
            'img': '/static/aplicacao/img.pmg',
            'semana':'segunda-feira'
        }

        return render(request, 'aplicacao/segunda.html',context)
