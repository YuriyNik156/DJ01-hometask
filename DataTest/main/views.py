from django.http import HttpResponse


def data_view(request):
    return HttpResponse("<h1>Это страница DATA</h1>")

def test_view(request):
    return HttpResponse("<h1>А это страница TEST</h1>")
