from django.shortcuts import render

# Create your views here.

def alunos(request):
    return render(request, 'alunos.html')

def new_register(request):
    return render(request, 'new-register.html')

