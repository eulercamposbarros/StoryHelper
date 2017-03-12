from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from composer.forms import *
from django.shortcuts import redirect, reverse
from composer.models import *
from django.contrib.auth import logout
from composer.services import findsequence

def home(request):
    session_id = request.session.session_key

    if request.session.session_key == None: request.session.create()

    if request.method == 'POST':
        form = IniciarHistoriaForm(request.POST)
        if form.is_valid():
            Historia.objects.create(session=request.session.session_key, estilo=form.cleaned_data['estilo'])
            return redirect('historia')

    historia = Historia.objects.filter(session=request.session.session_key).first()

    if historia != None:
        if historia.historia_finalizada():
            del request.session
            request.session.modified = True
        else:
            return redirect('historia')

    form = IniciarHistoriaForm()

    return render(
        request,
        'index.html',
        {
            'year': datetime.now().year,
            'form': form,
        }
    )

def historia(request):
    historia = Historia.objects.filter(session=request.session.session_key).first()

    if historia == None: return redirect('home')

    if request.method == 'POST':
        form = HistoriaForm(request.POST)
        if 'registrar' in request.POST and form.is_valid() and len(form.cleaned_data['parte']) > 0:
            parte = form.cleaned_data['parte']
            historia.incluir_parte(texto=parte, criado_pelo_usuario=False)
            historia.incluir_parte(texto=findsequence(parte), criado_pelo_usuario=True)
        elif 'finalizar' in request.POST: 
            return redirect('avaliacao')

    form = HistoriaForm()

    return render(
        request,
        'historia.html',
        {
            'year': datetime.now().year,
            'form': form,
            'historia': [{'text': p.texto, 'user': p.criado_pelo_usuario} for p in historia.parte_set.all()]
        }
    )


def avaliacao(request):
    if request.session.session_key == None: return redirect('home')
    historia = Historia.objects.filter(session=request.session.session_key).first()
    if historia == None: return redirect('home')

    if historia.parte_set.all().count() == 0: return redirect('historia')

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)

        if historia != None and form.is_valid():
            historia.incluir_avaliacao(coerencia=form.cleaned_data['coerencia'],
                                       diversao=form.cleaned_data['diversao'],
                                       comentario=form.cleaned_data['comentario'])

        logout(request)
        return redirect(reverse('home') + '?sucesso=1')

    form = AvaliacaoForm()
    return render(
        request,
        'avaliacao.html',
        {
            'year': datetime.now().year,
            'form': form,
        }
    )

