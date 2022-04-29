from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def render_maintenance(request):
    return render(request, "maintenance.html")


def send_code(request, id:str):
    return HttpResponse(
        "Zva01f4ZXQDUmsS_n6vhbp9rkIN8euLFRCZPAOWcUGk.HQ5lDu_UAZIjJtPpHnc49nz3gFeXbMdH_dmJR3POoNc"
    )
