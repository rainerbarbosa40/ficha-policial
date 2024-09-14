from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import FichaPolicial
from .forms import FichaPolicialForm

def editar_ficha(request, matr):
    ficha = get_object_or_404(FichaPolicial, matr=matr)
    
    if request.method == 'POST':
        form = FichaPolicialForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()  # Salva as alterações
            messages.success(request, 'Alterações realizadas com sucesso!')
            return redirect('index')  # Redireciona após salvar
    else:
        form = FichaPolicialForm(instance=ficha)

    return render(request, 'app_ficha_policial/editar_ficha.html', {'form': form})


def adicionar_ficha(request):
    if request.method == 'POST':
        # Captura os dados do formulário
        grad = request.POST.get('grad')
        matr = request.POST.get('matr')
        nome = request.POST.get('nome')
        ome = request.POST.get('ome')
        dispo = request.POST.get('dispo')
        sexo = request.POST.get('sexo')
        cpf = request.POST.get('cpf')
        quadro = request.POST.get('quadro')
        rg = request.POST.get('rg')

        # Cria uma nova instância do modelo e salva no banco de dados
        ficha = FichaPolicial(
            grad=grad,
            matr=matr,
            nome=nome,
            ome=ome,
            dispo=dispo,
            sexo=sexo,
            cpf=cpf,
            quadro=quadro,
            rg=rg
        )
        ficha.save()

        # Exibe uma mensagem de sucesso
        messages.success(request, 'Ficha policial adicionada com sucesso!')
        
        # Redireciona para a página de índice
        return redirect('index')

    return render(request, 'app_ficha_policial/adicionar_ficha.html')
    

def verificar_posto_ou_graduacao(grad):
    postos = ["MAJ", "CAP", "CEL", "1º TEN", "2º TEN", "TC"]
    return "Posto" if grad in postos else "Graduação"

def index(request):
    fichas = None
    if 'matricula' in request.GET or 'nome' in request.GET:
        matricula = request.GET.get('matricula')
        name = request.GET.get('nome')
        nome = name.upper() 
        if matricula:
            fichas = FichaPolicial.objects.filter(matr=matricula)
        elif nome:
            fichas = FichaPolicial.objects.filter(nome__icontains=nome)

    # Adiciona dados da tropa
    tropa = FichaPolicial.objects.all()
    total_geral = len(tropa)
    ciatur = FichaPolicial.objects.filter(ome='CIATUR') 
    total = len(ciatur)

    # Processa o tipo de graduação ou posto e adiciona como nova chave no dicionário de contexto
    if fichas:
        for ficha in fichas:
            ficha.tipo_grad = verificar_posto_ou_graduacao(ficha.grad)

    if tropa:
        for ficha in tropa:
            ficha.tipo_grad = verificar_posto_ou_graduacao(ficha.grad)

    if ciatur:
        for ficha in ciatur:
            ficha.tipo_grad = verificar_posto_ou_graduacao(ficha.grad)

    return render(request, 'app_ficha_policial/index.html', {
        'fichas': fichas,
        'ficha': tropa,
        'bpm': ciatur,
        'quant_total': total,
        'quant_total_geral': total_geral
    })
