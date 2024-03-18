from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Aplicação de Enquetes - DSWeb 2024.1: <br> Disciplina: Desenvolvimento de Sistemas Web <br> Semestre: 2024.1 <br> Matrícula do aluno: 20231014040007 <br> Nome do discente: Yasmim Raposo')




