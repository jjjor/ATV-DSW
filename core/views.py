from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import StudentForm

from .models import Student

# Create your views here.
def lista_estudantes(request):
    students = Student.objects.all()
    return render(request, 'core/lista_estudantes.html', {'students': students})
        
def criar_estudante(request):
    context = {'action': 'Criar'}
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:lista_estudantes'))
        else:
            context['form'] = form
            return render(request, 'core/form-est.html', context)
    else:
        context['form'] = StudentForm()
        return render(request, 'core/form-est.html', context)

def detalhar(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'core/detalhar.html', {'student': student})

def editar(request, student_id):
    context = {'action': 'Editar'}
    student = Student.objects.get(pk=student_id)
    if request.POST:
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:lista_estudantes'))
        else:
            context['form'] = form
            return render(request, 'core/form-est.html', context)
    else:
        
        form = StudentForm(instance=student)
        context['form'] = form

        return render(request, 'core/form-est.html', context)
    
def deletar_estudante(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return HttpResponseRedirect(reverse('core:lista_estudantes'))