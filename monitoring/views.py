from django.shortcuts import render


def index(request):
    """Renderiza a página institucional e de entrada do sistema."""
    return render(request, "monitoring/index.html")
