from django.shortcuts import render


def index(request):
    return render(request, 'aplicacao/index.html')


def semana(request, semana):
    context = {}
    if semana == 'segunda':
        context = {
            'img': '/static/aplicacao/img.pmg',
            'semana': 'segunda-feira',
            'nome': 'Pizza',
            'descricao' : 'Pizza de pepperoni e 4 queijos.'
        }
    elif semana == 'terca':
        context = {
            'img': '/static/aplicacao/img.pmg',
            'semana': 'terca-feira',
            'nome': 'Sanduiche',
            'descricao' : 'Sanduiche de feito de pão, manteiga, presunto, queijo e aflface com tomate.'
        }
    elif semana == 'quarta':
        context = {
            'img': '/static/aplicacao/img.pmg',
            'semana': 'quarta-feira',
            'nome': 'estrogonofe falso',
            'descricao' : 'Estrogonofe de carne bovina com maizena, acompanhado de arroz, salada. '
        }
    elif semana == 'quinta':
        context = {
            'img': '/static/aplicacao/img.pmg',
            'semana': 'quinta-feira',
            'nome': 'sorvete',
            'descricao' : 'Sabores de napolitano, creme e mix de frutas.'
        }
    elif semana == 'sexta':
        context = {
            'img': '/static/aplicacao/img.pmg',
            'semana': 'sexta-feira',
            'nome': 'Bolhacha + suco',
            'descricao' : 'Bolachas de manteiga e suco de uvo 100% natural.'

        }

    return render(request, 'aplicacao/segunda.html', context)
