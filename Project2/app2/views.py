from django.shortcuts import HttpResponse
def showMain(request):
    return HttpResponse("<html><body bgcolor='yellow'><h1>HelloWorld</h1></body></html>")
