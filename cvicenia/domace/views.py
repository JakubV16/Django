from django.shortcuts import render
def domace1(request):
    kontext = {"meno": "Jakub Vrškový"}
    return render(request, "domace/domace1.html", kontext)


def du2_vizitka(request):
    data = {
        "meno": "Jakub Vrškový",
        "trieda": "3.AT",
        "vek": 17,
        "predmety": [
            "Programovanie",
            "Matematika",
            "Informatika",
        ],
    }

    return render(request, "domace/du2_vizitka.html", data)