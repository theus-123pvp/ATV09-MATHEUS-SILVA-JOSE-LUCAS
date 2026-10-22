from django.shortcuts import get_object_or_404, render
from .models import Conteudo, Menu


def itens_menu():
    return Menu.objects.filter(ativo=True).select_related("conteudo").order_by("ordem", "titulo")


def inicio(request):
    conteudo_inicial = Conteudo.objects.filter(slug="inicio", ativo=True).first()
    if conteudo_inicial:
        return render(request, "portal/conteudo.html", {"conteudo": conteudo_inicial, "itens_menu": itens_menu(), "pagina_inicial": True})
    return render(request, "portal/inicio.html", {"itens_menu": itens_menu()})


def exibir_conteudo(request, slug):
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)
    return render(request, "portal/conteudo.html", {"conteudo": conteudo, "itens_menu": itens_menu(), "pagina_inicial": False})
