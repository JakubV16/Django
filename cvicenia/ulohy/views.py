from django.shortcuts import render, HttpResponse 
from datetime import date

def ahoj(request):
    return HttpResponse("Ahoj Svet!")

def o_mne(request):
    kontext = {
        "meno": "Jakub",
        "vek": 17,
        "zaluby":["skola", "matematika", "hokej"],
    }
    return render(request, "ulohy/o_mne.html", kontext)

def rozvrh(request):
    hodiny = [
        {"cislo": 1,"predmet": "Programovanie"},
        {"cislo": 2,"predmet": "Programovanie"},
        {"cislo": 3,"predmet": "Matematika"},
        {"cislo": 4,"predmet": "Prax"},
        {"cislo": 5,"predmet": "Prax"},
        {"cislo": 6,"predmet": "Anglický jazyk"},
    ]
    return render(request, "ulohy/rozvrh.html", {"den": "Pondelok", "hodiny":hodiny})

def pozdrav(request):
    meno = request.GET.get("meno", "")
    return render(request, "ulohy/pozdrav.html", {"meno":meno})

def sucet(request):
    vysledok= None
    if request.method == "POST":
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        vysledok= a + b
    return render(request, "ulohy/sucet.html", {"vysledok": vysledok})



def kalkulacka(request):
    vysledok = None

    if request.method == "POST":
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        operacia = request.POST["operacia"]

        if operacia == "+":
            vysledok = a + b
        elif operacia == "-":
            vysledok = a - b
        elif operacia == "*":
            vysledok = a * b

    return render(request, "ulohy/kalkulacka.html", {
        "vysledok": vysledok
    })



def obdlznik(request):
    obvod = None
    obsah = None

    if request.method == "POST":
        sirka = float(request.POST["sirka"])
        vyska = float(request.POST["vyska"])

        obvod = round(2 * (sirka + vyska), 2)
        obsah = round(sirka * vyska, 2)

    return render(request, "ulohy/obdlznik.html", {"obvod": obvod, "obsah": obsah})


def vek(request):
    vek = None

    if request.method == "POST":
        rok = int(request.POST["rok"])
        dnes = date.today()

        vek = dnes.year - rok

    return render(request, "ulohy/vek.html", {"vek": vek})
