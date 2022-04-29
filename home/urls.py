from django.urls import path
from home import views

urlpatterns = [
    path("", views.render_maintenance),
    path(".well-known/acme-challenge/<str:id>", views.send_code),
]
