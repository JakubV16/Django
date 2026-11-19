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

def du3_teplota(request):
    vysledok = None

    if request.method == "POST":
        teplota = float(request.POST.get("teplota"))
        smer = request.POST.get("smer")

        if smer == "C_F":
            vysledok = round(teplota * 9 / 5 + 32, 1)
            vysledok = str(vysledok) + " °F"

        elif smer == "F_C":
            vysledok = round((teplota - 32) * 5 / 9, 1)
            vysledok = str(vysledok) + " °C"

    return render(request, "domace/du3_teplota.html", {
        "vysledok": vysledok
    })