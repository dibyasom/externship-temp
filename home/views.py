from django.shortcuts import render

# Create your views here.
def render_maintenance(request):
    return render(request, "maintenance.html")
