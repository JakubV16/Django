from django.shortcuts import render
def domace1(request):
    kontext = {"meno": "Jakub Vrškový"}
    return render(request, "domace/domace1.html", kontext)
